# nextlevelbuilder/goclaw 分析报告

- 仓库：[nextlevelbuilder/goclaw](https://github.com/nextlevelbuilder/goclaw)
- 方向：多租户 AI Agent 平台 / 多 Agent AI 网关
- 主要语言：Go
- 指标：⭐ 3,502 · License CC BY-NC 4.0（**非商用**）· 最近推送 2026-08-03
- 主页/文档：[docs.goclaw.sh](https://docs.goclaw.sh)

> 分析基于 2026-08-04 抓取的 README、cmd/ 与 docker 配置。**许可证为 CC BY-NC 4.0（署名-非商用）**，商用需另行授权。

## 这是什么（非技术版）

- **这是什么**：一个"AI 网关/平台"。一个程序统一接入 20+ 模型服务商、7 种消息渠道（Telegram/Discord 等），支持多租户，供团队部署自己的 AI 助手与多 Agent 协作。
- **能拿来干什么**：自建多租户 AI 平台、统一模型路由、给不同客户/群组提供 AI 服务。
- **适合谁**：开发者、想要自托管 AI 平台的团队。
- **快速判断**：如果你要"一个二进制跑起多租户 AI 网关"，它很合适；**注意许可证限制非商用，商用需授权**。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（多租户 AI 网关）
- 副分类：3. 多 Agent 编排 / 协作系统（agents that orchestrate for you）
- 理由：README 自述 "Multi-tenant AI Agent Platform... Multi-agent AI gateway built in Go. 20+ LLM providers. 7 channels. Multi-tenant PostgreSQL."。

## 项目方向与定位

生产级多租户 AI 网关：单二进制、20+ LLM 提供商、7 个渠道（含 WebSocket/浏览器/CLI 等）、多租户 PostgreSQL、OpenTelemetry 可观测。定位是"能直接部署的 AI Agent 平台底座"。

## 主要功能（能做什么）

- 20+ LLM 提供商接入与路由
- 7 种渠道（浏览器、CLI、消息平台、WebSocket 等）
- 多租户 PostgreSQL 数据隔离
- Docker Compose 全家桶（claude-cli/cloudflared/otel/lightpanda 等）
- OpenTelemetry 集成、多语言 README

## 架构设计

```text
cmd/       入口
docker/ compose.d/ compose.options/  部署矩阵（多场景 compose）
_readmes/ _statics/  文档与静态资源
api-reference.md
```

## 实现思路与核心逻辑

- 网关模式：统一模型路由 + 多渠道接入 + 租户隔离
- 部署即产品：一堆开箱即用的 docker-compose 场景
- 生产可观测（OpenTelemetry）

## 亮点

- 3.5k stars，Go 单二进制多租户方案稀缺
- 渠道/提供商覆盖广，Docker 部署矩阵完整
- 工程成熟度高（多语言文档、API reference、changelog）

## 局限与风险（可选）

- **CC BY-NC 4.0**：非商用许可证，商用/托管需联系版权方（已列入 backlog 许可证盘点）
- 功能面大，上手配置复杂
- 与"内测 Harness"主题相关度中等（偏平台/网关）

## 分析说明

基于 README、cmd/、docker 配置与 LICENSE；未运行平台。
