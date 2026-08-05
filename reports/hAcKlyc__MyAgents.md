# hAcKlyc/MyAgents 分析报告

- 仓库：[hAcKlyc/MyAgents](https://github.com/hAcKlyc/MyAgents)
- 方向：开源桌面端个人 Agent 工作台（本地优先、任务系统、开放运行环境）
- 主要语言：TypeScript（Tauri v2 + React 19）
- 指标：⭐ 787 · License AGPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[myagents.io](https://myagents.io) · [架构文档](https://github.com/hAcKlyc/MyAgents/blob/main/specs/ARCHITECTURE.md)

> 分析基于 2026-08-06 抓取的 README、bundled-agents/skills 与架构文档。

## 这是什么（非技术版）

- **这是什么**：一个"住在电脑里的个人 AI 工作台"。对话、工作区文件、终端、浏览器、任务、模型、记忆都在一个桌面窗口里；想法能沉淀成任务、任务可周期调度、执行可追踪复盘。
- **能拿来干什么**：日常 AI 工作流一体化；周期任务自动化；多模型/工具/MCP 统一管理。
- **适合谁**：开发者、需要"桌面级任务系统"的 AI 重度用户。
- **快速判断**：如果你想要"不只是聊天框"的本地 Agent 工作台，它很合适；如果偶尔用 AI，功能过剩。

## 分类

- 主分类：1. 通用 Agent 桌面 / 客户端 / Runtime
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述"开源桌面端个人 Agent 工作台……本地优先的 Agent 桌面客户端 + 可持续工作的任务系统 + 开放的 AI 运行环境"。

## 项目方向与定位

把对话、工作区、文件、工具、模型、任务和长期记忆放进同一桌面系统。三大块：本地优先客户端（多标签/文件树/内嵌终端/内嵌浏览器/本地全文搜索）、任务系统（想法→任务→周期调度→追踪复盘）、开放运行环境（多模型供应商、MCP、Skills、自定义 Agent、IM Bot、插件、外部 Runtime）。

## 主要功能（能做什么）

- 桌面多标签工作区、文件树、内嵌终端与浏览器、历史会话、本地全文搜索
- 任务沉淀/周期调度/状态追踪复盘
- 多模型、MCP、Skills、自定义 Agent、IM Bot、插件
- macOS/Windows 构建脚本、bundled agents/skills 内置

## 架构设计

```text
bundled-agents/ bundled-skills/  内置 Agent 与技能
specs/ARCHITECTURE.md            架构文档
（Tauri v2 + React 19 桌面端）
```

## 实现思路与核心逻辑

- 以"桌面工作区"为容器整合 Agent 能力，降低工具切换成本
- 任务系统把"想法"变成可调度、可复盘的执行单元
- 开放运行时：外部 Runtime/IM Bot/插件可扩展

## 亮点

- 786 stars，个人 Agent 工作台赛道活跃项目
- 功能完整（终端/浏览器/任务/搜索/MCP/Skills），一体化程度高

## 局限与风险（可选）

- **AGPL-3.0**：派生分发需遵守 copyleft
- 功能多，稳定性与学习成本需观察

## 分析说明

基于 README、bundled-agents/skills 与架构文档；未运行应用。
