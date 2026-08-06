# praxstack/agent-org 分析报告

- 仓库：[praxstack/agent-org](https://github.com/praxstack/agent-org)
- 方向：reviewer↔coder 门控循环（Claude Code 自主编码）
- 主要语言：Shell
- 指标：⭐ 0 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/praxstack/agent-org)

> 分析基于 2026-08-06 抓取的 README、hooks/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个轻量、零依赖的"评审↔编码"门控循环。一条命令跑一个物理上不能提交的 coder agent、一个自己跑真实构建/测试的确定性验证门（LLM 无法假装"通过了"）、以及可选的多声部评审委员会——循环到真正通过才提交。
- **能拿来干什么**：无人值守的自主编码 + 真实验证。
- **适合谁**：开发者、团队。
- **快速判断**：如果你要"AI 干活但验证是真的"，它很对口；否则不需要。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent（门控循环）
- 副分类：5. 评测 / Benchmark 工具
- 理由：README 自述 "reviewer↔coder gated loop... a deterministic verification gate that runs your real build/tests itself (so an LLM can't fake 'it passes')"。

## 项目方向与定位

门控自主编码：coder 不能提交 + 真实验证门 + 评审委员会。

## 主要功能（能做什么）

- review-loop.sh 一键循环
- 真实验证（build/tests）
- 多声部评审

## 架构设计

```text
hooks/ lib/ examples/ fanout.sh gstack-*.sh
```

## 实现思路与核心逻辑

- "让验证不可伪造"：门控由真实构建决定
- 循环直到真正通过

## 亮点

- 0 stars，门控循环设计
- 与"可验证 Agent"主题契合
- MIT 开源

## 局限与风险（可选）

- 依赖 Claude Code
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、hooks/ 与文档；未运行。
