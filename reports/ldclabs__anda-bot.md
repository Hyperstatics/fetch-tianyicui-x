# ldclabs/anda-bot 分析报告

- 仓库：[ldclabs/anda-bot](https://github.com/ldclabs/anda-bot)
- 方向：终端 Rust AI Agent + 知识图谱记忆（Anda Brain）
- 主要语言：Rust
- 指标：⭐ 22 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/ldclabs/anda-bot)

> 分析基于 2026-08-06 抓取的 README、anda_bot/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"记得住事的终端 AI"。核心是 Anda Brain 记忆引擎：把对话变成活的认知图谱（人、项目、偏好、事件、决策、变化的事实），跨会话推理与记忆，而不是翻聊天记录。
- **能拿来干什么**：长期目标执行、跨会话记忆的终端助手。
- **适合谁**：开发者、想要"真记忆" Agent 的人。
- **快速判断**：如果你受够了"AI 每次忘光"，它很有价值；否则普通终端 Agent 即可。

## 分类

- 主分类：4. 记忆 / 上下文 / 知识管理（知识图谱记忆）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "Its primary differentiator is Anda Brain, the memory engine... a graph of people, projects, preferences, events, decisions, and changing facts."。

## 项目方向与定位

Rust 终端 Agent：图谱长期记忆（Anda Brain）、跨会话推理、长程目标、工具（Claude Code/Codex/shell/文件/笔记/任务/skills/cron）、子代理协作、持续改进。

## 主要功能（能做什么）

- 知识图谱长期记忆（Anda Brain）
- 自主提炼与上下文构建、长程执行
- 工具集成（Claude Code/Codex/shell/文件/任务/cron）
- chrome 扩展、docsite

## 架构设计

```text
anda_bot/      核心
chrome-extension/ docsite/
```

## 实现思路与核心逻辑

- 图谱而非日志：结构化记忆支持推理
- 自主蒸馏：从过往工作中提炼关键洞察
- 长程目标：跨压缩会话持续

## 亮点

- 22 stars，记忆引擎差异化（与帖子"记忆"类别契合）
- Rust 实现 + 工具丰富
- Apache-2.0

## 局限与风险（可选）

- 生态较新
- 图谱质量依赖提炼算法

## 分析说明

基于 README、anda_bot/ 与文档；未运行。
