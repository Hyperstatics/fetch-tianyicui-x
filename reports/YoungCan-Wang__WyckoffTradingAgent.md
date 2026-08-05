# YoungCan-Wang/WyckoffTradingAgent 分析报告

- 仓库：[YoungCan-Wang/WyckoffTradingAgent](https://github.com/YoungCan-Wang/WyckoffTradingAgent)
- 方向：A 股/港股/美股威科夫量价分析智能体
- 主要语言：Python
- 指标：⭐ 558 · License AGPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[架构文档](https://github.com/YoungCan-Wang/WyckoffTradingAgent/blob/main/docs/ARCHITECTURE.md)

> 分析基于 2026-08-06 抓取的 README、agents/ 结构与架构文档。仅教育/研究用途，非投资建议。

## 这是什么（非技术版）

- **这是什么**：一个"威科夫交易分析师 AI"。你用自然语言问，它读取 A 股/港股/美股行情，做威科夫量价结构识别、生成研报、管理持仓风控、复盘形态并推送通知。
- **能拿来干什么**：技术分析研究、形态复盘、行情扫描（美股/港股漏斗）。
- **适合谁**：对量价分析感兴趣的交易者/开发者。
- **快速判断**：如果你是量价分析学习者，它可作研究工具；**注意不是投资建议，风险自负**。

## 分类

- 主分类：6. 特定领域 / 其他（量化/技术分析 Agent）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述"A 股/港股/美股威科夫量价分析智能体……你说人话，他读盘面"。

## 项目方向与定位

自然语言驱动的威科夫分析自动化链路：日线行情（TickFlow 实时拉取）、威科夫结构识别、AI 研报、持仓风控、形态复盘、通知推送；React Web + CLI + MCP + GitHub Actions 构成产品形态；Supabase 仅存用户配置/持仓/复盘等。

## 主要功能（能做什么）

- 自然语言威科夫对话分析
- A 股/港股/美股行情扫描（漏斗）
- 威科夫结构识别、AI 研报、持仓风控、形态复盘、通知
- React Web、CLI、MCP 三入口

## 架构设计

```text
agents/       分析 Agent
attach/ metrics/  数据与指标
（Web + CLI + MCP + GitHub Actions）
```

## 实现思路与核心逻辑

- 行情实时拉取（TickFlow）→ 结构识别 → 研报/风控/复盘 → 通知
- 多入口（Web/CLI/MCP）复用同一分析内核
- 明确风险披露：教育/研究用途

## 亮点

- 垂直领域完整（分析+研报+风控+复盘）
- AGPL-3.0 开源，PyPI 发布，多语言文档
- 与帖子主题相关（Agent 应用示例）

## 局限与风险（可选）

- **AGPL-3.0**：派生分发需遵守 copyleft
- 金融领域合规风险：明确非投资建议
- 数据源依赖 TickFlow/Supabase 服务

## 分析说明

基于 README、agents/ 与架构文档；未运行分析。
