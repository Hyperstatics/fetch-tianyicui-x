# felixzhang-glitch/codeClaw 分析报告

- 仓库：[felixzhang-glitch/codeClaw](https://github.com/felixzhang-glitch/codeClaw)
- 方向：Harness 范式的工程落地（飞书/微信桥接到本机 AI CLI）
- 主要语言：Python
- 指标：⭐ 18 · License 未见 LICENSE 文件（需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/felixzhang-glitch/codeClaw)

> 分析基于 2026-08-06 抓取的 README、lib/hooks 与文档。⚠️ 未见 LICENSE 文件。

## 这是什么（非技术版）

- **这是什么**：一个"刻意做薄的 AI 编排层"。把飞书/微信消息桥接到本机 AI CLI（pi/opencode/codex/claude/qodercli），后端运行时可切换；智能（记忆/工具/代码）全部由 CLI Agent 承担，它只做消息收发与编排。
- **能拿来干什么**：用 IM 遥控本机 AI 编程；统一多 CLI 后端。
- **适合谁**：开发者、想"IM 遥控 Agent"的人。
- **快速判断**：如果你想让 AI 从 IM 里被调用，它很实用；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（薄编排层）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述"核心能力交给 CLI agent，codeClaw 收敛为接入层 + 后端路由……不造智能，只做编排"。

## 项目方向与定位

"能力归 agent，编排归 harness"：飞书/微信桥接、渠道适配（格式化/分段/图片）、后端路由切换；pi 默认、opencode 备选。

## 主要功能（能做什么）

- 飞书/微信消息桥接
- 多后端路由切换（pi/opencode/codex/claude/qodercli）
- 会话记忆/上下文压缩由 CLI 原生承载

## 架构设计

```text
lib/ hooks/ memory/ conf/ rules/
```

## 实现思路与核心逻辑

- 极薄 harness：零重复实现智能能力
- CLI-native：以 pi 会话自管为核心

## 亮点

- 18 stars，Harness 范式实践清晰
- 中文文档 + 多后端

## 局限与风险（可选）

- **未见 LICENSE 文件**（列入本地 backlog）
- 依赖各 CLI Agent

## 分析说明

基于 README、lib/hooks 与文档；未运行。
