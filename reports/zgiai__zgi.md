# zgiai/zgi 分析报告

- 仓库：[zgiai/zgi](https://github.com/zgiai/zgi)
- 方向：Agent Runtime 工作区（agents/workflows/skills/knowledge/model routes）
- 主要语言：Go（后端）+ Next.js（前端）
- 指标：⭐ 311 · License ZGI Community License 1.0（自定义社区许可）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/zgiai/zgi)

> 分析基于 2026-08-06 抓取的 README、api/web 结构与 LICENSE。注意：采用 ZGI Community License（自定义），非标准开源许可证。

## 这是什么（非技术版）

- **这是什么**：一个"Agent 运行时工作区"。用来构建、运行和运营 AI Agent、工作流、技能、知识库和模型路由；Docker Compose 一键起。
- **能拿来干什么**：自托管 Agent 平台、多 Agent 工作流、知识/技能管理。
- **适合谁**：开发者、想自建 Agent 平台的中小团队。
- **快速判断**：如果你要"开箱即用的 Agent Runtime 工作区"，它值得看；**注意自定义许可证**，使用前需读条款。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness
- 副分类：6. 特定领域 / 其他（平台工作区）
- 理由：README 自述 "An Agent Runtime workspace with source code available for building, running, and operating AI agents, workflows, skills, knowledge, and model routes"。

## 项目方向与定位

Go + Next.js 的 Agent Runtime 工作区：agents、workflows、skills、knowledge、model routes 一体化，Docker Compose 部署，社区版开源（自定义许可）。

## 主要功能（能做什么）

- Agent/工作流/技能/知识/模型路由管理
- Go API + Next.js Web
- Docker Compose 一键运行

## 架构设计

```text
api/         Go 后端
web/         Next.js 前端
docker/ docs/
```

## 实现思路与核心逻辑

- 平台化集成：运行时 + 工作区 + 管理面一体
- 开源社区版 + 自定义许可（非 OSI 标准）

## 亮点

- 311 stars，Agent 平台自托管方案
- Go 后端 + Docker 部署，运维简单

## 局限与风险（可选）

- **ZGI Community License**：自定义许可证，商用/分发需确认条款（列入本地 backlog）
- 生态较新

## 分析说明

基于 README、api/web 结构与 LICENSE；未运行。
