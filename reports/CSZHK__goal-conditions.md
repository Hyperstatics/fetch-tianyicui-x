# CSZHK/goal-conditions 分析报告

- 仓库：[CSZHK/goal-conditions](https://github.com/CSZHK/goal-conditions)
- 方向：Claude Code /goal skill 增强（条件表述校验）
- 主要语言：TypeScript（skill）
- 指标：⭐ 1 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/CSZHK/goal-conditions)

> 分析基于 2026-08-06 抓取的 README、skills/ 与文档。

## 这是什么（非技术版）

- **这是什么**：给 Claude Code 的 /goal 命令用的增强 skill。/goal 的评估器只读对话记录、不跑工具，条件表述错一个就会烧掉几十轮对话；这个 skill 帮助把条件写准。
- **能拿来干什么**：更可靠的 /goal 使用。
- **适合谁**：Claude Code 用户。
- **快速判断**：如果你用 Claude Code /goal，它很有用；否则用不上。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent（skill）
- 副分类：5. 评测 / Benchmark 工具（条件评估）
- 理由：README 自述 "The skill /goal should have shipped with... Its evaluator only reads the transcript — never runs tools. One mis-stated condition burns dozens of turns"。

## 项目方向与定位

针对 /goal 条件表述问题的增强 skill：帮助写准确、可评估的条件。

## 主要功能（能做什么）

- /goal 条件校验增强
- Claude Code skill

## 架构设计

```text
skills/ scripts/ .claude-plugin/
```

## 实现思路与核心逻辑

- 理解评估器限制（不跑工具），在条件表述端补强

## 亮点

- 1 stars，Claude Code 生态实用 skill
- MIT 开源

## 局限与风险（可选）

- 强依赖 Claude Code
- 与"内测 Harness"主题相关度低

## 分析说明

基于 README、skills/ 与文档；未运行。
