# yanhua1010/build-your-own-coding-agent 分析报告

- 仓库：[yanhua1010/build-your-own-coding-agent](https://github.com/yanhua1010/build-your-own-coding-agent)
- 方向：对照开源项目拆解并动手实现 mini coding agent（教学）
- 主要语言：JavaScript/TypeScript（步骤代码）
- 指标：⭐ 22 · License 未见 LICENSE 文件（需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/yanhua1010/build-your-own-coding-agent)

> 分析基于 2026-08-06 抓取的 README、steps/notes 与文档。⚠️ 未见 LICENSE 文件。

## 这是什么（非技术版）

- **这是什么**：一套教学项目。对照 pi、codex、grok-build 三个开源 coding agent，把 Agent 内核层层拆开，同时动手写一个能跑的 mini-agent；全程用国产模型 API（DeepSeek/GLM/Kimi）。
- **能拿来干什么**：从零理解 coding agent 原理并动手实现。
- **适合谁**：想学 Agent 原理的开发者。
- **快速判断**：如果你想"手写一个 Agent"，它是极佳教材；否则不需要。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent（教学）
- 副分类：6. 特定领域 / 其他
- 理由：README 自述"对照三个开源 coding agent 项目，把 agent 的内核一层层拆开，同时动手写一个能跑的 mini-agent"。

## 项目方向与定位

主线 pi（TS/MIT）+ codex/grok-build（Rust/Apache）对比；步骤式实现（steps/01-minimal-loop 可运行）；中文笔记。

## 主要功能（能做什么）

- 系列文章（Agent 本质是 while 循环、统一 LLM API 设计等）
- 可运行 mini-agent 步骤代码
- 国产模型 API

## 架构设计

```text
steps/        可运行实现
notes/        解析笔记
assets/
```

## 实现思路与核心逻辑

- 对照真实项目学架构，再手写验证理解
- 渐进步骤：最小 loop → provider API → ...

## 亮点

- 22 stars，教学价值高、紧跟最新 Agent 架构
- 中文语境 + 国产模型

## 局限与风险（可选）

- **未见 LICENSE 文件**（列入本地 backlog）
- 教程进行中，覆盖未完成

## 分析说明

基于 README、steps/notes 与文档；未运行示例。
