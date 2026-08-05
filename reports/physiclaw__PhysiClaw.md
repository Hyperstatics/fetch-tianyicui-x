# physiclaw/PhysiClaw 分析报告

- 仓库：[physiclaw/PhysiClaw](https://github.com/physiclaw/PhysiClaw)
- 方向：物理操作手机的 AI Agent（摄像头看屏 + 触控笔点击）
- 主要语言：Python
- 指标：⭐ 294 · License MIT · 最近推送 2026-08-03
- 主页/文档：[docs.physiclaw.ai](https://docs.physiclaw.ai)

> 分析基于 2026-08-06 抓取的 README、hardware/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"真的用手操作你手机"的 AI。摄像头看着屏幕，触控笔点按，像人一样用手机：点外卖、买菜、打车、缴费、回消息——不需要 API、不需要数据线、手机上不用装任何东西。
- **能拿来干什么**：让 AI 帮你跑日常手机操作；绕过"无 API 应用"的自动化难题。
- **适合谁**：个人用户、自动化爱好者、Agent 硬件研究者。
- **快速判断**：如果你想要"物理方式操控手机"的 Agent，它很独特；否则普通自动化即可。

## 分类

- 主分类：6. 特定领域 / 其他（物理自动化/机器人 Agent）
- 副分类：1. 通用 Agent Runtime / Harness（Agent 执行体）
- 理由：README 自述 "An AI agent that physically operates a phone... watches a phone's screen with a camera and taps it with a stylus"。

## 项目方向与定位

把"屏幕当 API"：摄像头读屏、触控笔做手势，对手机来说与真人手指无异（无指纹、难以检测）。面向无公开 API 的日常应用（外卖/购物/打车/缴费/消息），也适用于反机器人检测场景。

## 主要功能（能做什么）

- 摄像头屏幕识别 + 触控笔手势执行
- 无需 API/OAuth/ADB，手机零安装
- 覆盖外卖/购物/打车/缴费/回消息等日常操作
- hardware/ 硬件方案 + install 脚本 + 中英文档

## 架构设计

```text
hardware/   触控笔/机械结构
（视觉识别 + 动作执行闭环）
```

## 实现思路与核心逻辑

- "屏幕即 API"：绕过封闭应用限制
- 物理执行：与真人手指不可区分，反检测优势
- 视觉闭环：摄像头实时读取屏幕状态驱动动作

## 亮点

- 294 stars，物理 Agent 方案独特（区别于纯软件自动化）
- 对"无 API 应用"的通用覆盖是核心价值
- MIT 开源，中文文档齐全

## 局限与风险（可选）

- 需要硬件设备（摄像头+触控笔+手机摆放）
- 物理操作速度慢于软件自动化
- 与"Agent Harness 内测"主题相关度中等（是执行体）

## 分析说明

基于 README、hardware/ 与文档；未搭建硬件。
