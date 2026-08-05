# YangKGcsdms/antlegion-platform 分析报告

- 仓库：[YangKGcsdms/antlegion-platform](https://github.com/YangKGcsdms/antlegion-platform)
- 方向：自治 Agent 的事实总线（共享不可变事实而非命令）
- 主要语言：TypeScript
- 指标：⭐ 13 · License 双许可证（LICENSE 文件，README 标 MIT）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/YangKGcsdms/antlegion-platform)

> 分析基于 2026-08-06 抓取的 README、antlegion-bus/dcu-workspace 结构与 LICENSE。注意：LICENSE 为双许可模式，使用前需确认条款。

## 这是什么（非技术版）

- **这是什么**：一个"给 AI 们共享事实的公共汽车站"。本地可嵌入的基础设施，Agent 之间靠共享不可变事实协调，而不是互相发命令。
- **能拿来干什么**：多 Agent 数据协调、事实驱动的协作。
- **适合谁**：多 Agent 平台开发者。
- **快速判断**：如果你想让 Agent"基于事实协作而非互相指挥"，它很有参考价值；否则不需要。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（事实总线基础设施）
- 副分类：3. 多 Agent 编排 / 协作系统
- 理由：README 自述 "A fact bus for autonomous agents — agents coordinate by sharing immutable facts, never by sending each other commands"。

## 项目方向与定位

AntLegion：fact bus + dcu-workspace + ecu；TypeScript 5.x、Node 18+、147 测试、alpha。

## 主要功能（能做什么）

- 不可变事实共享总线
- dcu-workspace/ecu 工作区
- 147 测试、Docker

## 架构设计

```text
antlegion-bus/   总线
dcu-workspace/ ecu/
```

## 实现思路与核心逻辑

- 事实驱动：Agent 通过共享状态协调，降低命令耦合
- 不可变事实：可审计、可追溯

## 亮点

- 13 stars，事实总线理念与多 Agent 趋势契合
- 测试完善（147 passing）

## 局限与风险（可选）

- **双许可证**需确认（列入本地 backlog）
- alpha 阶段

## 分析说明

基于 README、antlegion-bus/ 与 LICENSE；未运行。
