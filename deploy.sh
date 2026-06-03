#!/bin/bash
set -e

SITE_DIR="/root/goodinfo-site"
REMOTE="root@43.153.121.114"
REMOTE_DIR="/www/wwwroot/goodinfo.net"
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
rsync -avz --delete -e "ssh -i $KEY -o StrictHostKeyChecking=no" public/ ${REMOTE}:${REMOTE_DIR}/ >> $LOG 2>&1 || true
echo "[$(date)] Deploy complete." >> $LOG
