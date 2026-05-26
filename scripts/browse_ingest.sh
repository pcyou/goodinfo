#!/bin/bash
# browse_ingest.sh - 将 browse.sh 技能"蒸馏"为 Hermes 智库条目
# 用法: ./browse_ingest.sh <repo_url>

SKILL_URL=$1
if [ -z "$SKILL_URL" ]; then
    echo "用法: ./browse_ingest.sh <SKILL_MD_URL>"
    echo "示例: ./browse_ingest.sh https://raw.githubusercontent.com/browserbase/browse.sh/main/skills/trainline.com/find-trains/SKILL.md"
    exit 1
fi

# 1. 提取主机名和技能名
HOSTNAME=$(echo "$SKILL_URL" | grep -oP 'skills/\K[^/]+')
SLUG=$(echo "$SKILL_URL" | grep -oP 'skills/[^/]+/\K[^/]+')
SKILL_NAME="browse-sh-${HOSTNAME}"

# 2. 创建目录
SKILL_DIR="/root/.hermes/skills/devops/${SKILL_NAME}"
mkdir -p "$SKILL_DIR"

echo "📥 正在下载技能: $HOSTNAME -> $SKILL_DIR"

# 3. 下载原始文件
curl -sL "$SKILL_URL" -o "$SKILL_DIR/raw_reference.md"

# 4. 生成 Hermes 技能模板
cat > "$SKILL_DIR/SKILL.md" << EOF
---
name: ${SKILL_NAME}
category: devops
description: |
  源自 Browse.sh 的 ${HOSTNAME} 操作指南 (已蒸馏为 Hermes 智库模式)。
  包含 API 端点、选择器和反爬策略。
tags:
  - browse-sh
  - ${HOSTNAME}
---

# ${HOSTNAME} 操作指南 (Think Tank Mode)

## 🧠 核心情报 (Intelligence)
*(请阅读 raw_reference.md 并在此处提炼关键信息，如 API、URL 模式等)*

## 🛠️ Hermes 执行步骤
1. ...
2. ...

## ⚠️ 避坑指南
- ...
EOF

echo "✅ 技能已生成: $SKILL_DIR/SKILL.md"
echo "👉 下一步：请人工审阅 raw_reference.md 并填充 SKILL.md 中的核心情报。"
