# tt-a1i/archify 分析报告

- 仓库：[tt-a1i/archify](https://github.com/tt-a1i/archify)
- 方向：Agent 技能——把代码库/系统描述变成可交互的系统架构地图
- 主要语言：HTML/TypeScript（输出为自包含 HTML 资产）
- 指标：⭐ 8,809 · License MIT · 最近推送 2026-08-03
- 主页/文档：[项目页](https://tt-a1i.github.io/archify/) · [场景指南](https://tt-a1i.github.io/archify/guide.html)

> 分析基于 2026-08-04 抓取的 README、DESIGN.md、PRODUCT.md 与目录结构。当前稳定版 v2.13.0。

## 这是什么（非技术版）

- **这是什么**：一个给 AI 用的"画架构图技能"。你让 AI"把项目的架构画出来"，它直接生成一份可以点开、搜索、演示的交互式系统地图（网页文件），还能做版本对比。
- **能拿来干什么**：新成员看懂系统、评审架构变更（合并前对比 Before/Delta/After）、做技术分享和文档。
- **适合谁**：架构师、技术负责人、开发者；搭配 Claude Code / Cursor / Codex / Raven / OpenCode 使用。
- **快速判断**：如果你经常要"给别人讲清楚系统长什么样"，它很好用；如果只是个人小项目，用不上。

## 分类

- 主分类：6. 特定领域 / 其他（架构可视化 Agent 技能）
- 副分类：2. Coding Harness / 工程向 Agent（依附编码 Agent 执行）
- 理由：README 自述 "agent skill for Raven, Cursor, Claude Code, Codex CLI, and OpenCode"。

## 项目方向与定位

把"架构文档/代码库"转化为**可交互、可信任、可分享**的系统地图：5 种技术图类型、4 种视觉预设、深色/浅色主题、可选的有限动效；核心卖点是"grounded"——所有拓扑都来自真实来源，不臆造。定位是 Agent 时代的架构可视化基础设施，而非 Harness 本身。

## 主要功能（能做什么）

- 从代码库或系统描述生成交互式系统地图（搜索节点、打开修订校验过的源码、追踪上游/下游）
- 架构变更评审：两个校验快照做 Before / Delta / After 对比（新增/删除/修改/移动/重路由）
- 输出自包含 HTML + PNG / SVG / WebM / 1200×630 分享卡片
- 支持 Raven / Cursor / Claude Code / Codex CLI / OpenCode；`npx skills add tt-a1i/archify -g` 安装

## 架构设计

```text
archify/        技能核心（生成管道）
benchmarks/     评测
examples/       示例
experiments/    实验
docs/ DESIGN.md / PRODUCT.md / ROADMAP.md  产品与设计文档
```

## 实现思路与核心逻辑

- 类型化 JSON IR + 确定性检查生成自包含 HTML：同一份图可导出多种格式
- 快照对比机制：两次校验快照做增量 diff，支持架构变更评审
- "不臆造拓扑"：节点可打开修订校验过的源码，交互行为 grounded 在真实来源

## 亮点

- 8.8k stars，架构可视化 Agent 技能赛道头部
- 变更评审场景（Before/Delta/After）贴近真实工程痛点
- EverMind Raven 官方赞助集成；稳定版 v2.13.0、版本节奏快

## 局限与风险（可选）

- 是"技能"而非 Harness，需要宿主 Agent 才能运行
- 与"Agent Harness 内测"主题相关度低
- 产出依赖宿主模型理解质量

## 分析说明

基于 README、DESIGN/PRODUCT 文档与目录结构；未运行技能。
