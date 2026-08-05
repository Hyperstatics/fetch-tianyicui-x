# maka-agent/maka-agent 分析报告

- 仓库：[maka-agent/maka-agent](https://github.com/maka-agent/maka-agent)
- 方向：本地优先的 Agent 工作台（Desktop/TUI/CLI/Headless 四入口）
- 主要语言：TypeScript
- 指标：⭐ 1,210 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[ARCHITECTURE.md](https://github.com/Maka-Agent/maka-agent/blob/main/ARCHITECTURE.md)

> 分析基于 2026-08-06 抓取的 README、ARCHITECTURE.md 与目录结构。

## 这是什么（非技术版）

- **这是什么**：一个"本地优先的 AI 工作台"。AI 可以在受控权限下检查项目、执行工具、产出文件；所有消息、工具调用、任务进度都作为可恢复的执行记录保存，断点续跑。
- **能拿来干什么**：日常 Agent 交互（桌面）、终端/无头跑长任务（TUI/CLI/Headless）、任务回放与评测。
- **适合谁**：开发者、需要"可恢复、可审计"长任务的人。
- **快速判断**：如果你要"日志即运行时"式的可靠 Agent 底座，它很有参考价值；如果只要简单聊天，功能过剩。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（本地优先工作台）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "A local-first Agent workspace built for real work... Log is the Runtime"。

## 项目方向与定位

以"执行事实（recoverable execution facts）"为核心的 Agent 工作台：模型消息、工具调用、结果与终止事实进入 Runtime Event Log，会话/UI/上下文/恢复都是日志的投影。四个入口（Desktop/TUI/CLI/Headless）共享同一运行时，面向真实工作和 durable task。

## 主要功能（能做什么）

- 受控权限下检查项目、执行工具、产出 artifacts
- 会话/分支/搜索/恢复；工具时间线
- `maka run` 单轮无交互执行；`maka eval` 评测与任务导出/恢复/对比
- TaskRun + Task Event Log + budgets + continuation（任务可活过单个 Turn）
- 本地优先：会话/设置/运行记录默认留在本机

## 架构设计

```text
apps/        桌面端（Electron + React）
packages/    共享核心（Runtime、事件日志、任务）
ARCHITECTURE.md / DESIGN.md
```

## 实现思路与核心逻辑

- 事件日志作为唯一事实源（Event Sourcing 风格），UI/上下文/恢复都是投影
- "Context is not history"：工具结果裁剪与 LLM 压缩改变下次推理输入，但不删除记录证据
- "Feedback is not fact authority"：自我检查只产生证据与一次有界修复机会，不直接成为系统事实

## 亮点

- "Log is the Runtime" 的设计哲学清晰，工程文档（ARCHITECTURE）质量高
- 四入口共享运行时，覆盖日常到无头评测全场景
- durable TaskRun 是对"长任务"问题的正面回答

## 局限与风险（可选）

- README 自述 active development，数据格式/CLI 可能变化
- macOS Apple Silicon 桌面为早期公开版

## 分析说明

基于 README、ARCHITECTURE 与目录结构；未运行。
