# open-multi-agent/open-multi-agent 分析报告

- 仓库：[open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent)
- 方向：TypeScript 多 Agent 编排框架——"描述目标，而非流程图"
- 主要语言：TypeScript
- 指标：⭐ 6,710 · License MIT · 最近推送 2026-08-03
- 主页/文档：[open-multi-agent.com](https://open-multi-agent.com)

> 分析基于 2026-08-04 抓取的 README、packages/ 结构与 CI 配置。

## 这是什么（非技术版）

- **这是什么**：一个"多 AI 调度中心"。你告诉它目标（比如"整理这份报告"），它自己规划把任务拆成几步、分配给多个 AI 协作完成，不用你手工画流程图。
- **能拿来干什么**：跑复杂的多步骤任务、让多个 AI 并行/接力干活，并且每一步谁在做什么、花了多少 token 都看得见。
- **适合谁**：开发者、需要可观测多 Agent 流程的团队。
- **快速判断**：如果你要"多个 AI 协作 + 运行时自动规划"，它很合适；如果单 Agent 就够，不需要。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：无
- 理由：README 自述 "Describe the goal, not the graph. Multi-agent orchestration that runs in your own environment."。

## 项目方向与定位

与"固定流程图"相反：运行时根据目标动态规划任务 DAG（有向无环图），支持任意 LLM，强调可观测性、可靠性与安全。npm 包 `@open-multi-agent/core`，自带 Run Viewer 回放（任务 DAG + span waterfall、状态/负责人/token/工具调用）。

## 主要功能（能做什么）

- 目标驱动的多 Agent 编排：动态规划 DAG，无需预设 agent 图
- 任意 LLM 接入；自己的环境里运行
- 可观测性：Run Viewer 可视化任务 DAG 与执行瀑布
- 可靠性/安全设计（CI + codecov，文档完善）

## 架构设计

```text
packages/   核心（@open-multi-agent/core 等）
docs/       文档站
scripts/    工具脚本
```

## 实现思路与核心逻辑

- 规划与执行分离：运行时规划器把目标拆成 DAG，执行器按依赖调度
- "not the graph"：用户给目标，规划由运行时完成，降低编排复杂度
- 观测优先：每个任务的状态/负责人/token/工具调用都可回放，便于调试与审计

## 亮点

- 6.7k stars，与帖子"多 Agent 编排"主题直接相关
- 理念清晰（目标驱动 vs 固定图），差异化明显
- TypeScript 生态、npm 分发、双语文档

## 局限与风险（可选）

- 项目相对年轻，生态与生产案例待验证
- 动态规划的稳定性依赖规划器质量

## 分析说明

基于 README、packages/ 结构与 CI；未运行框架，未细读 core 源码。
