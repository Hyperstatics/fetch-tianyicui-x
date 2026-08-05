# zqiren/Orbital 分析报告

- 仓库：[zqiren/Orbital](https://github.com/zqiren/Orbital)
- 方向：The project agent——以本地文件夹为长期项目的 Agent
- 主要语言：Python
- 指标：⭐ 128 · License GPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/zqiren/Orbital)

> 分析基于 2026-08-06 抓取的 README、agent_os/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"把项目当长期记忆"的 Agent。普通 AI 会话一关就忘，Orbital 会把项目当前状态、决策、教训、任务队列和产出持续写进本地文件夹，下一次任务从上次的上下文接着来；还能派 Claude Code/Codex 等干活并回收结果。
- **能拿来干什么**：长期项目研究/规划/执行，让 AI 工作"复利式积累"。
- **适合谁**：开发者、需要跨会话延续的 Agent 重度用户。
- **快速判断**：如果你受够了"每次都要重新给 AI 讲项目"，它很对口；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（项目级长期运行）
- 副分类：3. 多 Agent 编排 / 协作系统（派发 CLI agents）
- 理由：README 自述 "Every agent owns a session. Orbital owns the project."。

## 项目方向与定位

以"项目"而非"会话"为单元：文件夹内维护状态/决策/教训/任务队列/产物；新任务基于历史上下文启动；可派发 Claude Code、Codex、Gemini CLI、Cursor 等，派发时自动带项目上下文，运行后把结果写回项目。

## 主要功能（能做什么）

- 项目状态/决策/教训/任务队列/artifact 持久化
- 派发外部 CLI agents（Claude Code/Codex/Gemini/Cursor）
- 研究、规划、写命令、浏览网页、操作工具

## 架构设计

```text
agent_os/      核心
installer/ docs/ assets/
```

## 实现思路与核心逻辑

- 项目上下文即真相：一切积累写回文件夹，跨会话可用
- 派发+回收：外部 CLI agent 做重活，Orbital 负责编排与上下文

## 亮点

- 128 stars，"project agent"理念与长期任务趋势契合
- 与帖子主题（Harness/长期工作）直接相关
- 中文/英文双语

## 局限与风险（可选）

- **GPL-3.0**：派生分发需遵守 copyleft
- 依赖外部 CLI agents 能力

## 分析说明

基于 README、agent_os/ 与文档；未运行。
