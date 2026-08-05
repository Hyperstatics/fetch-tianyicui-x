# geminixiang/mikan 分析报告

- 仓库：[geminixiang/mikan](https://github.com/geminixiang/mikan)
- 方向：多平台 AI coding agent（Slack/Telegram/Discord/GitHub）
- 主要语言：TypeScript
- 指标：⭐ 7 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/geminixiang/mikan)

> 分析基于 2026-08-06 抓取的 README、ARCHITECTURE.md 与文档。⚠️ pre-1.0，配置/数据格式可能变化。

## 这是什么（非技术版）

- **这是什么**：一个多平台 AI 编程助手。通过 Slack、Telegram、Discord、GitHub 就能调用；对话级工作区 + 沙箱执行。
- **能拿来干什么**：在 IM 里遥控 AI 编程。
- **适合谁**：团队、多 IM 用户。
- **快速判断**：如果你想"在群里让 AI 干活"，它很对口；否则不需要。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "A multi-platform AI coding agent for Slack, Telegram, Discord, and GitHub"。

## 项目方向与定位

多平台 coding agent：conversation-scoped workspaces + sandbox execution（mikan office）；pre-1.0。

## 主要功能（能做什么）

- Slack/Telegram/Discord/GitHub 接入
- 会话级工作区、沙箱执行

## 架构设计

```text
architecture.toml / ARCHITECTURE.md
src/content/docs/
```

## 实现思路与核心逻辑

- 会话即工作区：按对话隔离上下文
- 沙箱执行保证安全

## 亮点

- 7 stars，IM 遥控 AI 编程
- 架构文档（office/architecture）完整
- MIT 开源

## 局限与风险（可选）

- pre-1.0，升级可能需重置状态
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、ARCHITECTURE.md 与文档；未运行。
