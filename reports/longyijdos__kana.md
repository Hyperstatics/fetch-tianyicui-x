# longyijdos/kana 分析报告

- 仓库：[longyijdos/kana](https://github.com/longyijdos/kana)
- 方向：手搓的 Agent 运行时（4 个直接运行时依赖）
- 主要语言：TypeScript
- 指标：⭐ 3 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/longyijdos/kana)

> 分析基于 2026-08-06 抓取的 README、evals/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"不靠 SDK 胶水"的 Agent 运行时。只有 4 个直接运行时依赖，Agent loop、TUI、MCP/OAuth、Provider 流式适配和会话系统全部手搓。
- **能拿来干什么**：学习/构建精简 Agent。
- **适合谁**：想"手搓 Agent"的开发者。
- **快速判断**：如果你喜欢极简可控的实现，它值得看；否则成熟框架更省事。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（手搓运行时）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述"不是又一层 SDK 胶水：4 个直接运行时依赖，核心链路全部手搓"。

## 项目方向与定位

精简 Agent 运行时：手搓 Agent loop/TUI/MCP/OAuth/provider 流式/会话；evals 配套。

## 主要功能（能做什么）

- Agent loop、TUI
- MCP/OAuth、Provider 流式适配、会话系统
- evals

## 架构设计

```text
evals/ docs/ assets/
```

## 实现思路与核心逻辑

- 最小依赖：核心链路自研

## 亮点

- 3 stars，极简理念
- MIT 开源

## 局限与风险（可选）

- 生态较新
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、evals/ 与文档；未运行。
