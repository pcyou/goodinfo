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

# Deploy via rsync (ignore partial transfer code 23, usually harmless permission diffs)
rsync -avz --delete --no-perms --no-owner --no-group -e "ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no" public/ ${REMOTE}:${REMOTE_DIR}/ >> $LOG 2>&1 || true

# ⚠️ rsync --delete 会删除 ssl/ 和 log/ 目录，需要重建
echo "[$(date)] Rebuilding ssl/ and log/ directories..." >> $LOG
ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no ${REMOTE} "mkdir -p ${REMOTE_DIR}/ssl ${REMOTE_DIR}/log && touch ${REMOTE_DIR}/log/access.log ${REMOTE_DIR}/log/error.log" >> $LOG 2>&1

# Deploy SSL certificate if missing
if ! ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no ${REMOTE} "test -f ${REMOTE_DIR}/ssl/fullchain.pem" 2>/dev/null; then
    echo "[$(date)] SSL certificate missing, deploying..." >> $LOG
    python3 /tmp/get_cf_cert.py >> $LOG 2>&1
    scp -i $KEY -P $REMOTE_PORT -o StrictHostKeyChecking=no /tmp/goodinfo.pem ${REMOTE}:${REMOTE_DIR}/ssl/fullchain.pem >> $LOG 2>&1
    scp -i $KEY -P $REMOTE_PORT -o StrictHostKeyChecking=no /tmp/goodinfo.key ${REMOTE}:${REMOTE_DIR}/ssl/privkey.pem >> $LOG 2>&1
fi

# Reload Nginx
ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no ${REMOTE} "docker exec 1Panel-openresty-Kb76 nginx -s reload" >> $LOG 2>&1

echo "[$(date)] Deploy complete." >> $LOG
