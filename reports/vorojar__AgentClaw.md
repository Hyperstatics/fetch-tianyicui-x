# vorojar/AgentClaw 分析报告

- 仓库：[vorojar/AgentClaw](https://github.com/vorojar/AgentClaw)
- 方向：24/7 AI 指挥官 + Agent 托管平台（Hive）
- 主要语言：TypeScript
- 指标：⭐ 29 · License README 标 MIT（仓库未见 LICENSE 文件，需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/vorojar/AgentClaw)

> 分析基于 2026-08-06 抓取的 README、data/ 与文档。⚠️ 未见 LICENSE 文件。

## 这是什么（非技术版）

- **这是什么**：一个"AI 指挥官"。它自己不写代码、不搜索，而是理解你的意图、规划任务、调度合适的工具/技能，并通过 Web UI / Telegram / WhatsApp / 钉钉 / 飞书 / QQ 全天候待命。Hive 模式下还能托管你发布的独立 Agent。
- **能拿来干什么**：个人 AI 调度中枢；给他人发布/托管 Agent。
- **适合谁**：重度 AI 用户、想托管 Agent 给团队/用户的人。
- **快速判断**：如果你要"一个入口调度所有 AI 能力"，它很对口；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（调度中心/托管平台）
- 副分类：3. 多 Agent 编排 / 协作系统
- 理由：README 自述"指挥官级别的个人 AI 助理，同时也是一个 Agent 托管平台（Hive）"。

## 项目方向与定位

理解意图、规划任务、调度工具/技能；多 IM 渠道待命；Hive 模式下每个 Agent 独立记忆空间、工具白名单、技能黑名单、知识库与 API Key。

## 主要功能（能做什么）

- 意图理解与任务规划调度
- Web UI / Telegram / WhatsApp / 钉钉 / 飞书 / QQ 渠道
- Hive Agent 托管（Soul/Tools/知识/Key）

## 架构设计

```text
data/ docker-compose.yml / Dockerfile
（调度核心 + 渠道适配 + Hive）
```

## 实现思路与核心逻辑

- "能力归 Agent、编排归我"：指挥调度而非重复造轮子
- 托管隔离：每个 Agent 独立权限/记忆/知识

## 亮点

- 29 stars，多渠道 + 托管平台组合完整
- 中文社区

## 局限与风险（可选）

- **未见 LICENSE 文件**（列入本地 backlog）
- 功能面大，稳定性待验证

## 分析说明

基于 README、data/ 与文档；未运行。
