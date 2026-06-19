#!/bin/bash
set -e

SITE_DIR="/root/goodinfo-site"
REMOTE="root@46.225.168.78"
REMOTE_PORT="16651"
REMOTE_DIR="/www/sites/goodinfo.net"
KEY="/root/.ssh/id_rsa_hermes_migration"
LOG="/var/log/goodinfo-deploy.log"

echo "[$(date)] Starting build & deploy..." >> $LOG
cd $SITE_DIR

# Build
hugo --minify >> $LOG 2>&1

# Fix Hugo multilingual root index.html (often empty)
if [ ! -s "$SITE_DIR/public/index.html" ] && [ -s "$SITE_DIR/public/zh/index.html" ]; then
    cp "$SITE_DIR/public/zh/index.html" "$SITE_DIR/public/index.html"
    echo "[$(date)] Patched empty root index.html from zh/" >> $LOG
fi

echo "[$(date)] Build successful." >> $LOG

# Deploy via rsync — exclude ssl/ and log/ to preserve certs and logs
rsync -avz --delete --exclude='ssl/' --exclude='log/' --no-perms --no-owner --no-group \
    -e "ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no" \
    public/ ${REMOTE}:${REMOTE_DIR}/ >> $LOG 2>&1 || true

echo "[$(date)] Files synced." >> $LOG

# Ensure log directory exists
ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no ${REMOTE} \
    "mkdir -p ${REMOTE_DIR}/log && touch ${REMOTE_DIR}/log/access.log ${REMOTE_DIR}/log/error.log" >> $LOG 2>&1

# Check SSL cert — renew via acme.sh if expiring within 30 days or missing
CERT_EXPIRY=$(ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no ${REMOTE} \
    "openssl x509 -enddate -noout -in ${REMOTE_DIR}/ssl/fullchain.pem 2>/dev/null | cut -d= -f2" 2>/dev/null || echo "")

NEED_RENEW=true
if [ -n "$CERT_EXPIRY" ]; then
    EXPIRY_EPOCH=$(date -d "$CERT_EXPIRY" +%s 2>/dev/null || echo 0)
    NOW_EPOCH=$(date +%s)
    DAYS_LEFT=$(( (EXPIRY_EPOCH - NOW_EPOCH) / 86400 ))
    if [ "$DAYS_LEFT" -gt 30 ]; then
        NEED_RENEW=false
        echo "[$(date)] SSL cert valid for ${DAYS_LEFT} more days, skipping renewal." >> $LOG
    else
        echo "[$(date)] SSL cert expires in ${DAYS_LEFT} days, renewing..." >> $LOG
    fi
else
    echo "[$(date)] SSL certificate missing, issuing new one..." >> $LOG
fi

if [ "$NEED_RENEW" = true ]; then
    # Use acme.sh on remote to issue/renew via Let's Encrypt HTTP-01
    ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no ${REMOTE} bash -s << 'REMOTE_EOF' >> /var/log/goodinfo-deploy.log 2>&1
        set -e
        REMOTE_DIR="/www/sites/goodinfo.net"
        CONF_BACKUP="/tmp/goodinfo.net.conf.bak"
        CONTAINER="1Panel-openresty-Kb76"
        CONF_PATH="/usr/local/openresty/nginx/conf/conf.d/goodinfo.net.conf"

        # Backup current config
        docker exec $CONTAINER cat $CONF_PATH > $CONF_BACKUP

        # Temporarily switch to HTTP-only for ACME challenge
        python3 -c "
config = '''server {
    listen 80;
    server_name goodinfo.net www.goodinfo.net *.goodinfo.net;
    root /www/sites/goodinfo.net;
    index index.html;
    location ^~ /.well-known/acme-challenge {
        allow all;
        root /www/sites/goodinfo.net;
    }
}
'''
with open('/tmp/goodinfo-temp.conf', 'w') as f:
    f.write(config)
"
        docker cp /tmp/goodinfo-temp.conf $CONTAINER:$CONF_PATH
        docker exec $CONTAINER nginx -s reload
        sleep 2

        # Issue cert via acme.sh + Let's Encrypt
        cd ~/.acme.sh
        ./acme.sh --issue --domain goodinfo.net --webroot $REMOTE_DIR --server letsencrypt --force

        # Install cert to ssl/ directory
        cp ~/.acme.sh/goodinfo.net_ecc/fullchain.cer $REMOTE_DIR/ssl/fullchain.pem
        cp ~/.acme.sh/goodinfo.net_ecc/goodinfo.net.key $REMOTE_DIR/ssl/privkey.pem

        # Restore original config and reload
        docker cp $CONF_BACKUP $CONTAINER:$CONF_PATH
        docker exec $CONTAINER nginx -t
        docker exec $CONTAINER nginx -s reload
REMOTE_EOF
    echo "[$(date)] SSL cert renewed via acme.sh." >> $LOG
fi

# Reload Nginx (final, in case cert was already valid)
ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no ${REMOTE} "docker exec 1Panel-openresty-Kb76 nginx -s reload" >> $LOG 2>&1

echo "[$(date)] Deploy complete." >> $LOG
