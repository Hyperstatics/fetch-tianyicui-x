# proma-ai/Proma 分析报告

- 仓库：[proma-ai/Proma](https://github.com/proma-ai/Proma)
- 方向：本地优先的 AI 桌面应用（多模型 Chat + Agent 工作台）
- 主要语言：TypeScript
- 指标：⭐ 1,895 · License AGPL-3.0 · 最近推送 2026-08-05
- 主页/文档：[proma.cool](https://proma.cool) · [新手教程](https://github.com/proma-ai/Proma/blob/main/tutorial/tutorial.md)

> 分析基于 2026-08-04 抓取的 README、apps/packages 结构与文档。许可证 AGPL-3.0（开源版）；另有商业版。

## 这是什么（非技术版）

- **这是什么**：一个"本地优先的 AI 工作台"。简单问题用 Chat 聊，复杂任务交给 Agent 干；工作区、Skills、MCP、远程机器人（飞书/钉钉/微信）和记忆都在一个客户端里。
- **能拿来干什么**：长期沉淀个人工作流；用手机/群聊远程触发电脑上的 Agent 干活。
- **适合谁**：喜欢桌面 AI 客户端、注重本地数据的个人与团队。
- **快速判断**：如果你想要"Chat + Agent + 远程 IM 触发"一体化且数据留本地，它很合适；如果只是偶尔聊天，功能过剩。

## 分类

- 主分类：1. 通用 Agent 桌面 / 客户端 / Runtime
- 副分类：2. Coding Harness / 工程向 Agent（内置 Claude/Pi Agent SDK）
- 理由：README 自述"本地优先的 AI 桌面应用，把多模型 Chat、通用 Agent、工作区、Skills、MCP、远程机器人和记忆能力放在同一个开源客户端里"。

## 项目方向与定位

"不是只面向闲聊的聊天框，而是长期沉淀个人工作流的 Agent 工作台"：简单问题 Chat、复杂任务 Agent；内置 Claude Agent SDK 与 Pi Agent SDK 两套运行时；本地优先（`~/.proma/` JSON/JSONL 存储，不依赖数据库）。开源版与商业版并行。

## 主要功能（能做什么）

- Chat 模式：多模型对话、附件/图片、Markdown/Mermaid/代码高亮、上下文管理
- Agent 模式：Claude / Pi 双运行时、工作区隔离、权限模式、长任务流式输出、计划确认
- 协作：复杂任务拆分子 Agent / Task，消息流中可视化调用过程
- Skills / MCP / 项目根目录独立配置
- 远程机器人：飞书/Lark 桥接 + 钉钉/微信入口
- 记忆共享、联网搜索、桌面体验（自动更新/快捷键/语音输入/主题）

## 架构设计

```text
apps/          桌面应用（macOS/Windows）
packages/      共享包（Chat/Agent/Skills/MCP/记忆）
index.ts       入口
proma-thinking/ 产品思考文档
docs/ tutorial/ release-notes/
```

## 实现思路与核心逻辑

- 双运行时内核：Claude Agent SDK（默认）+ Pi Agent SDK（实验），降低单内核依赖
- 本地优先：会话/工作区/附件/配置全部本地 JSON/JSONL，可迁移
- 远程桥接：IM 机器人把手机/群聊接到本机 Agent，形成"随身工作流"

## 亮点

- 1.9k stars，与帖子"本地优先 Agent 客户端"类别直接相关
- 双 Agent 运行时 + 远程 IM 桥接组合完整
- 产品思考文档（proma-thinking）体现长期主义

## 局限与风险（可选）

- **AGPL-3.0**：开源版派生需遵守 copyleft；商业功能在商业版
- 桌面客户端赛道竞争激烈（Kun/DeepChat/CodePilot 等）

## 分析说明

基于 README、apps/packages 结构与文档；未运行应用。
