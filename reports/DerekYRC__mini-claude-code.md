# DerekYRC/mini-claude-code 分析报告

- 仓库：[DerekYRC/mini-claude-code](https://github.com/DerekYRC/mini-claude-code)
- 方向：简化版 Java Claude Code——理解编码 Agent 核心原理
- 主要语言：Java
- 指标：⭐ 174 · License 未见 LICENSE 文件（需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/DerekYRC/mini-claude-code)

> 分析基于 2026-08-06 抓取的 README、src/ 与 changelog。⚠️ 仓库目录未见 LICENSE 文件，使用前需确认授权。

## 这是什么（非技术版）

- **这是什么**：一个"教学用迷你 Claude Code"。用 Java 实现 Agent Harness 的关键机制（Agent Loop、工具调用、权限、Hooks、Todo、Subagent、技能加载、上下文压缩、记忆、任务、多 Agent 协作、MCP 插件），代码精简、按章节分分支，帮你快速看懂编码 Agent 原理。
- **能拿来干什么**：学习 Agent 内部机制、作为教学/参考实现。
- **适合谁**：Java 开发者、想理解 Agent Harness 的人。
- **快速判断**：如果你想"看懂编码 Agent 怎么实现的"，它是极佳教材；否则直接产品化 Agent 用。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent（教学向）
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述"简化版的 Java 版 Claude Code 编程 Agent 项目，能帮助你快速理解编码 Agent 的核心原理……抽取了 Agent Harness 的关键机制"。

## 项目方向与定位

作者 mini-spring 系列的教学延伸：按章节拆解编码 Agent 核心机制，每章独立分支、保留最小代码。覆盖 Agent Loop、工具、权限、Hooks、Todo、Subagent、Skill、上下文压缩、记忆、任务、定时调度、多 Agent、团队协议、自主认领任务、MCP Plugin。

## 主要功能（能做什么）

- Agent Loop、工具调用、权限控制、Hooks、Todo
- Subagent、Skill Loading、上下文压缩、记忆、任务系统
- 后台任务、定时调度、多 Agent 协作、团队协议、MCP Plugin

## 架构设计

```text
src/          分章节实现
skills/       技能
pom.xml / changelog.md（分步教程）
```

## 实现思路与核心逻辑

- "减法教学"：每章一个机制，分支对应章节
- 保留最小可运行代码，降低理解成本

## 亮点

- 174 stars，Java 生态理解 Agent 的稀缺教材
- 覆盖机制全（Loop/工具/权限/记忆/多 Agent/MCP）
- 与 mini-spring 系列构成完整教学路径

## 局限与风险（可选）

- **未见 LICENSE 文件**：使用/分发前需确认（已列入本地 backlog）
- 教学项目，非生产级

## 分析说明

基于 README、src/ 与 changelog；未编译运行。
