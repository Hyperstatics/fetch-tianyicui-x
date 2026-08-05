# 13f/aman 分析报告

- 仓库：[13f/aman](https://github.com/13f/aman)
- 方向：aman——a man. an agent man.（Rust Agent，强调安全）
- 主要语言：Rust
- 指标：⭐ 6 · License AGPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/13f/aman)

> 分析基于 2026-08-06 抓取的 README、ARCHITECTURE.md 与 SECURITY_HARNESS 文档。⚠️ ALPHA，自行承担风险。

## 这是什么（非技术版）

- **这是什么**：一个 Rust 写的 Agent（"a man, an agent man"），强调安全架构：输入输出消毒、内容过滤、OS 沙箱、审计日志全部启用。作者明确警告没有 meme/token/币，谨防诈骗。
- **能拿来干什么**：实验/研究型 Agent。
- **适合谁**：Rust 开发者、安全向 Agent 研究者。
- **快速判断**：如果你对"安全优先的 Agent 实现"感兴趣，可参考；否则不建议生产使用。

## 分类

- 主分类：1. 通用 Agent Runtime / Harness
- 副分类：6. 特定领域 / 其他
- 理由：README 自述 "a man. an agent man."，SECURITY_HARNESS 强调安全架构。

## 项目方向与定位

ALPHA Agent：安全架构（消毒/过滤/沙箱/审计）、API/架构文档、防诈骗声明。

## 主要功能（能做什么）

- Agent 核心 + 安全 harness
- API.md/ARCHITECTURE.md 文档

## 架构设计

```text
crates/ 13f__aman/
SECURITY_HARNESS.md
```

## 实现思路与核心逻辑

- 安全优先：输入输出消毒、沙箱、审计

## 亮点

- 6 stars，安全向 Agent 实现
- AGPL-3.0 开源

## 局限与风险（可选）

- ALPHA，存储格式可能变化
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、ARCHITECTURE.md 与文档；未运行。
