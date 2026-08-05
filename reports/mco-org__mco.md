# mco-org/mco 分析报告

- 仓库：[mco-org/mco](https://github.com/mco-org/mco)
- 方向：CLI-first 的多 Agent 编排层（并行跑、对比原始答案再行动）
- 主要语言：Python
- 指标：⭐ 471 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/mco-org/mco)

> 分析基于 2026-08-06 抓取的 README、mco/ 与目录结构。

## 这是什么（非技术版）

- **这是什么**：一个"多 AI 意见征询器"。把同一个任务同时交给多个 Agent/模型并行执行，把它们的原始回答摆在一起对比，你再决定怎么做；减少单个模型的盲区。
- **能拿来干什么**：代码审查、实现、架构分析、CI 检查等多视角任务。
- **适合谁**：开发者、需要"多模型交叉验证"的团队。
- **快速判断**：如果你担心"一个 AI 有盲区"，它很实用；否则不需要。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "Orchestrate AI coding agents. Compare perspectives. Act with confidence... Give one task to the agents and models you choose, run them in parallel, and compare their raw answers"。

## 项目方向与定位

轻量 CLI-first 编排层：一个任务 → 多个 Agent/模型并行 → 对比原始回答 → 行动。可从终端或由另一个编码 Agent（Claude Code/Codex/Cursor/Copilot/Pi/OpenClaw）调用。

## 主要功能（能做什么）

- 多 Agent/模型并行执行同一任务
- 原始回答对比、盲区互补
- 代码审查/实现/架构分析/CI 检查场景
- npm 包（@tt-a1i/mco）+ Python

## 架构设计

```text
mco/          核心
bin/ docs/
```

## 实现思路与核心逻辑

- "对比后行动"：用多模型交叉验证降低单模型盲区
- 与现有 Agent 兼容（可被编码 Agent 调用）
- CLI 优先，轻量无依赖

## 亮点

- 471 stars，多 Agent 对比模式简单实用
- 与 squad/mco 系生态联动，MIT 开源
- 中英双语文档

## 局限与风险（可选）

- 并行多模型调用成本翻倍
- 复杂编排场景需要更重的工具

## 分析说明

基于 README、mco/ 与文档；未运行。
