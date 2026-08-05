# tt-a1i/hive 分析报告

- 仓库：[tt-a1i/hive](https://github.com/tt-a1i/hive)
- 方向：本地多 Agent 协作工作台（浏览器界面，真实 PTY 进程）
- 主要语言：TypeScript
- 指标：⭐ 451 · License Apache-2.0（≤0.6.0-alpha.7）→ **BSL-1.1**（2030 转 Apache-2.0）· 最近推送 2026-08-03
- 主页/文档：[hivehq.dev](https://hivehq.dev)

> 分析基于 2026-08-06 抓取的 README 与 LICENSE/LICEN.BSL。注意：0.6.0-alpha.8 起采用 BSL-1.1。

## 这是什么（非技术版）

- **这是什么**：一个"多 AI 团队工作台"。让 Claude Code、Codex、Gemini、OpenCode、Qwen 等 CLI Agent 组成可见的本地团队：一个 Orchestrator 规划派活，其他 workers 实现、审查、测试、研究并汇报——都在你电脑上真实运行。
- **能拿来干什么**：多 Agent 分工协作、复杂任务流水线，避免"一堆终端窗口"。
- **适合谁**：开发者、需要多 Agent 协作的团队。
- **快速判断**：如果你觉得"一个 Agent 不够、开一堆终端太乱"，它正合适；否则不需要。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：1. 通用 Agent Runtime / Harness（PTY 运行时）
- 理由：README 自述 "Run Claude Code, Codex, Gemini, OpenCode, Qwen... as a visible local team. An Orchestrator plans and delegates while workers implement, review, test, research"。

## 项目方向与定位

本地多 Agent 协作：Orchestrator 规划委派，workers 以真实 PTY 进程执行并回报。一个浏览器工作台统一管理，替代"一个 Agent 不够、终端一堆不是工作流"的困境。npm 分发（@tt-a1i/hive）。

## 主要功能（能做什么）

- 多 CLI Agent 接入与团队化组织
- Orchestrator 规划/委派 + workers 执行/审查/测试/研究
- 浏览器工作台实时可见
- 真实 PTY 进程（非模拟）

## 架构设计

```text
bin/ 入口
（多 Agent 运行时 + PTY + 浏览器工作台）
```

## 实现思路与核心逻辑

- "可见的本地团队"：Agent 以进程形式真实运行，工作台只做编排与可视化
- Orchestrator/Worker 角色分离：规划与执行解耦

## 亮点

- 451 stars，多 Agent 编排定位清晰，与帖子主题直接相关
- 浏览器工作台降低多 Agent 管理门槛
- npm 分发，中英双语

## 局限与风险（可选）

- **BSL-1.1**：0.6.0-alpha.8 起非宽松许可，商用需评估
- PTY 多进程资源占用与稳定性需实践验证

## 分析说明

基于 README、LICENSE 与目录结构；未运行。
