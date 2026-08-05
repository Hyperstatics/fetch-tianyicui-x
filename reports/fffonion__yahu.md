# fffonion/yahu 分析报告

- 仓库：[fffonion/yahu](https://github.com/fffonion/yahu)
- 方向：Hermes Agent 的轻量 Web 界面（单二进制）
- 主要语言：TypeScript（React）+ Rust
- 指标：⭐ 15 · License 未见 LICENSE 文件（需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/fffonion/yahu)

> 分析基于 2026-08-06 抓取的 README、frontend/ 与文档。⚠️ 未见 LICENSE 文件。

## 这是什么（非技术版）

- **这是什么**：一个"Hermes Agent 的网页遥控器"。单二进制内置后端 + React 前端，指向 Hermes API Server 就能在浏览器里聊天、看会话历史、cron、记忆、技能、工作区文件和图片；不修改 Hermes 本身。
- **能拿来干什么**：给 Hermes Agent 加 Web UI。
- **适合谁**：Hermes Agent 用户。
- **快速判断**：如果你用 Hermes 且想要网页界面，它很合适；否则用不上。

## 分类

- 主分类：1. 通用 Agent 桌面 / 客户端 / Runtime（Web UI）
- 副分类：6. 特定领域 / 其他
- 理由：README 自述 "A lightweight web interface for Hermes Agent, packaged as one Rust binary with an embedded React frontend."。

## 项目方向与定位

非侵入式：通过 API Server 与 Hermes 并存，不装插件/不改数据；UI 覆盖聊天/会话/cron/记忆/技能/工作区/图库。

## 主要功能（能做什么）

- 聊天、会话历史、cron、记忆、技能、工作区、图库
- 单二进制 + 移动端适配 + 10 主题多语言
- 发布构件（GitHub Releases）

## 架构设计

```text
frontend/       React
src（Rust 二进制）
deploy/ docs/
```

## 实现思路与核心逻辑

- 单二进制嵌入式前端，部署零依赖
- 非侵入 API 集成

## 亮点

- 15 stars，Hermes 生态补位
- 单二进制 + 多语言主题

## 局限与风险（可选）

- **未见 LICENSE 文件**（列入本地 backlog）
- 强依赖 Hermes Agent

## 分析说明

基于 README、frontend/ 与文档；未运行。
