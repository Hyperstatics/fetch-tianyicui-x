# basionwang-bot/HermesPet 分析报告

- 仓库：[basionwang-bot/HermesPet](https://github.com/basionwang-bot/HermesPet)
- 方向：住进 MacBook 刘海的 AI 桌宠 + 多终端可观察控制面
- 主要语言：TypeScript（原生 macOS 应用）
- 指标：⭐ 592 · License 无许可证文件（谨慎使用）· 最近推送 2026-08-03
- 主页/文档：[hermespet.cc](https://hermespet.cc)

> 分析基于 2026-08-06 抓取的 README、client/drizzle 结构。⚠️ 仓库未发现 LICENSE 文件（GitHub 显示无许可证），默认保留所有权利，使用前需注意。

## 这是什么（非技术版）

- **这是什么**：一个住在 MacBook 刘海里的 AI 桌宠。它同时把 7 类 AI 终端接入同一块"控制面"，显示系统遥测、支持多任务并行，手机配套端开发中。
- **能拿来干什么**：桌面陪伴 + AI 状态可视化；统一观察多个 AI 终端。
- **适合谁**：macOS 用户、喜欢桌宠 + 控制台的开发者。
- **快速判断**：如果你想要"可爱 + 可观察"的 AI 桌宠控制面，它很有特色；**注意无许可证，商用/分发需谨慎**。

## 分类

- 主分类：1. 通用 Agent 桌面 / 客户端 / Runtime（桌宠/控制面）
- 副分类：6. 特定领域 / 其他（系统遥测可视化）
- 理由：README 自述"让 AI 住进 MacBook 的刘海，也让不同 AI 终端进入同一块可观察的控制面"。

## 项目方向与定位

原生 macOS AI 桌宠 + 任务控制面：7 类 AI 终端接入、实时系统诊断、多任务并行、手机配套端规划。Apple 公证签名，官方 DMG 分发。

## 主要功能（能做什么）

- 刘海桌宠形态的 AI 状态展示
- 7 类 AI 终端统一控制面
- 实时系统遥测、多任务并行
- drizzle 数据库、client 前端、docs

## 架构设计

```text
client/       客户端
drizzle/      数据层
components.json / docs / patches
```

## 实现思路与核心逻辑

- "可观察控制面"：把分散的 AI 终端状态集中展示
- 桌宠形态降低工具感，增强日常陪伴

## 亮点

- 592 stars，桌宠 + 控制面组合有差异化
- 原生 macOS、Apple 公证，发布规范
- 中英双语文档

## 局限与风险（可选）

- **无 LICENSE 文件**：默认保留所有权利，使用/分发需联系作者确认（已列入本地 backlog 许可证盘点）
- 仅 macOS 14+；手机端开发中

## 分析说明

基于 README、client/drizzle 结构；未运行应用。
