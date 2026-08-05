# Sma1lboy/kobe 分析报告

- 仓库：[Sma1lboy/kobe](https://github.com/Sma1lboy/kobe)
- 方向：agent multiplexer——像终端分屏一样并行跑多个 Agent
- 主要语言：TypeScript
- 指标：⭐ 93 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/Sma1lboy/kobe)

> 分析基于 2026-08-06 抓取的 README、src/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"AI 分屏器"。像终端开多个标签页一样并行跑 Claude Code、Codex、Copilot，每个会话独立 git worktree 和分支；可以断开再连回，它们会继续干活。
- **能拿来干什么**：多个 AI 同时并行处理不同任务。
- **适合谁**：重度 AI 编程用户、多任务开发者。
- **快速判断**：如果你想让"多个 AI 同时干活"，它很实用；否则不需要。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "an open-source agent multiplexer: it runs Claude Code, Codex, and Copilot in parallel, each session on its own git worktree and branch"。

## 项目方向与定位

把"终端分屏"体验带给 Agent：并行会话、独立 worktree/branch、detach/reattach 继续工作。npm 分发（@sma1lboy/kobe）。

## 主要功能（能做什么）

- 并行运行多 Agent（Claude Code/Codex/Copilot）
- 每会话独立 worktree/branch
- attach/detach/reattach
- 工作区（任务侧栏/嵌入式会话/文件树/终端）

## 架构设计

```text
src/          核心
docs/ assets/
```

## 实现思路与核心逻辑

- worktree 隔离：并行会话互不污染
- 会话持久：断开后继续，可重新连接

## 亮点

- 93 stars，多 Agent 并行实用工具
- npm 分发 + 工作区 UI
- MIT 开源

## 局限与风险（可选）

- 依赖各 CLI agent
- 与 ccteam/hive 等"多 Agent 编排"工具竞争

## 分析说明

基于 README、src/ 与文档；未运行。
