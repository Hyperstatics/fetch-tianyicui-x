# bex-co/bex 分析报告

- 仓库：[bex-co/bex](https://github.com/bex-co/bex)
- 方向：Render 的开源 AI 原生替代（Git 部署到 HTTPS，自持基础设施）
- 主要语言：Go
- 指标：⭐ 415 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[架构 ADR](https://github.com/bex-co/bex/blob/main/docs/ADR002-architecture.md)

> 分析基于 2026-08-06 抓取的 README、cli/dashboard 结构与架构文档。

## 这是什么（非技术版）

- **这是什么**：一个"自己家的部署平台"。从 Git 仓库自动部署到 HTTPS，跑在你自己的基础设施上；开发者和 AI 编码 Agent 都能用同一个控制面管理部署。
- **能拿来干什么**：自托管应用部署、给团队/Agent 提供部署入口。
- **适合谁**：开发者、SRE、想自建部署平台的团队。
- **快速判断**：如果你要"私有化 Render/Heroku"，它很对口；否则用云平台即可。

## 分类

- 主分类：6. 特定领域 / 其他（部署平台）
- 副分类：2. Coding Harness / 工程向 Agent（Agent 可用控制面）
- 理由：README 自述 "The open-source, AI-native alternative to Render... give developers and coding agents the same first-class control plane"。

## 项目方向与定位

AI 原生的自托管部署平台：Git → HTTPS，开发者与编码 Agent 统一控制面。CLI + dashboard，Apache-2.0。

## 主要功能（能做什么）

- Git 仓库自动部署、HTTPS
- 开发者/Agent 统一控制面（CLI + dashboard）
- 架构 ADR 文档、Docker 部署

## 架构设计

```text
cli/          命令行
dashboard/    控制台
docs/ADR002-architecture.md  架构决策
```

## 实现思路与核心逻辑

- 以"自持基础设施"为核心：部署平台可控、数据自有
- Agent 友好：控制面 API 与 CLI 让编码 Agent 可直接操作

## 亮点

- 415 stars，Render 开源替代定位稀缺
- Apache-2.0，自托管友好
- 架构文档（ADR）规范

## 局限与风险（可选）

- 与"Agent Harness 内测"主题相关度低（偏 PaaS 层）
- 功能面仍在早期

## 分析说明

基于 README、cli/dashboard 与 ADR 文档；未部署。
