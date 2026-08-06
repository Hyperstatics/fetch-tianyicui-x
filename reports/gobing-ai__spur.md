# gobing-ai/spur 分析报告

- 仓库：[gobing-ai/spur](https://github.com/gobing-ai/spur)
- 方向：本地优先 harness 工程工具包（包装主流 coding agents）
- 主要语言：TypeScript
- 指标：⭐ 1 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/gobing-ai/spur)

> 分析基于 2026-08-06 抓取的 README、.spur/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"harness 工程工具包"。不是 coding agent、不是 BYOK 平台；它包装你已经装好的 Agent（Claude Code/Codex/Gemini CLI/pi/OpenCode 等），加执行纪律：检测与健康检查、约束检查、工作流编排、会话历史导入与分析。
- **能拿来干什么**：给现有 Agent 加治理层。
- **适合谁**：开发者、Agent 工作流设计者。
- **快速判断**：如果你要"给现有 Agent 加纪律"，它很对口；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（harness 工具包）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "Local-first harness engineering toolkit for mainstream coding agents... wraps them with execution discipline"。

## 项目方向与定位

harness 工具包：Agent 检测/健康检查、约束检查、工作流编排、会话历史导入与分析。

## 主要功能（能做什么）

- Agent 检测与健康检查
- 约束检查、工作流编排
- 会话历史导入/分析

## 架构设计

```text
.spur/ .claude-plugin/ .moon/
```

## 实现思路与核心逻辑

- "包装而非替代"：给已有 Agent 加执行纪律

## 亮点

- 1 stars，harness 工程定位
- 与帖子"Harness"主题直接相关
- Apache-2.0

## 局限与风险（可选）

- 生态较新
- 依赖多 Agent 安装

## 分析说明

基于 README、.spur/ 与文档；未运行。
