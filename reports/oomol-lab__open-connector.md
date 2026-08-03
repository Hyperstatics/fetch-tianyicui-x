# oomol-lab/open-connector 分析报告

- 仓库：[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)
- 方向：AI Agent 连接器网关（Pipedream / Composio 的开源替代）
- 主要语言：TypeScript（Node.js 22+，Cloudflare 兼容）
- 指标：⭐ 4,178 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[OOMOL](https://oomol.com/apps) · [自托管文档](https://oomol.com/docs/openconnector-self-hosting/)

> 分析基于 2026-08-04 抓取的 README、目录结构与部署文档。

## 这是什么（非技术版）

- **这是什么**：一个"应用连接中转站"。用户的应用账号（网盘、邮箱、IM 等）只需授权一次，之后 AI/应用就能通过它调用 1000+ 服务商的 10000+ 现成操作。
- **能拿来干什么**：让 AI 能真正"操作你的各种账号"；给应用加连接器能力，不用每个服务商单独对接。
- **适合谁**：开发者、SaaS 团队、想给 Agent 加工具能力的个人。
- **快速判断**：如果你要"一个网关接所有第三方应用"，它很合适；如果只是单服务对接，直接调 API 就行。

## 分类

- 主分类：6. 特定领域 / 其他（连接器网关/集成平台）
- 副分类：1. 通用 Agent Runtime / Harness（Agent 工具基础设施）
- 理由：README 自述 "open-source connector gateway for AI agents and an alternative to Pipedream/Composio"。

## 项目方向与定位

"Connect once. Use everywhere."——用户账号授权一次，向 Agent 和应用暴露统一目录（1000+ providers / 10000+ Actions）。三种部署：OOMOL 托管、Cloudflare（Workers/D1/R2）、自托管（Docker/Node）。MCP 与 OpenAPI 3.1 就绪。

## 主要功能（能做什么）

- 统一连接器目录：1000+ 提供商、10000+ 预置 Actions
- OAuth 管理；MCP / OpenAPI 3.1 协议暴露
- 三种部署方式（托管 / Cloudflare / 自托管）
- Connector SDK 供应用代码调用；migrations / docker / fly.toml 齐全

## 架构设计

```text
src/（根目录）核心服务
docker/ docker-compose.yml  容器部署
migrations/                 数据库迁移
scripts/ examples/ docs/
```

## 实现思路与核心逻辑

- "连接器即目录"：授权、凭据、操作统一管理，Agent 按目录发现能力
- 云原生优先：Cloudflare Workers/D1/R2 兼容，Node 22+ 运行
- 协议层开放：MCP + OpenAPI，避免绑定单一 Agent

## 亮点

- 4.2k stars，连接器赛道开源替代（Pipedream/Composio）直接对标
- 三种部署路径，从托管到自托管全覆盖
- 1000+/10000+ 规模的目录是护城河

## 局限与风险（可选）

- 连接器目录的维护与第三方 OAuth 稳定性依赖生态投入
- 自托管需要自己管理 OAuth app 与存储
- 与"Agent Harness 内测"主题相关度中等（是 Agent 工具层而非运行时）

## 分析说明

基于 README、目录结构与部署文档；未运行服务。
