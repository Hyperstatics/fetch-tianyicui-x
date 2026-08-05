# yologdev/yoagent 分析报告

- 仓库：[yologdev/yoagent](https://github.com/yologdev/yoagent)
- 方向：The agent loop for Rust（7 种 LLM 协议流式 + 工具 + 循环）
- 主要语言：Rust
- 指标：⭐ 173 · License MIT · 最近推送 2026-08-03
- 主页/文档：[yologdev.github.io/yoagent](https://yologdev.github.io/yoagent)

> 分析基于 2026-08-06 抓取的 README、src/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个 Rust 版的"Agent 主循环库"。让 Rust 程序接入 7 种 LLM 协议（流式输出）、执行工具、循环直到任务完成。
- **能拿来干什么**：用 Rust 构建 Agent/工具链；高性能、低延迟的 Agent 运行时。
- **适合谁**：Rust 开发者、Agent 基础设施团队。
- **快速判断**：如果你用 Rust 做 Agent，它很对口；否则其他生态更成熟。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（Agent 循环库）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "The agent loop for Rust. Stream from any of 7 LLM protocols, run tools, loop until done."。

## 项目方向与定位

Rust Agent 循环：prompt → LLM 流式 → 工具执行 → 循环。多协议抽象（7 种）、crates.io 发布、文档站（book）。

## 主要功能（能做什么）

- 7 种 LLM 协议流式接入
- 工具执行与循环
- crates.io（yoagent）、文档站、examples

## 架构设计

```text
src/          核心
docs/ book.toml
examples/ scripts/
```

## 实现思路与核心逻辑

- 协议抽象层：7 种 LLM 协议统一为流式接口
- 循环内核：LLM 输出 → 工具 → 再入 LLM，直到完成

## 亮点

- 173 stars，Rust Agent 生态稀缺
- MIT 开源、crates.io 分发、文档完善

## 局限与风险（可选）

- Rust 生态 Agent 工具较少，社区待成长
- 与 yoyo-evolve 同作者，功能面相对基础

## 分析说明

基于 README、src/ 与文档；未运行。
