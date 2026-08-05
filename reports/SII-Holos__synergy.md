# SII-Holos/synergy 分析报告

- 仓库：[SII-Holos/synergy](https://github.com/SII-Holos/synergy)
- 方向：持久、可恢复的 AI Agent 工作区（会话/代理/文件/浏览器/工具一体）
- 主要语言：TypeScript
- 指标：⭐ 540 · License MIT · 最近推送 2026-08-03
- 主页/文档：[synergy.holosai.io](https://synergy.holosai.io)

> 分析基于 2026-08-06 抓取的 README、packages/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"不断电的 AI 工作区"。会话、代理、文件、浏览器、工具和自动化连在一个运行时里，中断后能恢复，适合软件与知识工作。
- **能拿来干什么**：把 AI 干活的过程持久化；跨会话继续工作。
- **适合谁**：开发者、需要可恢复 Agent 工作区的团队。
- **快速判断**：如果你受够了"AI 会话断了就重来"，它值得关注；否则普通客户端即可。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（可恢复工作区）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "Persistent, recoverable AI agent work... keeps sessions, agents, files, Browser, tools, and automation connected in one runtime"。

## 项目方向与定位

以"持久、可恢复"为核心的开源工作区：软件与知识工作的统一运行时，会话/代理/文件/浏览器/工具/自动化互联。MIT 开源、CI 完善。

## 主要功能（能做什么）

- 会话、Agent、文件、浏览器、工具、自动化一体
- 可恢复运行（persistent/recoverable）
- install 脚本、ECOSYSTEM 生态文档

## 架构设计

```text
packages/    多包（ui/核心等）
install/ docs/
```

## 实现思路与核心逻辑

- 单一运行时连接所有工作对象，避免工具割裂
- 以"可恢复"为第一性设计（会话/任务状态持久化）

## 亮点

- "持久可恢复"定位直接回应 Agent 会话易失痛点
- MIT 开源，工程规范完整

## 局限与风险（可选）

- 项目较新，成熟度待验证
- 与 Kun/Maka 等"可恢复工作区"同赛道

## 分析说明

基于 README、packages/ 与文档；未运行。
