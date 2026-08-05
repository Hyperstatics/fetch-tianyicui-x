# gupsammy/Claudest 分析报告

- 仓库：[gupsammy/Claudest](https://github.com/gupsammy/Claudest)
- 方向：精选 Claude Code 插件市场（memory/research/coding/skills 等）
- 主要语言：Python
- 指标：⭐ 269 · License README 标注 MIT（仓库未见 LICENSE 文件，需确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/gupsammy/Claudest)

> 分析基于 2026-08-06 抓取的 README、plugins/ 与文档。⚠️ 仓库目录未见 LICENSE 文件，README 徽章标 MIT，使用前建议确认。

## 这是什么（非技术版）

- **这是什么**：一个"经过作者亲自使用验证的 Claude Code 插件商店"。作者自己项目里在用的插件才收录，保证"能用"。
- **能拿来干什么**：一键给 Claude Code 装记忆、研究、编码、技能、思考、内容类插件。
- **适合谁**：Claude Code 用户、想少踩插件坑的人。
- **快速判断**：如果你用 Claude Code 且想找靠谱插件，它是很好的入口；否则用不上。

## 分类

- 主分类：6. 特定领域 / 其他（插件市场）
- 副分类：2. Coding Harness / 工程向 Agent（Claude Code 生态）
- 理由：README 自述 "A curated Claude Code plugin marketplace. Everything here is something I personally use, build, and iterate on"。

## 项目方向与定位

精选型 Claude Code 插件市场：claude-memory、claude-research、claude-coding、claude-skills、claude-thinking、claude-content 等；`/plugin marketplace add gupsammy/claudest` 一条命令接入。

## 主要功能（能做什么）

- 插件市场接入（memory/research/coding/skills/thinking/content）
- 一键安装插件
- 作者真实项目验证背书

## 架构设计

```text
plugins/      插件实现
scripts/ tests/ docs/
```

## 实现思路与核心逻辑

- "个人精选"信任模式：收录标准是作者真实使用，而非数量
- Claude Code 原生插件机制，零改造成本

## 亮点

- 269 stars，插件市场垂直定位
- 精选质量背书，减少试错
- Python + tests 规范

## 局限与风险（可选）

- **未见 LICENSE 文件**：使用/分发前需确认授权
- 依赖 Claude Code 插件生态

## 分析说明

基于 README、plugins/ 与文档；未安装插件。
