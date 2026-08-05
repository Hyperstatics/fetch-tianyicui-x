# zhuzhaoyun/Molio 分析报告

- 仓库：[zhuzhaoyun/Molio](https://github.com/zhuzhaoyun/Molio)
- 方向：本地优先工作台——把 AI 运行时接进 Obsidian 知识库
- 主要语言：TypeScript
- 指标：⭐ 94 · License 修改版 Apache-2.0（商用需商业许可）· 最近推送 2026-08-03
- 主页/文档：[molio.cn](https://molio.cn)

> 分析基于 2026-08-06 抓取的 README、apps/ 与 LICENSE。⚠️ Molio 采用修改版 Apache-2.0（类似 Yao），商用需取得商业许可。

## 这是什么（非技术版）

- **这是什么**：一个"懂你知识库的 AI 工作台"。把 Claude Code、Codex 等 AI 运行时接进你的 Obsidian 笔记库：它们读取你积累的资料，研究、分析、创作，再把结果写回笔记库；越用越懂你，数据全在本地。
- **能拿来干什么**：个人知识管理 + AI 协作、研究/创作工作流。
- **适合谁**：Obsidian 用户、知识工作者。
- **快速判断**：如果你是 Obsidian 重度用户，它很对路；否则普通 AI 工具即可。

## 分类

- 主分类：4. 记忆 / 上下文 / 知识管理
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "plugs Claude Code, Codex, and other AI runtimes into your Obsidian vault... Everything runs on your machine, never through a third-party server."。

## 项目方向与定位

本地优先工作台：以 Obsidian vault 为数据源与落点，AI 基于你的积累干活并写回；第三方服务器不参与。Docker 部署。

## 主要功能（能做什么）

- 接入 Claude Code/Codex 等 AI 运行时
- 读取/写入 Obsidian vault
- 本地优先、Docker 部署

## 架构设计

```text
apps/         应用
docker-compose.yml / Dockerfile
```

## 实现思路与核心逻辑

- 以个人知识库为上下文：AI 从你的积累出发
- 闭环写回：产出沉淀进 vault

## 亮点

- 94 stars，知识库 + Agent 组合有差异化
- 本地优先、数据自有

## 局限与风险（可选）

- **修改版 Apache-2.0**：商用需商业许可（列入本地 backlog）
- 依赖 Obsidian 生态

## 分析说明

基于 README、apps/ 与 LICENSE；未运行。
