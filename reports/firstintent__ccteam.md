# firstintent/ccteam 分析报告

- 仓库：[firstintent/ccteam](https://github.com/firstintent/ccteam)
- 方向：把已有 coding agents（Claude Code/Codex/Grok/Kimi）变成一队
- 主要语言：Rust
- 指标：⭐ 112 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/firstintent/ccteam)

> 分析基于 2026-08-06 抓取的 README、crates/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"AI 团队调度器"。你现有的 Claude Code、Codex、Grok、Kimi 各自擅长不同的活，它把它们组成一队：任何会话可以派活、跨机器收集结果，你通过 Telegram、飞书或浏览器遥控。
- **能拿来干什么**：多 Agent 分工（Claude 规划、Codex 长跑、Grok 快速回答、Kimi 便宜批量）。
- **适合谁**：多 Agent 用户、想远程遥控 AI 团队的人。
- **快速判断**：如果你有多个 coding agent 想组合使用，它很合适；否则不需要。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "turns the coding agents you already run... into one team — any session can spawn, dispatch, and collect work from any vendor on any machine"。

## 项目方向与定位

让"各自孤岛"的 coding CLI 组成团队：Claude Code 规划最深、Codex 长跑稳、Grok 最快、Kimi 便宜批量；跨机器派发与收集；Telegram/Lark/浏览器控制。

## 主要功能（能做什么）

- 多 vendor coding agent 团队化
- 会话派发/收集、跨机器
- Telegram/Lark/浏览器遥控
- macOS/Linux/WSL

## 架构设计

```text
crates/       Rust 核心
docs/ INSTALL.md
```

## 实现思路与核心逻辑

- 以"现有 CLI"为执行体，Rust 做编排与控制层
- 远程通道（IM/浏览器）作为操作面
- 按各 agent 优势路由任务

## 亮点

- 112 stars，多 Agent 组合定位与帖子主题契合
- 跨机器 + IM 遥控能力完整
- MIT 开源

## 局限与风险（可选）

- 依赖各 CLI agent 安装与配置
- 生态较新

## 分析说明

基于 README、crates/ 与文档；未运行。
