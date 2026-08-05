# GodOnlyKn0w/mnema 分析报告

- 仓库：[GodOnlyKn0w/mnema](https://github.com/GodOnlyKn0w/mnema)
- 方向：append-only 语义拓扑（非 RAG 的持久记忆）
- 主要语言：Rust
- 指标：⭐ 1 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/GodOnlyKn0w/mnema)

> 分析基于 2026-08-06 抓取的 README、src/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个"持久工作记忆"系统。信息和历史表达为显式拓扑结构：不可变、哈希链的条目投影到 strands/trees/scopes，而不是对文本块做向量相似度（RAG）。进程和模型可替换，拓扑更长寿。
- **能拿来干什么**：持久的人类/多 Agent 工作记忆。
- **适合谁**：记忆方向研究者、多 Agent 平台开发者。
- **快速判断**：如果你研究"非 RAG 的记忆拓扑"，它很有参考价值；否则用不上。

## 分类

- 主分类：4. 记忆 / 上下文 / 知识管理（拓扑记忆）
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述 "An append-only semantic topology for durable human and multi-agent work... immutable, hash-chained entries projected into strands, trees, and scopes — not as vector similarity over blobs (RAG)"。

## 项目方向与定位

拓扑而非向量：append-only 哈希链条目 → strands/trees/scopes；进程/模型可替换，拓扑持久。

## 主要功能（能做什么）

- 不可变哈希链语义拓扑
- 跨会话持久记忆

## 架构设计

```text
src/ .archived-v3-*
```

## 实现思路与核心逻辑

- 拓扑优先于相似度：结构即记忆
- append-only：可追溯

## 亮点

- 1 stars，记忆架构理念前沿
- 与帖子"记忆/上下文"类别契合
- Apache-2.0

## 局限与风险（可选）

- 项目早期（有 v3 归档）
- 生态待验证

## 分析说明

基于 README、src/ 与文档；未运行。
