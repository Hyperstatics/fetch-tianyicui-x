# solo-agent/solo 分析报告

- 仓库：[solo-agent/solo](https://github.com/solo-agent/solo)
- 方向：本地优先的人机协同工作区（渠道/线程对话/任务板/团队）
- 主要语言：Go（后端）+ TypeScript（前端）
- 指标：⭐ 562 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/solo-agent/solo)

> 分析基于 2026-08-06 抓取的 README、cmd/frontend 结构与文档。

## 这是什么（非技术版）

- **这是什么**：一个"人和 AI 一起办公的工作区"。通过渠道、线程对话、任务板和按渠道划分的团队，协调多个 AI 编码 Agent（Claude Code/Codex/OpenCode/Hermes/OpenClaw）一起干活，数据本地优先。
- **能拿来干什么**：多 Agent 协作、团队任务管理、本地部署的 AI 工作区。
- **适合谁**：开发者、小型团队、想自托管 AI 协作平台的人。
- **快速判断**：如果你要"本地优先的多 Agent 协作工作区"，它很合适；否则不需要。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：1. 通用 Agent Runtime / Harness（工作区运行时）
- 理由：README 自述 "Local-first workspace for humans and AI coding agents. Coordinate multiple agents through channels, threaded conversations, task boards, and channel-scoped teams."。

## 项目方向与定位

本地优先的人机协同：渠道 + 线程对话 + 任务板 + channel 团队，协调多个 AI 编码 Agent。Go 后端 + Node 前端，Docker 部署。

## 主要功能（能做什么）

- 多 Agent 接入（Claude Code/Codex/OpenCode/Hermes/OpenClaw）
- 渠道、线程对话、任务板、channel 团队
- 本地优先、Docker 部署

## 架构设计

```text
cmd/       Go 后端入口
frontend/  前端
docker-compose.yml / Dockerfile
```

## 实现思路与核心逻辑

- "工作区即协作层"：Agent 通过渠道/任务板协作，人在其中审查
- 本地优先：数据自托管
- 多 Agent 兼容：不绑定单一 CLI

## 亮点

- 562 stars，与 Orkas/Commonly 同赛道但更轻
- Go 后端性能与部署友好，MIT 开源
- 中英双语文档

## 局限与风险（可选）

- 与同类"多 Agent 工作区"竞争激烈
- 生态与成熟案例待积累

## 分析说明

基于 README、cmd/frontend 结构与文档；未运行。
