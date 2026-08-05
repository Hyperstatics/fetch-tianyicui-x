# btspoony/mstar-harness 分析报告

- 仓库：[btspoony/mstar-harness](https://github.com/btspoony/mstar-harness)
- 方向：Morning Star Code Agent Harness Framework（多客户端插件）
- 主要语言：TypeScript
- 指标：⭐ 10 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/btspoony/mstar-harness)

> 分析基于 2026-08-06 抓取的 README、agents/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"Code Agent Harness 框架"（Morning Star）。提供多客户端插件形态（Claude Code/Codex/Cursor/Kimi/OMP/ZCode），让同一套 harness 能力在多个 AI 客户端里复用。
- **能拿来干什么**：跨客户端统一 Agent 工作流。
- **适合谁**：多客户端 Agent 用户。
- **快速判断**：如果你想"一套 harness 到处用"，它很对口；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "Morning Star Code Agent Harness Framework"，多客户端插件。

## 项目方向与定位

多客户端 harness 框架：.claude-plugin/.codex-plugin/.cursor-plugin/.kimi-plugin/.omp-plugin/.zcode-plugin，一套框架多端适配。

## 主要功能（能做什么）

- 多客户端插件（claude/codex/cursor/kimi/omp/zcode）
- agents/ 编排
- CI、release

## 架构设计

```text
agents/       核心
.*-plugin/    各客户端插件
```

## 实现思路与核心逻辑

- 框架 + 适配器：同一 harness 能力，不同客户端壳

## 亮点

- 10 stars，与帖子 Harness 主题直接相关
- 多客户端兼容面广
- MIT 开源

## 局限与风险（可选）

- 项目较新
- 多端适配维护成本高

## 分析说明

基于 README、agents/ 与文档；未运行。
