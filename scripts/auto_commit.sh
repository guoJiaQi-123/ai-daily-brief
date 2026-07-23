#!/bin/bash
# AI晨报自动提交脚本
# 用法：./scripts/auto_commit.sh "提交备注"

set -e

# 进入仓库目录
cd "$(dirname "$0")/.."

# 检查是否有变更
if git status --porcelain | grep -q .; then
    # 添加所有变更
    git add .
    
    # 提交，默认备注是当日日期，支持自定义
    COMMIT_MSG="${1:-📰 AI晨报更新 $(date +%Y-%m-%d)}"
    git commit -m "$COMMIT_MSG"
    
    # 推送到main分支
    git push origin main
    
    echo "✅ 提交成功！备注：$COMMIT_MSG"
else
    echo "ℹ️ 没有需要提交的变更"
fi
