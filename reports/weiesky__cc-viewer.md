# weiesky/cc-viewer 分析报告

- 仓库：[weiesky/cc-viewer](https://github.com/weiesky/cc-viewer)
- 方向：基于 Claude Code 的 Vibe Coding 工具（蒸馏积累真实开发经验）
- 主要语言：JavaScript
- 指标：⭐ 1,056 · License MIT · 最近推送 2026-08-03
- 主页/文档：[cc-viewer 官网](https://weiesky.github.io/cc-viewer/)

> 分析基于 2026-08-06 抓取的 README、cli.js/plugins 结构与文档。

## 这是什么（非技术版）

- **这是什么**：一个"AI 编程经验积累器"。在 Claude Code 上增强：每次开发中的经验会被蒸馏、沉淀下来复用，越用越懂你的项目；还能把配置一键分享到多台设备。
- **能拿来干什么**：日常 vibe coding；沉淀团队/个人开发经验；统一多设备配置。
- **适合谁**：Claude Code 用户、想积累"开发经验资产"的人。
- **快速判断**：如果你用 Claude Code 且觉得"每次都要重新教"，它很对口；不用 Claude Code 则用不上。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent（Claude Code 增强）
- 副分类：4. 记忆 / 上下文 / 知识管理（经验蒸馏）
- 理由：README 自述 "Based on Claude Code, a Vibe Coding tool that distills and accumulates real development experience"。

## 项目方向与定位

给 Claude Code 加"经验层"：把真实开发过程蒸馏为可复用经验，配置与经验跨设备同步。npm / Homebrew 分发，18 种语言文档，electron 桌面端（cc-viewer 应用）。

## 主要功能（能做什么）

- 开发经验蒸馏与积累（concepts/ 概念库）
- 一键部署、跨设备分享配置
- npm / Homebrew 安装、Electron 桌面端
- 插件体系、CLI（cli.js）

## 架构设计

```text
cli.js / findcc.js   CLI 入口
concepts/           经验/概念库
plugins/            插件
electron/           桌面端（electron-builder.yml）
homebrew/           分发
```

## 实现思路与核心逻辑

- "经验即资产"：把开发中验证过的做法结构化沉淀，跨会话复用
- Claude Code 生态内增强，不另起炉灶
- 多端分发（npm/Homebrew/桌面）降低使用门槛

## 亮点

- 1.1k stars，经验蒸馏角度在 Claude Code 生态中独特
- 18 语言文档，国际化为开源项目少见的投入
- 安装方式多样（npm/Homebrew/桌面）

## 局限与风险（可选）

- 强依赖 Claude Code 生态
- 经验复用质量取决于蒸馏规则
- 与"Agent Harness 内测"主题相关度低（偏经验工具）

## 分析说明

基于 README、cli/plugins 结构与文档；未运行。
