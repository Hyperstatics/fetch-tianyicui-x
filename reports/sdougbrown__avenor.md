# sdougbrown/avenor 分析报告

- 仓库：[sdougbrown/avenor](https://github.com/sdougbrown/avenor)
- 方向：突破单层 sub-agent 限制的多级编排（jockey/horse）
- 主要语言：Go + TypeScript
- 指标：⭐ 0 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/sdougbrown/avenor)

> 分析基于 2026-08-06 抓取的 README、cmd/、docs/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个让顶层 Agent 能启动完全独立进程的编排器，子 Agent 可以再调子 Agent（多级）。支持 8 个后端（opencode/codex/gemini/cursor/pi 等）；作者用"jockey（骑手，只读）→ horse/mule（写）"模式防止实现 Agent 乱做。
- **能拿来干什么**：多级 Agent 编排、写读分离模式。
- **适合谁**：多 Agent 开发者。
- **快速判断**：如果你要"子 Agent 也能有子 Agent"，它很对口；否则不需要。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "allows any given top-level agent to kick off an entirely separate process that is no longer bound by the single-level sub-agent restriction. Now your sub-agents can call sub-agents"。

## 项目方向与定位

多级编排：jockey 只读派活、horse/mule 写执行；8 后端；MCP server（avenor mcp）。

## 主要功能（能做什么）

- 多级 sub-agent 编排
- 8 个后端、MCP server
- 模板包（dispatch 矩阵）

## 架构设计

```text
cmd/ client/ templates/ docs/
```

## 实现思路与核心逻辑

- "让马跑起来"：解除单层限制
- jockey/horse 写读分离防混淆

## 亮点

- 0 stars，多级编排理念
- 与帖子"多 Agent"主题契合
- MIT 开源

## 局限与风险（可选）

- 生态较新
- 编排复杂度高

## 分析说明

基于 README、cmd/docs 与文档；未运行。
