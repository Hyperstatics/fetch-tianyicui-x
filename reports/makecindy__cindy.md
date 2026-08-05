# makecindy/cindy 分析报告

- 仓库：[makecindy/cindy](https://github.com/makecindy/cindy)
- 方向：开箱即用的开源 AI Agent（多 Harness 混用，桌面 + 移动客户端）
- 主要语言：TypeScript（pnpm monorepo，React Native/Electron）
- 指标：⭐ 1,779 · License Apache-2.0 · 最近推送 2026-08-05
- 主页/文档：[cindy.app](https://cindy.app)

> 分析基于 2026-08-06 抓取的 README、apps/ 结构与设计文档。

## 这是什么（非技术版）

- **这是什么**：一个"装好就能用的 AI Agent 客户端"。把 Claude Code、Codex 等多种 AI 引擎和模型装进一个应用，让它直接用你电脑上的真实文件和已登录的应用干活；做任务时还能让不同引擎/模型分工并行。
- **能拿来干什么**：日常让 AI 改代码、操作浏览器/电脑/手机；通过 IM 和日程触发任务。
- **适合谁**：开发者、想用"多引擎混合 Agent"的个人和团队。
- **快速判断**：如果你想"一个客户端统一多个 AI 引擎、任务可并行分工"，它很有代表性；如果只用一个引擎，官方客户端就行。

## 分类

- 主分类：1. 通用 Agent 桌面 / 客户端 / Runtime
- 副分类：3. 多 Agent 编排 / 协作系统（多引擎并行执行/审查）
- 理由：README 自述 "brings multiple harnesses, models and tools into one agent... one task can even be planned, executed in parallel, and reviewed by agents on different harness × model combos"。

## 项目方向与定位

"Consider it done."——开箱即用的开源 Agent 客户端：首个支持 Claude Code 与 Codex 两套 harness，模型与 harness 可自由混合、任务中途切换；工作区/记忆/skills/工具跨引擎连续。桌面 + 移动客户端（pnpm monorepo），原生 harness 开发中。

## 主要功能（能做什么）

- 多 harness（Claude Code / Codex）+ 多模型混用，任务中可切换
- 任务级并行：规划/执行/审查可由不同 harness × model 组合承担
- 驱动浏览器、电脑、手机；IM 与日程触发
- 桌面与移动客户端、共享包 monorepo

## 架构设计

```text
apps/          桌面/移动客户端
（根）packages/ 共享代码（pnpm workspace）
DESIGN.md REVIEW.md SECURITY.md  设计、评审与安全文档
```

## 实现思路与核心逻辑

- 以"引擎无关"为核心抽象：Claude Code/Codex 等作为可插拔 harness，模型同理
- 跨引擎连续性：工作区/记忆/skills/工具不随引擎切换而丢失
- 并行任务：同一任务由不同引擎组合规划/执行/审查，发挥各自优势

## 亮点

- 1.8k stars，多引擎混用的桌面/移动 Agent 客户端定位独特
- "开箱即用 + 可塑形"的产品理念清晰
- 工程规范完整（DCO、REVIEW、SECURITY、多语言文档）

## 局限与风险（可选）

- 多引擎混用增加复杂性与不一致风险
- 依赖 Claude Code/Codex 等宿主引擎的稳定性
- 客户端竞争激烈，需持续迭代

## 分析说明

基于 README、apps/ 结构与设计文档；未运行客户端。
