#!/usr/bin/env python3
"""
AI每日晨报生成脚本
功能：搜索最近24小时的AI行业新闻，生成标准化晨报并自动提交到仓库
"""

import requests
import json
from datetime import datetime, timedelta
import os
import sys

# 配置
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAILY_BRIEF_DIR = os.path.join(REPO_DIR, "daily-briefs")
TEMPLATE_PATH = os.path.join(REPO_DIR, "templates", "daily_brief_template.md")

# 时间范围：最近24小时
END_TIME = datetime.now()
START_TIME = END_TIME - timedelta(hours=24)
DATE_STR = END_TIME.strftime("%Y-%m-%d")
TIME_STR = END_TIME.strftime("%H:%M")

def search_ai_news():
    """搜索最近24小时的AI行业新闻"""
    # 搜索关键词组合
    keywords = [
        "AI 大模型 最新 2026",
        "人工智能 行业动态 24小时",
        "大模型 融资 发布 2026",
        "AI 政策 法规 最新",
        "OpenAI DeepSeek 字节 腾讯 AI"
    ]
    
    all_news = []
    
    for keyword in keywords:
        try:
            # 使用通用搜索API
            url = "https://api.coze.cn/open_api/v1/chat/completions"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {os.getenv('COZE_TOKEN', '')}"
            }
            
            # 这里使用搜索工具获取新闻，实际执行时会调用search_web
            # 临时模拟，实际执行时会通过search_web获取真实新闻
            # 实际使用时，这里会调用search_web工具获取最近24小时的新闻
            print(f"搜索关键词：{keyword}")
            
        except Exception as e:
            print(f"搜索出错：{e}")
            continue
    
    return all_news

def filter_recent_news(news_list):
    """过滤出最近24小时的新闻"""
    recent_news = []
    for news in news_list:
        # 解析新闻时间，这里需要根据实际搜索结果调整
        # 假设新闻有publish_time字段
        if 'publish_time' in news:
            try:
                news_time = datetime.fromisoformat(news['publish_time'].replace('Z', '+00:00'))
                if news_time >= START_TIME:
                    recent_news.append(news)
            except:
                # 如果时间解析失败，暂时保留，后续人工确认
                recent_news.append(news)
    return recent_news

def generate_brief_content(news_list):
    """根据新闻生成晨报内容"""
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # 替换模板变量
    content = template.replace('{{date}}', DATE_STR)
    content = content.replace('{{generate_time}}', END_TIME.strftime("%Y-%m-%d %H:%M:%S"))
    
    # 这里需要根据实际新闻分类填充内容
    # 实际使用时会将搜索到的新闻分类到不同板块
    placeholder = "- 正在获取最新新闻，请稍候..."
    content = content.replace('[新闻标题](链接) - 摘要（发布时间：{{time}}）', placeholder)
    
    return content

def save_brief(content):
    """保存晨报到对应目录"""
    year_month = END_TIME.strftime("%Y/%m")
    save_dir = os.path.join(DAILY_BRIEF_DIR, year_month)
    os.makedirs(save_dir, exist_ok=True)
    
    file_path = os.path.join(save_dir, f"{DATE_STR}.md")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 晨报已保存到：{file_path}")
    return file_path

def main():
    print(f"📅 生成 {DATE_STR} 的AI晨报，时间范围：{START_TIME.strftime('%Y-%m-%d %H:%M')} 至 {END_TIME.strftime('%Y-%m-%d %H:%M')}")
    
    # 1. 搜索新闻
    print("🔍 正在搜索最近24小时的AI新闻...")
    news_list = search_ai_news()
    
    # 2. 过滤最近24小时的新闻
    print("⏳ 正在过滤新闻...")
    recent_news = filter_recent_news(news_list)
    print(f"✅ 共找到 {len(recent_news)} 条最近24小时的新闻")
    
    # 3. 生成晨报内容
    print("✍️  正在生成晨报...")
    content = generate_brief_content(recent_news)
    
    # 4. 保存晨报
    file_path = save_brief(content)
    
    # 5. 自动提交到仓库
    print("📤 正在提交到GitHub仓库...")
    os.chdir(REPO_DIR)
    commit_msg = f"📰 AI晨报更新 {DATE_STR}"
    os.system(f"./scripts/auto_commit.sh \"{commit_msg}\"")
    
    print("🎉 晨报生成并提交完成！")
    return 0

if __name__ == "__main__":
    sys.exit(main())
