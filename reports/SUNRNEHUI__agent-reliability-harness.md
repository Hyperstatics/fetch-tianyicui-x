# SUNRNEHUI/agent-reliability-harness 分析报告

- 仓库：[SUNRNEHUI/agent-reliability-harness](https://github.com/SUNRNEHUI/agent-reliability-harness)
- 方向：跨 Agent 的可靠执行 harness（Plan-native skill）
- 主要语言：Python（skill）
- 指标：⭐ 2 · License 未见 LICENSE 文件（需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/SUNRNEHUI/agent-reliability-harness)

> 分析基于 2026-08-06 抓取的 README、master-prompt.md 与文档。⚠️ 未见 LICENSE 文件。版本 v9.1.0（2026-08-02）。

## 这是什么（非技术版）

- **这是什么**：一个"跨 Agent 可靠执行"的 skill。跨 Codex、Claude Code、Grok 等可用：普通工作用运行时自己的 Plan，跨边界时才物化中立的 provider 契约，风险需要时才加审计控制。
- **能拿来干什么**：给多 Agent 加可靠性/审计边界。
- **适合谁**：多 Agent 用户、团队。
- **快速判断**：如果你要"按需加重的可靠性层"，它很对口；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（可靠性 harness）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "a Plan-native skill for reliable execution across Codex, Claude Code, Grok... adds audit controls only when risk requires them"。

## 项目方向与定位

Plan-native 可靠性 skill：默认轻、跨边界时物化契约、高风险时加审计。

## 主要功能（能做什么）

- 跨 Agent（Codex/Claude Code/Grok）可靠执行
- provider-neutral 契约、审计控制

## 架构设计

```text
master-prompt.md + adapters/ agents/ references/ scripts/
```

## 实现思路与核心逻辑

- "按风险加重"：不套仪式，需要时才物化契约/审计

## 亮点

- 2 stars，可靠性 harness 与帖子主题直接相关
- 设计务实（渐进加重）

## 局限与风险（可选）

- **未见 LICENSE 文件**（列入本地 backlog）
- 生态较新

## 分析说明

基于 README、master-prompt.md 与文档；未运行。
