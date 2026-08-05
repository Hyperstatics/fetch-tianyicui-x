# runesleo/claude-code-workflow 分析报告

- 仓库：[runesleo/claude-code-workflow](https://github.com/runesleo/claude-code-workflow)
- 方向：QuietHarness——给 AI 编程 Agent 加一层轻量可靠性边界
- 主要语言：Shell
- 指标：⭐ 708 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/runesleo/claude-code-workflow)

> 分析基于 2026-08-06 抓取的 README、scripts 与迁移文档。

## 这是什么（非技术版）

- **这是什么**：一套给 AI 编程助手"立规矩"的小工具。让 Claude Code / Codex / Cursor 干活前先看现状、不碰无关改动、按风险验证、不可逆动作先向你确认——核心只有 1,604 字节，可回滚。
- **能拿来干什么**：给现有 AI 编程工作流加可靠性护栏；换 Agent 时边界习惯可带走。
- **适合谁**：用 AI 编程维护真实项目、被"Agent 乱改/假完成"困扰的人。
- **快速判断**：如果你经常觉得"AI 干活不靠谱"，它值得试；如果只是写玩具代码，不需要。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent（可靠性边界/工作流）
- 副分类：无
- 理由：README 自述"给你的 AI 编程 Agent 装上一层极小、可回滚的工作边界"。

## 项目方向与定位

不替代 Agent、不套仪式：把长期验证有效的行为压缩成 1,604 字节共享 Core，提供 dry-run、备份、隔离测试与可逆安装。多端兼容（Claude Code/Codex/Cursor），"换工具时带走边界"。

## 主要功能（能做什么）

- 先看现状（inventory）再动手
- 保留无关改动、按风险分级验证
- 对删除/发布/生产变更/凭证操作先确认
- dry-run、备份、隔离测试、可逆安装

## 架构设计

```text
scripts/      核心脚本（inventory 等）
examples/ docs/
MIGRATION-v3 / RELEASE_NOTES  版本迁移
```

## 实现思路与核心逻辑

- "极小可回滚"优先：核心 1,604 字节，降低引入成本与维护负担
- 行为即规范：把可靠性经验固化为可执行脚本，而非提示词
- 多端兼容：同一组边界跨 Agent 复用

## 亮点

- 708 stars，解决"AI 乱改代码/假完成"的真实痛点
- 轻量（1.6KB 核心）设计克制，可逆安装
- MIT 开源，Shell 实现零依赖

## 局限与风险（可选）

- 不提供任务数据库/后台自动化/团队编排（README 明确边界）
- 与"Agent Harness 内测"主题相关度中等（偏工作流护栏）

## 分析说明

基于 README、scripts 与迁移文档；未运行脚本。
