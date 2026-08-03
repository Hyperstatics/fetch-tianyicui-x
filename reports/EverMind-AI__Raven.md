# EverMind-AI/Raven 分析报告

- 仓库：[EverMind-AI/Raven](https://github.com/EverMind-AI/Raven)
- 方向：The Self-Improving Agent Harness（自我改进的 Agent Harness）
- 主要语言：Python
- 指标：⭐ 3,494 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[raven.evermind.ai](https://raven.evermind.ai)

> 分析基于 2026-08-04 抓取的 README、目录结构与文档。

## 这是什么（非技术版）

- **这是什么**：一个"会越用越强的 AI 工作台"。每次跑完任务，它会自动改进周围的工具、技能、记忆、策略和执行环境，把成功的流程沉淀成可复用模板。
- **能拿来干什么**：长跑型 Agent 任务、深度调研（Deep Research）、把工作流固化为"数字员工"。
- **适合谁**：重度 Agent 用户、研究者、想搭建自我进化工作流的团队。
- **快速判断**：如果你想要"跨会话持续变强"的 Agent 底座，它很对口；如果单次对话就够，不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（自我改进型 Harness）
- 副分类：4. 记忆 / 上下文 / 知识管理（EverOS 记忆）
- 理由：README 自述 "Raven is The Self-Improving Agent Harness, built on EverOS"。

## 项目方向与定位

基于 EverOS（持久用户记忆/Agent 记忆/世界知识）构建的自我改进 Harness：跨会话持续优化工具、技能、记忆、代码执行、策略与工作环境；成功工作流演化为 Agent Templates 与 digital workers。可选 Deep Research（MiroThinker 支撑的多源调查）。

## 主要功能（能做什么）

- 自我改进：运行间持续优化系统组件
- Deep Research：多源深度调查（`raven deep-research enable`）
- 持久记忆（EverOS）：用户记忆 / Agent 记忆 / 世界知识
- Agent Templates：成功流程沉淀为可复用模板
- 消息网关（Messaging Gateways）、CLI 快速上手、benchmarks

## 架构设计

```text
bridge/          桥接层
benchmarks/      评测
docs/ demos/     文档与演示
AGENTS.md / CLAUDE.md / CONTEXT-MAP.md  开发规范与上下文地图
LICENSES/ NOTICES.md  许可证与声明
```

## 实现思路与核心逻辑

- 核心假设：Agent 的进步来自"系统组件的持续改进"而非单一模型
- 记忆分层：用户记忆 / Agent 记忆 / 世界知识，跨会话可用
- 模板化：把验证过的工作流固化为 Agent Template / digital worker

## 亮点

- 3.5k stars，"自我改进 Harness"理念在帖子生态中有辨识度
- EverOS 记忆底座 + Deep Research 组合完整
- 工程规范（benchmarks/CI/pre-commit、许可证清单）严谨

## 局限与风险（可选）

- 概念新颖但效果依赖长期运行验证
- 与 Archify 等技能生态绑定（EverMind 系）

## 分析说明

基于 README、目录结构与文档；未运行 Raven，未细读 bridge 源码。
