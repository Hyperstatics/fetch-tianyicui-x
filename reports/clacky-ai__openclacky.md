# clacky-ai/openclacky 分析报告

- 仓库：[clacky-ai/openclacky](https://github.com/clacky-ai/openclacky)
- 方向：宣称"最 token 高效"的开源 AI Agent（Ruby CLI）
- 主要语言：Ruby
- 指标：⭐ 1,158 · License MIT · 最近推送 2026-08-03
- 主页/文档：[openclacky.com](https://www.openclacky.com)

> 分析基于 2026-08-04 抓取的 README、目录结构与 Gemfile。

## 这是什么（非技术版）

- **这是什么**：一个命令行 AI Agent，主打"省钱"：宣称同样的活比 Claude Code 成本低约 20%，比其他开源 Agent 省 50%–3 倍，因为只带 16 个精简工具、高缓存命中、子 Agent 路由。
- **能拿来干什么**：日常终端 AI 编程/任务，接任意 OpenAI 兼容模型（BYOK）。
- **适合谁**：在意 token 成本的开发者、Ruby 生态用户。
- **快速判断**：如果你觉得"模型费用贵"，它值得对比；成本数据是其自测口径，需自行验证。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent
- 副分类：1. 通用 Agent Runtime / Harness（轻量 harness 工程）
- 理由：README 自述 "The most Token-efficient open-source AI Agent... built on two years of Agentic R&D and harness engineering"。

## 项目方向与定位

以"token 效率"为核心卖点的 Agent：16 个工具（避免 schema 膨胀）、~100% 缓存命中、subagent 路由（子 Agent 承担简单任务），整体成本宣称 ~0.8× Claude Code、~50% 低于 OpenClaw、~3× 便宜于 Hermes。商业背书：MiraclePlus / 真格 / 红杉中国 / 高瓴。

## 主要功能（能做什么）

- 终端 Agent（Ruby CLI，gem 分发）
- BYOK：任意 OpenAI 兼容模型
- 16 工具精简集、缓存优化、子 Agent 路由
- benchmark 目录、Homebrew、Docker 支持

## 架构设计

```text
bin/           入口
benchmark/     成本/能力对比
docs/ Gemfile（多 Ruby 版本锁） 构建与文档
homebrew/      分发
clacky-legacy/ 旧版
```

## 实现思路与核心逻辑

- 效率优先：工具数最小化 → 减少 schema 开销；缓存命中最大化 → 降低重复 token
- 子 Agent 路由：简单任务交给子 Agent，主 Agent 专注高价值决策
- 以 benchmark 数据驱动宣称，透明对比

## 亮点

- 1.2k stars，成本效率定位有明确数据与对比表
- 顶级机构背书（真格/红杉中国/高瓴），工程投入有厚度
- Ruby 生态的 Agent 稀缺，差异化明显

## 局限与风险（可选）

- 成本数据为内部口径，需独立验证
- Ruby 生态 vs 主流（TS/Python）社区规模较小
- 与"Agent Harness 内测"主题相关度中等

## 分析说明

基于 README、benchmark 目录与 Gemfile；未运行 benchmark 复测。
