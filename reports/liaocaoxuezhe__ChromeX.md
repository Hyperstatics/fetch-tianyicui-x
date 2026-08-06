# liaocaoxuezhe/ChromeX 分析报告

- 仓库：[liaocaoxuezhe/ChromeX](https://github.com/liaocaoxuezhe/ChromeX)
- 方向：Link2Chrome——本地 Agent 连接真实浏览器（MCP）
- 主要语言：JavaScript（Chrome 扩展 + Node）
- 指标：⭐ 1 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/liaocaoxuezhe/ChromeX)

> 分析基于 2026-08-06 抓取的 README、extension/ 与文档。

## 这是什么（非技术版）

- **这是什么**：Link2Chrome——本地优先的浏览器自动化项目。通过 Chrome 扩展、WebSocket 和 MCP Server 把本地 Agent 与真实浏览器连接：导航、点击/输入/滚动、读 DOM、截图、跑 Playwright 风格脚本、管理多任务 Session（标签组）。
- **能拿来干什么**：让 Agent 操作真实浏览器。
- **适合谁**：开发者、浏览器 Agent 用户。
- **快速判断**：如果你要"Agent 用我的浏览器干活"，它很实用；否则不需要。

## 分类

- 主分类：6. 特定领域 / 其他（浏览器自动化 MCP）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述"通过 Chrome 扩展、WebSocket 和 MCP Server 将本地 Agent 与真实浏览器连接"。

## 项目方向与定位

本地浏览器自动化：MCP Server（26 工具）+ Chrome 扩展（Manifest V3，chrome.debugger/CDP）+ 多任务 Session。

## 主要功能（能做什么）

- 26 个统一浏览器工具（MCP stdio）
- Chrome 扩展 + CDP、alarms keepalive
- 多任务 Session（标签组）

## 架构设计

```text
extension/        Chrome 扩展
（MCP Server + WebSocket）
```

## 实现思路与核心逻辑

- 扩展驱动 CDP、MCP 暴露给 Agent

## 亮点

- 1 stars，浏览器 MCP 工具
- 多任务 Session 设计
- MIT 开源

## 局限与风险（可选）

- 与 mcp-chrome 等竞争
- 依赖 Chrome 扩展环境

## 分析说明

基于 README、extension/ 与文档；未运行。
