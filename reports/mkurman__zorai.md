# mkurman/zorai 分析报告

- 仓库：[mkurman/zorai](https://github.com/mkurman/zorai)
- 方向：全自主 daemon 运行时——持久、多 Agent、可审计、会学习
- 主要语言：Rust
- 指标：⭐ 321 · License MIT · 最近推送 2026-08-03
- 主页/文档：[docs.zorai.app](https://docs.zorai.app) · [zorai.app](https://zorai.app)

> 分析基于 2026-08-06 抓取的 README、crates/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"常驻后台的 AI 工作引擎"。工作、记忆、审批、工具和长期目标都住在 daemon 里，关掉界面任务照跑；Electron、TUI、CLI、MCP、聊天网关都连到同一个 daemon。
- **能拿来干什么**：长跑 Agent 任务、可审批的工具执行、跨界面恢复工作。
- **适合谁**：开发者、需要"关了 UI 任务也不断"的 Agent 用户。
- **快速判断**：如果你要"持久 daemon + 多 Agent + 审批"的执行平台，它很对口；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（daemon 运行时）
- 副分类：3. 多 Agent 编排 / 协作系统
- 理由：README 自述 "Fully agentic daemon runtime for durable AI work... the daemon owns work, memory, approvals, tools, and long-running goals"。

## 项目方向与定位

持久多 Agent 执行平台：daemon 拥有工作/记忆/审批/工具/长期目标；运行时可规划工作、跑工具、派生有界子 Agent、暂停等待审批、随时间学习。所有前端（Electron/TUI/CLI/MCP/聊天网关）都是同一 daemon 的客户端。

## 主要功能（能做什么）

- daemon 持久化工作/记忆/审批/工具/长期目标
- 多端重连同一状态（UI 关了任务照跑）
- 内建运行时：规划、工具、有界子 Agent、审批暂停、学习
- 记忆、workspace boards、执行队列、操作历史持久化

## 架构设计

```text
crates/        Rust 核心
frontend/      桌面/UI
npm-package/ plugins/ docs/
```

## 实现思路与核心逻辑

- daemon 即真相：状态驻留 daemon，前端只是投影
- 有界子 Agent + 审批暂停：可控的自主性
- 学习机制：随时间改进行为

## 亮点

- 321 stars，"daemon 拥有工作"理念与"持久可恢复"赛道一致
- Rust 实现，多端统一状态架构清晰
- MIT 开源

## 局限与风险（可选）

- 概念较重，上手成本不低
- 与 Maka/synergy 等"可恢复工作区"竞争

## 分析说明

基于 README、crates/ 与文档；未运行 daemon。
