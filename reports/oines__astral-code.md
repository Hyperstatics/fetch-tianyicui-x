# oines/astral-code 分析报告

- 仓库：[oines/astral-code](https://github.com/oines/astral-code)
- 方向：provider-neutral 编码 Agent harness（Codex CLI fork）
- 主要语言：Rust
- 指标：⭐ 1 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/oines/astral-code)

> 分析基于 2026-08-06 抓取的 README、.codex/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个从 OpenAI Codex CLI fork 的"任意模型"编码 Agent（命令 `astral`）。去掉 OpenAI 托管依赖，重新改装运行时，让它可以接任何 LLM（本地或远程），保留 Codex 的 Rust 核心、跨平台沙箱和 TUI。
- **能拿来干什么**：用任意模型跑 Codex 式 Agent。
- **适合谁**：开发者、多模型用户。
- **快速判断**：如果你想要"Codex 体验 + 任意模型"，它很对口；否则官方 Codex 即可。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "A provider-neutral coding agent harness forked from OpenAI Codex CLI... works with any LLM provider — local or remote — while keeping Codex's proven Rust core, cross-platform sandbox, and TUI"。

## 项目方向与定位

Codex fork：provider-neutral、保留 Rust 核心/沙箱/TUI。

## 主要功能（能做什么）

- 任意 LLM 提供商
- 跨平台沙箱、TUI

## 架构设计

```text
（Rust + Bazel，Codex 同构）
```

## 实现思路与核心逻辑

- 去 OpenAI 依赖、接通用 provider

## 亮点

- 1 stars，Codex 生态 fork
- Apache-2.0

## 局限与风险（可选）

- fork 维护依赖作者
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、目录结构与文档；未运行。
