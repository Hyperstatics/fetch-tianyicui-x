# CisaSettle/bluffking 分析报告

- 仓库：[CisaSettle/bluffking](https://github.com/CisaSettle/bluffking)
- 方向：纯 Rust 德州扑克引擎 + 可验证发牌（mental poker）
- 主要语言：Rust
- 指标：⭐ 0 · License AGPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/CisaSettle/bluffking)

> 分析基于 2026-08-06 抓取的 README、audits/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个纯 Rust 的无限制德州扑克规则引擎、Monte-Carlo 权益/翻后求解器，以及可验证发牌（mental poker）crate——无 IO、无异步、无数据库。
- **能拿来干什么**：扑克引擎研究、公平发牌验证。
- **适合谁**：游戏/密码学研究者。
- **快速判断**：如果你做扑克引擎或可验证发牌，它值得看；否则用不上。

## 分类

- 主分类：6. 特定领域 / 其他（扑克引擎/密码学）
- 副分类：无
- 理由：README 自述 "A pure-Rust No-Limit Texas Hold'em rules engine, a Monte-Carlo equity / post-hand solver, and a verifiable card-dealing ('mental poker') crate"。

## 项目方向与定位

扑克引擎 + mental poker：audits/ 安全审计、blog。

## 主要功能（能做什么）

- 德州扑克规则引擎
- Monte-Carlo 权益求解
- 可验证发牌

## 架构设计

```text
audits/ blog/
```

## 实现思路与核心逻辑

- 纯 Rust、无 IO/async/db

## 亮点

- 0 stars，密码学+游戏结合
- AGPL-3.0 开源

## 局限与风险（可选）

- **AGPL-3.0**：派生分发需遵守 copyleft
- 与"Agent Harness 内测"主题无关

## 分析说明

基于 README、audits/ 与文档；未运行。
