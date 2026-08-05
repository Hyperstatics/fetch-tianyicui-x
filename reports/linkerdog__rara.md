# linkerdog/rara 分析报告

- 仓库：[linkerdog/rara](https://github.com/linkerdog/rara)
- 方向：快速、本地优先的终端 Coding Agent
- 主要语言：Rust
- 指标：⭐ 14 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/linkerdog/rara)

> 分析基于 2026-08-06 抓取的 README、components/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个本地优先的终端 AI 编程助手。选模型、让它写代码或探索仓库，通过富 TUI 实时看流式输出、语法高亮和并排上下文。
- **能拿来干什么**：日常终端 AI 编程，本地数据不出机器。
- **适合谁**：开发者、注重本地优先的人。
- **快速判断**：如果你想要"本地跑、TUI 好看"的 Agent，它值得试；否则主流 Agent 更成熟。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "A fast, local-first coding agent for your terminal... no cloud dependency required"。

## 项目方向与定位

本地优先终端 Agent：模型自由（Claude/DeepSeek/Gemini/Ollama 等）、TUI 流式/高亮/并排上下文。

## 主要功能（能做什么）

- 本地运行、模型自由
- 写代码/探索仓库
- 富 TUI（流式/语法高亮/并排上下文）

## 架构设计

```text
components/      UI/核心组件
（Rust + Bazel 构建）
```

## 实现思路与核心逻辑

- 本地优先：数据与模型选择自主
- TUI 增强可观察性

## 亮点

- 14 stars，Rust 终端 Agent
- Apache-2.0

## 局限与风险（可选）

- 生态较新
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、components/ 与文档；未运行。
