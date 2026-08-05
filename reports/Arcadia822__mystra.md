# Arcadia822/mystra 分析报告

- 仓库：[Arcadia822/mystra](https://github.com/Arcadia822/mystra)
- 方向：coding-agent 编排平台（headless 控制面）
- 主要语言：TypeScript
- 指标：⭐ 2 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/Arcadia822/mystra)

> 分析基于 2026-08-06 抓取的 README、.od-skills/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"编码 Agent 编排平台"。通过 HTTP/CLI/MCP 提交工作、本地优先持久化、可插拔的 Issue/runtime/repository 接缝、pull-based runners 在沙箱执行并返回结构化审查交接。
- **能拿来干什么**：多 Agent 工作编排、沙箱执行。
- **适合谁**：开发者、Agent 平台团队。
- **快速判断**：如果你要"headless 多 Agent 控制面"，它很对口；否则不需要。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "an open-source coding-agent orchestration platform... headless control plane for submitting work through HTTP, CLI or MCP"。

## 项目方向与定位

基于 Open Agents 参考架构的编排平台：HTTP/CLI/MCP 提交、本地优先持久化、可插拔接缝、沙箱 pull runners、结构化审查交接。

## 主要功能（能做什么）

- headless 控制面（HTTP/CLI/MCP）
- 本地优先持久化
- 沙箱 runners + 审查交接

## 架构设计

```text
.od-skills/ .specify/
```

## 实现思路与核心逻辑

- 参考 Open Agents 架构，本地化持久化
- pull-based 执行 + 审查

## 亮点

- 2 stars，编排平台定位
- MIT 开源

## 局限与风险（可选）

- 项目较新
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、.od-skills/ 与文档；未运行。
