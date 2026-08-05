# liaocaoxuezhe/FigmaX 分析报告

- 仓库：[liaocaoxuezhe/FigmaX](https://github.com/liaocaoxuezhe/FigmaX)
- 方向：跨 AI 客户端的 Skill——聊天让 Agent 在 Figma 画稿
- 主要语言：JavaScript
- 指标：⭐ 6 · License 未见 LICENSE 文件（需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/liaocaoxuezhe/FigmaX)

> 分析基于 2026-08-06 抓取的 README、figma_editor/ 与文档。⚠️ 未见 LICENSE 文件。

## 这是什么（非技术版）

- **这是什么**：一个"让 AI 在 Figma 里画图"的技能包。在 Claude Code/Cursor/Codex 里聊设计需求，AI 直接在 Figma 画布上画稿、改稿、出图；依赖 Figma 官方 MCP（读）和 figma_editor MCP（写）。
- **能拿来干什么**：AI 辅助 UI 设计、设计稿快速迭代。
- **适合谁**：设计师、开发者。
- **快速判断**：如果你想让"AI 直接改 Figma"，它很有价值；否则不需要。

## 分类

- 主分类：6. 特定领域 / 其他（设计工具 Skill）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述"在 Claude Code/Cursor/Codex 里聊天，让 Agent 直接在你的 Figma 画布上画稿、改稿、出图"。

## 项目方向与定位

跨 AI 客户端 Skill：Figma 官方 MCP（读：解析 URL/截图/设计令牌）+ figma_editor MCP（写：建节点/自动布局/变量/组件/导出）。

## 主要功能（能做什么）

- 聊天→Figma 画稿/改稿/出图
- 读写双 MCP
- 多客户端（Claude Code/Cursor/Codex）

## 架构设计

```text
figma_editor/  MCP 服务
commands/ assets/
```

## 实现思路与核心逻辑

- 读写分离：官方 MCP 读、自研 editor MCP 写
- 工作流可分发/可复用/可定制

## 亮点

- 6 stars，AI×Figma 垂直 Skill
- 中文社区

## 局限与风险（可选）

- **未见 LICENSE 文件**（列入本地 backlog）
- 依赖两个 MCP 服务

## 分析说明

基于 README、figma_editor/ 与文档；未运行。
