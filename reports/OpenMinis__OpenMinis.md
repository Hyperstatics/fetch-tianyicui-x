# OpenMinis/OpenMinis 分析报告

- 仓库：[OpenMinis/OpenMinis](https://github.com/OpenMinis/OpenMinis)
- 方向：端侧私有的移动 AI Agent（iOS/Android，自带 Linux shell 沙箱）
- 主要语言：Swift（+ 原生移动端）
- 指标：⭐ 3,084 · License GPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[openminis.app](https://openminis.app)

> 分析基于 2026-08-04 抓取的 README 与目录结构。许可证 GPL-3.0（copyleft）。

## 这是什么（非技术版）

- **这是什么**：一个"住在手机里的私人 AI 助理"。自带一个完整的小型 Linux 系统（沙箱），AI 可以在里面装软件、跑脚本、操作真实文件；还能访问健康、日历、通讯录、HomeKit 等设备能力。
- **能拿来干什么**：在手机上让 AI 深度干活（研究、自动化、设备联动），自带模型密钥，数据在端侧。
- **适合谁**：注重隐私的 AI 用户、移动端 Agent 探索者。
- **快速判断**：如果你想"手机上的私有 AI + 真实执行能力"，它很有代表性；如果只是聊天，太重了。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness（端侧 Agent 运行时）
- 副分类：6. 特定领域 / 其他（移动应用）
- 理由：README 自述 "Your private, on-device AI agent... a full Linux shell running on your device, browser automation, extensible skills, persistent memory"。

## 项目方向与定位

把"给 AI 一台真电脑"做到移动端：设备内沙箱 Alpine Linux（可装包/跑脚本/操作文件）、浏览器自动化、设备集成（健康/日历/提醒/通讯录/HomeKit/蓝牙/剪贴板/媒体/闹钟）、持久记忆、可扩展 skills、BYOM（自带模型：Claude/GPT/Gemini 等）。理念：产品优势来自与用户的紧密反馈闭环。

## 主要功能（能做什么）

- 自带模型（BYOM）：自己的 API key 或账号登录
- 设备内 Linux shell 沙箱（Alpine）：装包、脚本、真实文件操作
- 设备集成工具：健康、日历、提醒、通讯录、HomeKit、蓝牙、剪贴板、媒体、闹钟
- 浏览器自动化、可扩展 skills、跨会话持久记忆
- iCloud 同步、细粒度权限

## 架构设计

```text
src/        原生应用（iOS/Android）
deps/       依赖与运行时
scripts/    构建脚本
docs/ BUILDING.md / THIRD_PARTY_LICENSES.md
```

## 实现思路与核心逻辑

- "端侧真执行"：在设备内跑真实 Linux 沙箱，Agent 有真实执行能力而非只读对话
- 设备能力工具化：把系统功能（健康/HomeKit 等）暴露为 Agent 工具
- 隐私优先：数据端侧、BYOM，不依赖云端中转

## 亮点

- 3.1k stars，端侧移动 Agent 的代表项目
- 设备内 Linux 沙箱是稀缺能力
- 免费开源（App Store + APK 双发），理念清晰

## 局限与风险（可选）

- **GPL-3.0**：派生分发需遵守 copyleft
- 移动端沙箱的执行边界与权限安全需持续验证
- 硬件/平台适配范围（iOS/Android 原生）维护成本高

## 分析说明

基于 README 与目录结构；未运行移动应用。
