# Zane456/PCB-Agent-Teams 分析报告

- 仓库：[Zane456/PCB-Agent-Teams](https://github.com/Zane456/PCB-Agent-Teams)
- 方向：KiCad PCB 工作流——描述板子，得到可生产的 Gerber
- 主要语言：Python（skill/工作流）
- 指标：⭐ 27 · License PolyForm Noncommercial 1.0.0（**非商用**）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/Zane456/PCB-Agent-Teams)

> 分析基于 2026-08-06 抓取的 README、Projects/ 与 LICENSE.md。⚠️ PolyForm Noncommercial 1.0.0，商用需书面许可。

## 这是什么（非技术版）

- **这是什么**：一个"说需求就能出 PCB"的工作流。描述想要的电路板，得到 KiCad 项目 + 可生产的 Gerber 文件；每个器件对照实时库存，每个阶段由脚本、SPICE 和 DRC 把关，不靠模型自说自话。
- **能拿来干什么**：AI 辅助 PCB 设计、从拓扑讨论到 Gerber 出货全流程。
- **适合谁**：硬件工程师、PCB 设计者。
- **快速判断**：如果你做 PCB 设计且想要"AI 走完整流程"，它很有价值；**注意非商用许可**。

## 分类

- 主分类：6. 特定领域 / 其他（硬件/PCB 工作流）
- 副分类：3. 多 Agent 编排 / 协作系统（Agent Teams）
- 理由：README 自述 "Describe the board you want. Get back a KiCad project and a fab-ready Gerber package"。

## 项目方向与定位

KiCad 10 多项目 PCB 工作区：10 个 skills 驱动 Phase 0–5 管道（拓扑讨论 → Gerber 出货）；实时库存检查、SPICE/DRC 验证；Claude Code only。

## 主要功能（能做什么）

- 自然语言 → KiCad 项目 + Gerber
- 实时器件库存检查
- 脚本/SPICE/DRC 阶段验证
- 多项目工作区、中文文档

## 架构设计

```text
Projects/      项目
lib_external/ lib_cache/
.claude/ CLAUDE.md
```

## 实现思路与核心逻辑

- "人话描述 → 硬件产出"：把 PCB 全流程 Agent 化
- 验证优先：每个阶段过脚本/SPICE/DRC

## 亮点

- 27 stars，PCB 垂直领域稀缺
- 验证链完整（库存/SPICE/DRC）
- 中文社区

## 局限与风险（可选）

- **PolyForm 非商用许可**（列入本地 backlog）
- 仅 Claude Code 运行时、macOS 验证

## 分析说明

基于 README、Projects/ 与 LICENSE.md；未运行工作流。
