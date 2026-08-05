# ythx-101/agent-sop 分析报告

- 仓库：[ythx-101/agent-sop](https://github.com/ythx-101/agent-sop)
- 方向：human-gated 的编码 Agent 协作 SOP（按风险分级流程）
- 主要语言：Python（skill）
- 指标：⭐ 46 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/ythx-101/agent-sop)

> 分析基于 2026-08-06 抓取的 README、SKILL.md 与文档。

## 这是什么（非技术版）

- **这是什么**：一套"给 AI 立规矩"的作业流程（SOP）。高风险活走完整可审计链路（研究→计划→人批准→实现→独立评审→验证→签收→部署），低风险活走轻流程；不为小事套仪式。
- **能拿来干什么**：让 AI 干活更可控、可审查、可签字。
- **适合谁**：用 AI 写生产代码的团队。
- **快速判断**：如果你要"按风险分级管控 AI 干活"，它很实用；否则不需要。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent（工作流/治理）
- 副分类：5. 评测 / Benchmark 工具（验证/签收）
- 理由：README 自述 "A human-gated, capability-slotted collaboration workflow (SOP) for coding agents"。

## 项目方向与定位

目标不是让 Agent 更自主，而是按风险挑流程重量：高风险走完整可审计序列，低风险走轻路径；tier 定义在 SKILL.md §1.1。

## 主要功能（能做什么）

- 风险分级流程（tiers）
- 高风险完整链路（research→plan→approval→implement→review→verify→signoff→deploy）
- templates/references/scripts

## 架构设计

```text
SKILL.md      核心流程定义
templates/ references/ scripts/
```

## 实现思路与核心逻辑

- "流程重量匹配风险"：避免过度仪式
- human-gated：关键节点由人批准/签收

## 亮点

- 46 stars，Agent 治理/流程主题与帖子契合
- 分级设计务实
- MIT 开源

## 局限与风险（可选）

- 需要团队流程配合
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、SKILL.md 与文档；未运行。
