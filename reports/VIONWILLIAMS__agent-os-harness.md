# VIONWILLIAMS/agent-os-harness 分析报告

- 仓库：[VIONWILLIAMS/agent-os-harness](https://github.com/VIONWILLIAMS/agent-os-harness)
- 方向：小型 DeepSeek-native、证据优先的编码 Agent
- 主要语言：TypeScript
- 指标：⭐ 1 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/VIONWILLIAMS/agent-os-harness)

> 分析基于 2026-08-06 抓取的 README、docs/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"小而证据优先"的编码 Agent（从 Agent OS 提取）。能检查工作区、调用本地工具、请求副作用审批、回放工具历史、留下不存原始提示词的证据轨迹。
- **能拿来干什么**：受控、可审计的编码 Agent。
- **适合谁**：开发者。
- **快速判断**：如果你要"证据优先 + 审批边界"的 Agent，它很对口；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（证据优先）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "A small, DeepSeek-native, evidence-first coding agent... The harness is the engineering layer that gives it a workspace, tools, control boundaries, iteration, and verifiable execution."。

## 项目方向与定位

DeepSeek-native 证据优先 Agent：工作区检查、本地工具、副作用审批、工具历史回放、证据轨迹（不存 raw prompt/reasoning）。

## 主要功能（能做什么）

- 工作区检查、本地工具
- 副作用审批、工具历史回放
- 证据轨迹

## 架构设计

```text
docs/ PROVENANCE.md SECURITY.md
```

## 实现思路与核心逻辑

- "模型还不是 Agent，harness 是工程层"
- 证据优先：可验证执行

## 亮点

- 1 stars，证据优先理念
- 与帖子"Harness"主题直接相关
- MIT 开源

## 局限与风险（可选）

- 生态较新
- 信息有限

## 分析说明

基于 README、docs/ 与文档；未运行。
