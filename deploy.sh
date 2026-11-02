#!/bin/bash
# GoodInfo build & deploy
#
# ⚠️ 2026-10-30 hardening (see skill ref deploy-run-verification-2026-10-30.md):
#   1. flock serialisation — two cron jobs (goodinfo-daily-build 0 8 * * * and
#      GoodInfo GitHub Trending 0 */4 * * *) fired at 08:00 and both ran this
#      script, corrupting the rsync source mid-transfer.
#   2. Isolated build dir + atomic publish — hugo writes to a temp dir, then the
#      local public/ is swapped in with a single rename. The rsync source can
#      never be observed half-written.
#   3. rsync failure is NO LONGER swallowed — exit code now reflects reality.
#   4. Post-sync verification via rsync dry-run; drift is a hard failure.
set -euo pipefail

# Paths are env-overridable so the deploy logic can be exercised in isolation
# (see references/deploy-run-verification-2026-10-30.md).
SITE_DIR="${GI_SITE_DIR:-/root/goodinfo-site}"
REMOTE="${GI_REMOTE:-root@46.225.168.78}"
REMOTE_PORT="${GI_REMOTE_PORT:-16651}"
REMOTE_DIR="${GI_REMOTE_DIR:-/www/sites/goodinfo.net}"
KEY="${GI_KEY:-/root/.ssh/id_rsa_hermes_migration}"
LOG="${GI_LOG:-/var/log/goodinfo-deploy.log}"
LOCKFILE="${GI_LOCKFILE:-/var/lock/goodinfo-deploy.lock}"
CONTAINER="${GI_CONTAINER:-1Panel-openresty-Kb76}"
LOCK_WAIT="${GI_LOCK_WAIT:-900}"

log() { echo "[$(date)] $*" >> "$LOG"; }

# ---------------------------------------------------------------- locking ----
# Prevent concurrent runs from writing the same build/rsync target.
exec 9>"$LOCKFILE"
if ! flock -n 9; then
    log "Another deploy holds the lock; waiting (max ${LOCK_WAIT}s)."
    if ! flock -w "$LOCK_WAIT" 9; then
        log "FATAL: timeout waiting for deploy lock; aborting."
        exit 1
    fi
fi
log "Acquired deploy lock."

BUILD_DIR=""
# NOTE: must use the `if` form, not `[ -n "$X" ] && rm ...`. The latter returns 1
# when X is empty, and under `set -e` that becomes the script's exit status —
# the deploy would report failure even though everything succeeded.
cleanup() {
    if [ -n "$BUILD_DIR" ]; then
        rm -rf "$BUILD_DIR"
    fi
    return 0
}
trap cleanup EXIT

cd "$SITE_DIR"

# ------------------------------------------------------------------ build ---
# Build into an isolated directory (same filesystem as public/ for atomic swap).
BUILD_DIR="$(mktemp -d "$(dirname "$SITE_DIR")/.gi-build-XXXXXX")"
log "Starting build & deploy... (build dir: $BUILD_DIR)"

hugo --minify --destination "$BUILD_DIR" --cleanDestinationDir >> "$LOG" 2>&1

# Fix Hugo multilingual root index.html (often empty)
if [ ! -s "$BUILD_DIR/index.html" ] && [ -s "$BUILD_DIR/zh/index.html" ]; then
    cp "$BUILD_DIR/zh/index.html" "$BUILD_DIR/index.html"
    log "Patched empty root index.html from zh/"
fi

log "Build successful."

# ------------------------------------------------------------------ deploy ---
# CRITICAL (2026-11-02 fix): rsync must read from the ISOLATED build dir, never
# from public/.
#
# Root cause of the 2026-11-02 08:00 failure (rsync code 23):
#   The sibling cron "GoodInfo GitHub Trending" (schedule 0 */4 * * *) fires at
#   08:00 too and runs `cd /root/goodinfo-site && hugo --minify`, which writes
#   DIRECTLY into public/. Our rsync was reading public/ as its source, so the
#   sibling rewrote files underneath the transfer mid-flight:
#     rsync: [sender] read errors mapping
#     "/root/goodinfo-site/public/tags/地震/index.xml": No data available (61)
#     rsync error: some files/attrs were not transferred (code 23)
#
# flock only serialises deploy.sh runs against each other — it cannot stop an
# unrelated process from mutating the rsync source. BUILD_DIR is created by
# mktemp and is referenced by nothing else, so it is effectively immutable.
# We therefore sync FROM BUILD_DIR, and only publish it to public/ afterwards.
#
# NOTE: no `|| true` — a failed rsync must fail the deploy.
rsync -avz --delete --exclude='ssl/' --exclude='log/' --no-perms --no-owner --no-group \
    -e "ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no" \
    "$BUILD_DIR/" ${REMOTE}:${REMOTE_DIR}/ >> "$LOG" 2>&1

log "Files synced."

# ---------------------------------------------------------------- verify -----
# Dry-run comparison against the SAME immutable source: any reported difference
# means remote != local build.
DRIFT=$(rsync -ani --delete --exclude='ssl/' --exclude='log/' --no-perms --no-owner --no-group \
    -e "ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no" \
    "$BUILD_DIR/" ${REMOTE}:${REMOTE_DIR}/ 2>/dev/null | grep -vE '^\./$|^$' || true)
if [ -n "$DRIFT" ]; then
    log "FATAL: remote drift detected after sync:"
    echo "$DRIFT" >> "$LOG"
    exit 1
fi
log "Verified: remote tree matches local build exactly."

# ------------------------------------------------- atomic local publish swap ---
# Only NOW do we touch public/. The swap is a single rename so readers never
# see a torn build. `rm -rf public` guards against a sibling hugo recreating
# the directory between the two renames (which would make the second mv nest
# the build INSIDE public/ instead of replacing it).
rm -rf "$SITE_DIR/.public.old"
if [ -d "$SITE_DIR/public" ]; then
    mv "$SITE_DIR/public" "$SITE_DIR/.public.old"
fi
rm -rf "$SITE_DIR/public"
mv "$BUILD_DIR" "$SITE_DIR/public"
BUILD_DIR=""
rm -rf "$SITE_DIR/.public.old"

# ------------------------------------------------------------------- logs ----
ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no ${REMOTE} \
    "mkdir -p ${REMOTE_DIR}/log && touch ${REMOTE_DIR}/log/access.log ${REMOTE_DIR}/log/error.log" >> "$LOG" 2>&1

# ------------------------------------------------------- SSL cert management ---
CERT_EXPIRY=$(ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no ${REMOTE} \
    "openssl x509 -enddate -noout -in ${REMOTE_DIR}/ssl/fullchain.pem 2>/dev/null | cut -d= -f2" 2>/dev/null || echo "")

NEED_RENEW=true
if [ -n "$CERT_EXPIRY" ]; then
    EXPIRY_EPOCH=$(date -d "$CERT_EXPIRY" +%s 2>/dev/null || echo 0)
    NOW_EPOCH=$(date +%s)
    DAYS_LEFT=$(( (EXPIRY_EPOCH - NOW_EPOCH) / 86400 ))
    if [ "$DAYS_LEFT" -gt 30 ]; then
        NEED_RENEW=false
        log "SSL cert valid for ${DAYS_LEFT} more days, skipping renewal."
    else
        log "SSL cert expires in ${DAYS_LEFT} days, renewing..."
    fi
else
    log "SSL certificate missing, issuing new one..."
fi

if [ "$NEED_RENEW" = true ]; then
    # Use acme.sh on remote to issue/renew via Let's Encrypt HTTP-01
    ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no ${REMOTE} bash -s -- "$REMOTE_DIR" "$CONTAINER" << 'REMOTE_EOF' >> "$LOG" 2>&1
        set -e
        REMOTE_DIR="$1"
        CONTAINER="$2"
        CONF_BACKUP="/tmp/goodinfo.net.conf.bak"
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
    log "SSL cert renewed via acme.sh."
fi

# Reload Nginx (final, in case cert was already valid)
ssh -i $KEY -p $REMOTE_PORT -o StrictHostKeyChecking=no ${REMOTE} "docker exec $CONTAINER nginx -s reload" >> "$LOG" 2>&1

log "Deploy complete."
