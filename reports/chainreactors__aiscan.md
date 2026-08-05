# chainreactors/aiscan 分析报告

- 仓库：[chainreactors/aiscan](https://github.com/chainreactors/aiscan)
- 方向：AI 驱动单二进制渗透测试 Agent（内置多引擎军火库）
- 主要语言：Go
- 指标：⭐ 234 · License AGPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/chainreactors/aiscan)

> 分析基于 2026-08-06 抓取的 README、agent/aop/core 结构与文档。仅限授权目标，未经授权使用违法。

## 这是什么（非技术版）

- **这是什么**：一个"AI 安全扫描器"。把大模型 Agent 和传统安全扫描引擎结合，既能做确定性的扫描流水线，也能用自然语言做自主评估，还支持多 Agent 分布式协作。
- **能拿来干什么**：渗透测试、漏洞扫描、安全评估（需授权）。
- **适合谁**：安全工程师、渗透测试人员。
- **快速判断**：如果你做授权的安全测试且想要 AI 辅助，它很有价值；**未授权使用是违法的**。

## 分类

- 主分类：6. 特定领域 / 其他（安全/渗透工具）
- 副分类：2. Coding Harness / 工程向 Agent（Agent 化扫描）
- 理由：README 自述 "AI-driven single-binary pentest agent with a built-in multi-engine arsenal"。

## 项目方向与定位

LLM Agent + 传统安全扫描引擎：Scan（确定性流水线 + 可选 AI 辅助）、Agent（自然语言自主评估）、IOA（多 Agent 分布式协作）。单二进制、内置多引擎、即装即用。

## 主要功能（能做什么）

- Scan / Agent / IOA 三种模式
- 内置多引擎扫描能力（web 安全）
- 单二进制分发（goreleaser）、Docker、Web 界面
- 中文文档、CI

## 架构设计

```text
agent/         Agent 层
core/ aop/     核心与切面
cmd/ web/      入口与界面
docs/ examples/
```

## 实现思路与核心逻辑

- 传统引擎做确定性检测 + LLM 做自主推理与编排
- IOA 模式多 Agent 协作扩大覆盖
- 单二进制降低部署门槛

## 亮点

- 234 stars，AI 渗透赛道活跃项目
- 三模式（扫描/Agent/IOA）覆盖不同使用场景
- 单二进制 + Docker + Web 分发完整

## 局限与风险（可选）

- **AGPL-3.0**：派生分发需遵守 copyleft
- 安全工具使用必须严格限授权目标
- 预览阶段，API 可能变化

## 分析说明

基于 README、agent/core 结构与文档；未运行扫描。
