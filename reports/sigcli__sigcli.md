# sigcli/sigcli 分析报告

- 仓库：[sigcli/sigcli](https://github.com/sigcli/sigcli)
- 方向：AI Agent 安全认证工具（浏览器 SSO + 凭据加密注入）
- 主要语言：TypeScript
- 指标：⭐ 279 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/sigcli/sigcli)

> 分析基于 2026-08-06 抓取的 README、cli/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"给 AI 发通行证但不给钥匙"的工具。AI 要访问 Jira、wiki、日历等系统时，由它完成浏览器 SSO 登录、加密保存凭据、按需注入进程——AI 永远看不到密码本身。
- **能拿来干什么**：让 Agent 安全地访问内部系统，避免凭据泄露。
- **适合谁**：企业开发者、关心 Agent 安全的团队。
- **快速判断**：如果你让 AI 访问内部系统又担心凭据安全，它很有用；否则不需要。

## 分类

- 主分类：6. 特定领域 / 其他（安全/认证工具）
- 副分类：1. 通用 Agent Runtime / Harness（Agent 基础设施）
- 理由：README 自述 "handles browser SSO, encrypts credentials at rest, and injects them into any process — so your agents authenticate without ever seeing secrets"。

## 项目方向与定位

解决"Agent 需要访问工作系统但凭据不能进 shell history/环境变量/上下文"的问题：sig 做浏览器 SSO、静态加密存储、进程注入。`sig request` 让 Agent 直接以已认证身份调 API。

## 主要功能（能做什么）

- 浏览器 SSO 一次性登录
- 凭据加密静态存储（~/.sig）
- 注入任意进程；`sig request` 代理认证请求
- npm 全局安装（@sigcli/cli）

## 架构设计

```text
cli/          核心
website/      站点
```

## 实现思路与核心逻辑

- 凭据与 Agent 隔离：Agent 只见认证结果，不见 secrets
- 进程注入 + 请求代理：透明地为 Agent 提供认证

## 亮点

- 279 stars，Agent 安全认证痛点定位精准
- MIT 开源，CLI 即用

## 局限与风险（可选）

- 企业 SSO/合规场景需自行评估
- 与"Agent Harness 内测"主题相关度低（安全基础设施）

## 分析说明

基于 README、cli/ 与文档；未运行认证流程。
