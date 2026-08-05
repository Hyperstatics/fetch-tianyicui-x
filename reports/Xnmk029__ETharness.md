# Xnmk029/ETharness 分析报告

- 仓库：[Xnmk029/ETharness](https://github.com/Xnmk029/ETharness)
- 方向：Agent MFT——面向 Pi 的记忆寻址层
- 主要语言：TypeScript
- 指标：⭐ 17（抓取时）· License 未见 LICENSE 文件（需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/Xnmk029/ETharness)

> 分析基于 2026-08-06 抓取的 README、agent-mft/ 与文档。⚠️ 项目状态：暂缓开发（依赖 DeepSeek 长效 KV 缓存，待新模型验证）；未见 LICENSE 文件。

## 这是什么（非技术版）

- **这是什么**：一个"给 AI 记忆编地址"的系统（Agent MFT）。实现 Everything 风格的过滤语法与确定性地址，跨会话、跨后端精确定位 Agent 记忆；相当于给记忆一个文件系统式的寻址方式。
- **能拿来干什么**：Agent 跨会话记忆定位、记忆管理研究。
- **适合谁**：Agent 记忆方向研究者、Pi 用户。
- **快速判断**：如果你研究"Agent 记忆寻址"，它很有参考价值；否则用不上。

## 分类

- 主分类：4. 记忆 / 上下文 / 知识管理（记忆寻址）
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "Agent MFT——面向 Pi 的记忆寻址层……Everything 风格的过滤语法与确定性地址，支持跨会话、跨后端精确定位 Agent 记忆"。

## 项目方向与定位

独立记忆寻址系统：解决"会话记忆受限于上下文窗口、跨会话靠重复阐述"问题；暂缓开发（依赖 DeepSeek 磁盘前缀缓存 $0.0028/M）。

## 主要功能（能做什么）

- Everything 风格过滤语法
- 确定性记忆地址、跨会话定位
- gui/research 配套

## 架构设计

```text
agent-mft/      核心
gui/ research/ docs/
```

## 实现思路与核心逻辑

- 记忆寻址：把记忆变成可查询的地址空间
- 依赖长效 KV 缓存降本

## 亮点

- 17 stars（本批最高），记忆寻址理念独特
- 与帖子"记忆/上下文"类别直接相关

## 局限与风险（可选）

- **暂缓开发**（依赖 DeepSeek 缓存机制）
- **未见 LICENSE 文件**（列入本地 backlog）

## 分析说明

基于 README、agent-mft/ 与文档；未运行。
