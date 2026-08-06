# alexalexalex222/Loop-Factory-mcp-public 分析报告

- 仓库：[alexalexalex222/Loop-Factory-mcp-public](https://github.com/alexalexalex222/Loop-Factory-mcp-public)
- 方向：Loop Factory——让 AI 证明自己变好了（进化评测）
- 主要语言：JavaScript
- 指标：⭐ 0 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/alexalexalex222/Loop-Factory-mcp-public)

> 分析基于 2026-08-06 抓取的 README、loops/ 与文档。

## 这是什么（非技术版）

- **这是什么**：Loop Factory——"让 AI Agent 证明它变好了"。Agent 说改进了工作流？它冻结旧版本，把挑战者同时对基线和无关 sham 评测，重新打开执行收据和磁盘证据，晋升由 operator 控制。worker 提议，verifier 裁决。
- **能拿来干什么**：Agent 自我改进的可验证评测。
- **适合谁**：Agent 研究者、工作流开发者。
- **快速判断**：如果你要"证明 Agent 真变好了"，它很对口；否则不需要。

## 分类

- 主分类：5. 评测 / Benchmark 工具（进化评测）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "Make AI agents prove they got better... freezes the old version, evaluates the challenger against both the baseline and an irrelevant sham, re-opens execution receipts and evidence from disk"。

## 项目方向与定位

本地优先、零依赖、MCP over stdio：worker 提议、verifier 裁决、operator 控制晋升。

## 主要功能（能做什么）

- 旧版冻结 + 挑战者评测（含 sham 对照）
- 证据回放、operator 晋升控制

## 架构设计

```text
loops/ hosts/ proof/ examples/
```

## 实现思路与核心逻辑

- 对抗评测：基线 + 无关 sham 双对照
- 证据驱动晋升

## 亮点

- 0 stars，进化评测理念
- 与帖子"评测/自进化"主题契合
- MIT 开源

## 局限与风险（可选）

- 生态较新
- 依赖 MCP

## 分析说明

基于 README、loops/ 与文档；未运行。
