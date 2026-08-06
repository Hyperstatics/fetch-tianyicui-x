# zhoudongliang-lut/agent-runtime 分析报告

- 仓库：[zhoudongliang-lut/agent-runtime](https://github.com/zhoudongliang-lut/agent-runtime)
- 方向：轻量 Agent 运行平台（基于 Claude Agent SDK）
- 主要语言：Python
- 指标：⭐ 1 · License 未见 LICENSE 文件（需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/zhoudongliang-lut/agent-runtime)

> 分析基于 2026-08-06 抓取的 docs/architecture 与目录结构。⚠️ 未见 LICENSE 文件（README API 404，从克隆文档分析）。

## 这是什么（非技术版）

- **这是什么**：一个轻量 Agent 运行平台，基于 Claude Agent SDK：总依赖约 65MB（对比 OpenClaw 1.4GB）、4 层防御架构、单进程部署、REST API + Web UI、混合 Skill 模式（内置 + 第三方进程隔离）。
- **能拿来干什么**：自用/小团队的 Agent 服务。
- **适合谁**：开发者、小团队。
- **快速判断**：如果你要"轻量 + 安全"的 Agent 运行时，它很对口；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（轻量运行时）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：docs 自述"轻量级 Agent 运行平台，基于 Claude Agent SDK，支持部署和扩展不同的 Skill 技能"。

## 项目方向与定位

轻量（65MB）、安全（4 层防御）、简单（单进程）、灵活（混合 Skill）。

## 主要功能（能做什么）

- REST API + Web UI
- Skill 部署（内置 + 进程隔离）
- 4 层防御

## 架构设计

```text
src/agent_runtime + skills/ + web-ui/
docs/architecture.md
```

## 实现思路与核心逻辑

- 轻量 vs OpenClaw、防御 vs CVE

## 亮点

- 1 stars，轻量安全定位
- 架构文档完善

## 局限与风险（可选）

- **未见 LICENSE 文件**（列入本地 backlog）
- 依赖 Claude CLI

## 分析说明

基于 docs/architecture 与目录结构；未运行。
