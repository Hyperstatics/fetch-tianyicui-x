# bytedance/deer-flow 分析报告

- 仓库：[bytedance/deer-flow](https://github.com/bytedance/deer-flow)
- 方向：开源 "super agent harness"——编排子代理、记忆与沙箱完成复杂任务
- 主要语言：Python（backend，LangGraph）+ Node.js（frontend）
- 指标：⭐ 79,136 · License MIT · 最近推送 2026-08-03
- 主页/文档：[deerflow.tech](https://deerflow.tech)

> 分析基于 2026-08-04 抓取的 README、backend/frontend 目录结构与配置。

## 这是什么（非技术版）

- **这是什么**：一个"AI 总指挥系统"。它不是单个聊天机器人，而是把多个 AI 分工（有的负责研究、有的负责执行）、配上记忆和隔离沙箱，协同完成一项大任务。
- **能拿来干什么**：自动做深度调研、写报告、跑自动化流程；通过"技能"（skills）扩展它能干的事。
- **适合谁**：开发者、研究团队、想用 AI 跑复杂多步骤任务的人。
- **快速判断**：如果你需要"多个 AI 协作 + 长任务 + 可扩展技能"的工作流底座，它很合适；如果只是单轮对话，用普通聊天工具就行。

## 分类

- 主分类：3. 多 Agent 编排 / 协作系统
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "super agent harness that orchestrates sub-agents, memory, and sandboxes"。

## 项目方向与定位

DeerFlow 2.0 是**从零重写**的超级 Agent Harness（与 1.x 深研框架无代码共享）。定位：给 Agent 提供可编排的运行时底座——子代理、记忆、沙箱、可扩展技能，让 Agent "做几乎所有事"。字节跳动出品，2026-02-28 登上 GitHub Trending #1。

## 主要功能（能做什么）

- 子代理（sub-agents）编排与协作
- 记忆系统 + 沙箱执行环境
- 可扩展 skills 体系
- 集成 InfoQuest（智能搜索与爬取工具集）
- Docker / 本地两种部署；官方姊妹项目 LLM Space（harness 调试/回放/评测）
- 推荐搭配 Doubao-Seed-2.0-Code、DeepSeek v3.2、Kimi 2.5 等模型

## 架构设计

```text
backend/   Python（pyproject.toml, langgraph.json → LangGraph 编排）
  packages/  核心包
  app/       应用入口
  samples/   示例
frontend/  前端界面
contracts/  契约/协议定义
docker/ deploy/  部署
docs/ plans/     文档与规划
```

## 实现思路与核心逻辑

- 以 LangGraph 作为编排内核（`backend/langgraph.json`），用图结构表达多 Agent 工作流
- "harness" 思维：把记忆、沙箱、技能等横切能力做成可插拔组件，Agent 只负责决策
- 2.0 完全重写：v1 的 Deep Research 能力保留在 `main-1.x` 分支，主开发线转向通用 harness
- 商业化生态：字节云（Volcengine）编码计划、InfoQuest 等配套服务直接集成

## 亮点

- 字节背书 + GitHub Trending #1，社区规模大、多语言文档全
- 生态配套好：LLM Space 调试工具、InfoQuest 搜索工具集、官方模型推荐
- 单仓库即"可运行的产品"：Docker 部署、前端界面、示例齐全

## 局限与风险（可选）

- 2.0 重写时间短，接口与稳定性仍在快速变化
- 生产部署有资源门槛（README 提供部署 sizing 建议）
- 与字节云服务（Volcengine/InfoQuest）有一定生态绑定倾向

## 分析说明

基于 README、backend 结构、langgraph 配置与文档；未运行代码，未细读全部 backend 源码。
