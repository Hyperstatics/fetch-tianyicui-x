# CJackHwang/SunamAI 分析报告

- 仓库：[CJackHwang/SunamAI](https://github.com/CJackHwang/SunamAI)
- 方向：浏览器中运行的开源 AI 编程助手（WebContainer 隔离）
- 主要语言：TypeScript
- 指标：⭐ 5 · License AGPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/CJackHwang/SunamAI)

> 分析基于 2026-08-06 抓取的 README、docs/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"跑在浏览器里的 AI 编程助手"。通过 OpenAI 兼容 API 接模型，用 WebContainer 在浏览器内提供隔离文件系统、终端、进程和本地服务预览。
- **能拿来干什么**：浏览器内 AI 编程、资源分析、文件编辑、命令执行。
- **适合谁**：开发者、想要"免安装浏览器工作区"的人。
- **快速判断**：如果你喜欢"浏览器里跑 Agent 工作区"，它很前沿；否则桌面更稳。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述"运行在浏览器中的开源 AI 编程助手……WebContainer 在浏览器内提供隔离文件系统、终端、进程和本地服务预览"。

## 项目方向与定位

浏览器内 Agent 工作区：BYO 模型（OpenAI-compatible）、WebContainer 隔离、可恢复文件快照；不提供模型服务/账号/托管。

## 主要功能（能做什么）

- OpenAI 兼容模型接入（/models 列表）
- 浏览器内文件/终端/进程/端口服务
- 可恢复文件快照

## 架构设计

```text
docs/ index.html
```

## 实现思路与核心逻辑

- WebContainer 承担执行与隔离
- BYO 模型：无厂商绑定

## 亮点

- 5 stars，浏览器 Agent 工作区前沿
- AGPL-3.0 开源

## 局限与风险（可选）

- **AGPL-3.0**：派生分发需遵守 copyleft
- 浏览器端性能/能力受限

## 分析说明

基于 README、docs/ 与文档；未运行。
