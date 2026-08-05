# haseeb-heaven/open-agent 分析报告

- 仓库：[haseeb-heaven/open-agent](https://github.com/haseeb-heaven/open-agent)
- 方向：开源终端 Agent（自然语言规划、工具执行、免费/本地/BYOK 模型）
- 主要语言：TypeScript
- 指标：⭐ 279 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/haseeb-heaven/open-agent)

> 分析基于 2026-08-06 抓取的 README 与目录结构。

## 这是什么（非技术版）

- **这是什么**：一个开源终端 AI Agent。你用大白话描述任务，它规划、调工具、交付结果；支持免费 OpenRouter 模型、本地 Ollama/LM Studio，也支持 BYOK 云端模型，无需账号。
- **能拿来干什么**：日常终端 AI 任务（分析数据、写脚本、画图等）。
- **适合谁**：想零成本试用终端 Agent 的开发者。
- **快速判断**：如果你想要"不花钱、不绑账号"的终端 Agent，它很合适；否则其他 Agent 也行。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "Describe a task in plain English. OpenAgent plans, uses tools, and delivers — with free, local, and BYOK cloud models. No account required."。

## 项目方向与定位

零门槛终端 Agent：免费模型（OpenRouter）、本地模型（Ollama/LM Studio）、BYOK 云模型三路接入；Windows/Mac/Linux；无厂商锁定。规划 + 工具执行 + 交付闭环。

## 主要功能（能做什么）

- 自然语言任务规划与工具执行
- Free / Local / BYOK 三模式
- 跨平台（Win/Mac/Linux）
- npm 安装即用

## 架构设计

```text
（npm 包 + 终端 UI）
```

## 实现思路与核心逻辑

- 以"零配置可用"为目标：npm install && npm start 即可
- 多模型来源抽象：免费/本地/BYOK 统一接口

## 亮点

- 279 stars，零门槛定位清晰
- Apache-2.0，无账号无锁定

## 局限与风险（可选）

- 功能面较基础，生态小
- 与主流 Agent（Claude Code/Codex）差距明显

## 分析说明

基于 README 与目录结构；未运行。
