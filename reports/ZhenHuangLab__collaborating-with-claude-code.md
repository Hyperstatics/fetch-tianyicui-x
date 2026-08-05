# ZhenHuangLab/collaborating-with-claude-code 分析报告

- 仓库：[ZhenHuangLab/collaborating-with-claude-code](https://github.com/ZhenHuangLab/collaborating-with-claude-code)
- 方向：Codex CLI skill——JSON bridge 委托 Claude Code 协作
- 主要语言：Python
- 指标：⭐ 39 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/ZhenHuangLab/collaborating-with-claude-code)

> 分析基于 2026-08-06 抓取的 README、SKILL.md 与桥接脚本。

## 这是什么（非技术版）

- **这是什么**：一个给 Codex 用的"协作技能"。让 Codex 通过一个 JSON 桥接脚本，把代码审查、调试、方案对比等任务委托给 Claude Code，并拿回结构化结果，实现多模型协作。
- **能拿来干什么**：多模型分工（Codex 主编排，Claude 做深度审查/调试）。
- **适合谁**：同时用 Codex 和 Claude Code 的开发者。
- **快速判断**：如果你想要"两个 AI 各干擅长的事"，它很实用；否则不需要。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent（多模型协作）
- 副分类：3. 多 Agent 编排 / 协作系统
- 理由：README 自述"把代码审查/调试/方案对比等任务委托给 Anthropic Claude Code CLI，并以结构化 JSON 结果返回"。

## 项目方向与定位

Codex skill + `scripts/claude_code_bridge.py`：SOTA context engineering（渐进式披露，两次 tool call 即可用）；解决 extended thinking 下 message 结构校验问题（把长 agentic loop 拆成多次短 loop）。

## 主要功能（能做什么）

- 委托 Claude Code 做审查/调试/方案对比
- JSON 结构化返回
- 渐进式披露（低成本掌握）
- 兼容 strict Anthropic-compatible proxy

## 架构设计

```text
SKILL.md                    技能定义
scripts/claude_code_bridge.py  桥接脚本
```

## 实现思路与核心逻辑

- bridge 模式：主 Agent 编排，Claude 执行子任务
- 拆长 loop 为短 loop：解决 thinking 校验兼容问题

## 亮点

- 39 stars，多模型协作实操性强
- context engineering 细节到位（progressive disclosure）
- 与帖子"多 Agent 协作"契合

## 局限与风险（可选）

- 需要同时安装 Codex 与 Claude Code
- 依赖 CLI 稳定性

## 分析说明

基于 README、SKILL.md 与桥接脚本；未运行。
