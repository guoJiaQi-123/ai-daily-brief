# AI行业咨询与每日晨报仓库

## 📁 目录结构
```
ai-daily-brief/
├── daily-briefs/          # 每日晨报，按年月分类
│   └── 2026/
│       └── 06/
│           └── 2026-06-04.md
├── ai-consulting/         # AI行业深度咨询文档
├── templates/             # 文档模板
│   └── daily_brief_template.md
├── scripts/               # 自动化脚本
│   ├── generate_daily_brief.py  # 晨报生成脚本
│   └── auto_commit.sh           # 自动提交脚本
├── .gitignore
└── README.md
```

## 🚀 使用说明

### 生成每日晨报
```bash
# 生成当天的晨报（自动取最近24小时的新闻）
python scripts/generate_daily_brief.py
```

### 手动提交变更
```bash
# 提交所有变更并推送到GitHub
./scripts/auto_commit.sh "自定义提交备注"
```

## ⏰ 自动化规则
- 晨报生成时间：每天上午9点自动执行
- 新闻范围：严格筛选最近24小时内的AI行业动态
- 自动提交：晨报生成后自动推送到GitHub仓库

## 📌 内容范围
- 🔴 重磅新闻：大模型发布、大额融资、重大政策
- 🤖 技术突破：AI技术进展、新模型发布
- 📊 行业动态：AI行业趋势、市场数据
- 🏢 企业动态：科技公司AI相关动作

---
*本仓库由小虾助手自动维护，每日更新AI行业最新动态*
