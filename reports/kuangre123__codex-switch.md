# kuangre123/codex-switch 分析报告

- 仓库：[kuangre123/codex-switch](https://github.com/kuangre123/codex-switch)
- 方向：macOS 工具——一键切换 Codex 官方/自定义 API，对话记录不丢
- 主要语言：Python
- 指标：⭐ 58 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/kuangre123/codex-switch)

> 分析基于 2026-08-06 抓取的 README、app/src 与文档。

## 这是什么（非技术版）

- **这是什么**：一个小的 macOS 应用。把手改 Codex 配置文件（auth.json/config.toml）变成一次点击：在官方 OpenAI 和你的自定义/第三方 API 之间切换，已保存的对话记录不会丢。
- **能拿来干什么**：Codex 接入第三方/国内模型、快速切换 provider。
- **适合谁**：Codex 用户、想用自定义 API 的开发者。
- **快速判断**：如果你用 Codex 且想一键切换模型商，它很实用；否则不需要。

## 分类

- 主分类：6. 特定领域 / 其他（工具类）
- 副分类：2. Coding Harness / 工程向 Agent（Codex 配置管理）
- 理由：README 自述"一键把 Codex 在官方 OpenAI 和你自己的自定义/第三方 API 之间切换，切换后对话记录始终都在"。

## 项目方向与定位

解决 Codex provider 切换痛点：官方与自定义 provider 同时保留在配置，切换只改默认路由；内置国内主流大模型预设；本地 adapter 桥接 Chat-Completions → Responses 协议。

## 主要功能（能做什么）

- 一键切换 Codex provider（官方/自定义）
- 对话记录保留（不重写归属）
- 国内模型预设 + Chat→Responses 协议桥接
- DMG 分发

## 架构设计

```text
app/ src/ bin/
scripts/ tests/
```

## 实现思路与核心逻辑

- 配置双轨保留：切换只改"默认路由"，不重写历史归属
- 本地 adapter 做协议转换

## 亮点

- 58 stars，解决真实痛点（配置切换）
- MIT 开源 + 中英双语

## 局限与风险（可选）

- 仅 macOS
- 与"Agent Harness 内测"主题相关度低

## 分析说明

基于 README、app/src 与文档；未运行。
