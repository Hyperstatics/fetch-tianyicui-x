# yofine/Mexus 分析报告

- 仓库：[yofine/Mexus](https://github.com/yofine/Mexus)
- 方向：Multi-agent Execution Unified System——统一多 Agent 执行
- 主要语言：TypeScript
- 指标：⭐ 85 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[BLUEPRINT](https://github.com/yofine/Mexus/blob/main/BLUEPRINT.md)

> 分析基于 2026-08-06 抓取的 README、agent-team/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"多 AI 统一控制台"。把散落的 CLI AI Agent（Claude Code、OpenCode、Aider、Codex、Gemini）变成统一的本地系统：运行、看状态、审查它们的工作，从一个操作台管理。
- **能拿来干什么**：多 Agent 并行管理、统一观察与审查。
- **适合谁**：多 Agent 用户、团队管理者。
- **快速判断**：如果你要"一个控制台管所有 AI 干活"，它很合适；否则不需要。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "the execution layer for multi-agent development. It turns scattered CLI AI agents into a unified local system"。

## 项目方向与定位

多 Agent 执行统一层：每个 Agent 作为受管执行面板（创建/关闭/重启/恢复），实时状态指示，底部浮动终端；从统一控制台运行、观察、审查。

## 主要功能（能做什么）

- 多 Agent 接入（Claude Code/OpenCode/Aider/Codex/Gemini）
- 受管执行面板 + 实时状态
- 创建/关闭/重启/恢复会话
- 统一审查工作台

## 架构设计

```text
agent-team/   核心
design/ docs/ doc_site/
```

## 实现思路与核心逻辑

- "执行面板"抽象：每个 Agent 一个受管会话
- 状态机管理（running/waiting/idle/stopped/error）
- 审查聚合：多 Agent 产出统一查看

## 亮点

- 85 stars，多 Agent 统一控制台
- Apache-2.0、BLUEPRINT 文档
- 与帖子多 Agent 类别契合

## 局限与风险（可选）

- 依赖各 CLI agent
- 与 kobe/ccteam 等竞争

## 分析说明

基于 README、agent-team/ 与文档；未运行。
