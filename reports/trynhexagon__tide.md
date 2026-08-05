# trynhexagon/tide 分析报告

- 仓库：[trynhexagon/tide](https://github.com/trynhexagon/tide)
- 方向：飞书工作流的本地第二大脑（会话流→工作流）
- 主要语言：JavaScript/TypeScript
- 指标：⭐ 5 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/trynhexagon/tide)

> 分析基于 2026-08-06 抓取的 README、backend/frontend 与文档。

## 这是什么（非技术版）

- **这是什么**：潮汐（Tide）——飞书/钉钉工作流的本地第二大脑。把导出的聊天流转成日报、任务、风险、跨聊主题、关系图和主题演化视图；不是摘要器，而是把"会话流"重组成"工作流"。
- **能拿来干什么**：飞书工作信息整理、跨群上下文聚合。
- **适合谁**：飞书重度用户、团队。
- **快速判断**：如果你在飞书里信息分散，它很有价值；否则不需要。

## 分类

- 主分类：4. 记忆 / 上下文 / 知识管理（工作流重组）
- 副分类：6. 特定领域 / 其他（飞书生态）
- 理由：README 自述 "a local-first, multi-agent work assistant for Lark/Feishu... turns exported chat streams into daily briefs, tasks, risks, cross-chat topics, relation graphs"。

## 项目方向与定位

本地优先多 Agent 工作助手：日报、任务、风险、跨聊主题、关系图、主题演化；frontend + backend + docker。

## 主要功能（能做什么）

- 日报/任务/风险汇总
- 跨聊主题、关系图、主题演化
- 多 Agent 工作流

## 架构设计

```text
backend/ frontend/
docker-compose.yml
```

## 实现思路与核心逻辑

- 会话流→工作流重组：按项目/主题/任务/决策/风险组织
- 本地优先：数据不出机器

## 亮点

- 5 stars，飞书垂直工具
- 工作流视角差异化
- Apache-2.0

## 局限与风险（可选）

- 依赖飞书导出数据
- 与"内测 Harness"主题相关度低

## 分析说明

基于 README、backend/frontend 与文档；未运行。
