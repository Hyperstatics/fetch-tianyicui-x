# cosmtrek/jeju 分析报告

- 仓库：[cosmtrek/jeju](https://github.com/cosmtrek/jeju)
- 方向：声明式本地优先的受限 Agent 运行时
- 主要语言：Go
- 指标：⭐ 26 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/cosmtrek/jeju)

> 分析基于 2026-08-06 抓取的 README、cmd/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"用清单文件定义 AI"的运行时。像 Kubernetes 描述部署一样描述 Agent（模型、指令、循环、工作区、工具、技能、权限、预算、输出 schema、评估器），它校验、编译、运行，并把每个效果记录到 trajectory.jsonl；还能用评估证据改进 Agent。
- **能拿来干什么**：声明式 Agent 部署、可审计执行。
- **适合谁**：开发者、想要"manifest 即 Agent"的人。
- **快速判断**：如果你喜欢声明式配置管理 Agent，它很有特色；否则传统框架即可。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（声明式运行时）
- 副分类：5. 评测 / Benchmark 工具（evaluators/evolve）
- 理由：README 自述 "Declarative, local-first runtime for bounded AI agents. Define an agent in one manifest, run it headless, and audit every effect."。

## 项目方向与定位

"Jeju 之于 Agent 如 K8s manifest 之于部署"：一个 manifest 定义 Agent，headless 运行，trajectory.jsonl 记录效果；评估证据驱动 `jeju evolve` 改进。

## 主要功能（能做什么）

- 声明式 Agent manifest（model/instructions/loop/workspace/tools/skills/permissions/budget/output schema/evaluators）
- headless 运行 + trajectory.jsonl 审计
- jeju evolve（评估驱动改进）
- catalog、benchmarks、examples

## 架构设计

```text
cmd/           CLI
catalog/ examples/ benchmarks/ docs/
```

## 实现思路与核心逻辑

- Manifest 即真相：Agent 全配置化、可复现
- 效果审计：每次运行留轨迹
- 评估闭环：证据 → evolve

## 亮点

- 26 stars，声明式 Agent 运行时理念新颖
- 审计与进化闭环完整
- MIT 开源

## 局限与风险（可选）

- 项目较新，生态待验证
- 与"内测 Harness"主题相关度中等（运行时/评测）

## 分析说明

基于 README、cmd/ 与文档；未运行。
