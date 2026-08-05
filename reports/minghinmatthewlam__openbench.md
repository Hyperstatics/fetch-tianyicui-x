# minghinmatthewlam/openbench 分析报告

- 仓库：[minghinmatthewlam/openbench](https://github.com/minghinmatthewlam/openbench)
- 方向：比较 coding-agent harness 的 benchmark（同一模型，harness 影响多大）
- 主要语言：Python
- 指标：⭐ 118 · License MIT · 最近推送 2026-08-03
- 主页/文档：[WRITEUP](https://github.com/minghinmatthewlam/openbench/blob/main/WRITEUP.md) · [RESULTS](https://github.com/minghinmatthewlam/openbench/blob/main/RESULTS.md)

> 分析基于 2026-08-06 抓取的 README、bench/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"Agent 框架考试系统"。它回答的问题是：同一个模型、同一个任务，外面包的 harness（Codex/Pi/OpenCode/Cursor 等）到底影响多大？
- **能拿来干什么**：对比编码 Agent 框架的性能、在自己的私有代码库上做评测。
- **适合谁**：Agent 研究者、选型团队、评测工程师。
- **快速判断**：如果你想"量化比较 Agent harness"，它很对口；否则不需要。

## 分类

- 主分类：5. 评测 / Benchmark 工具
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "A benchmark for comparing coding-agent harnesses... given the same underlying model and task, how much does the harness around it matter?"。

## 项目方向与定位

聚焦 harness 层对比：CLI 工具在 run loop/工具集/权限策略上的差异。提供 obench CLI（`obench run [suite.toml]`）、Harbor 生态（suites/profiles/metering/results）、私有代码库评测、OAuth 认证与密封代理计量。

## 主要功能（能做什么）

- harness 对比基准（codex/pi/opencode/cursor/devin/claude）
- obench CLI + suite.toml 定义
- Harbor：任务/套件/配置/证据校验/计量
- 私有代码库评测（obench init）
- 文档完善（WRITEUP/RESULTS/SETUP）

## 架构设计

```text
bench/ data/ docs/
ablation/（消融实验）
```

## 实现思路与核心逻辑

- 控制变量：同模型同任务，只变 harness
- 证据严格校验（Harbor evidence validation）
- 计量密封（sealed proxy metering）保证结果可信

## 亮点

- 118 stars，"harness 本身值多少"的评测定位独特
- 方法论严谨（消融/证据/计量）
- 与帖子"Agent Harness"主题直接相关

## 局限与风险（可选）

- 评测结果时效性强，需持续更新
- 上手需要理解 Harbor 概念

## 分析说明

基于 README、bench/docs 与文档；未运行评测。
