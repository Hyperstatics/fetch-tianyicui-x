# tommy0103/obelisk 分析报告

- 仓库：[tommy0103/obelisk](https://github.com/tommy0103/obelisk)
- 方向：过去的 Claude Code/Codex/Kimi/Pi 会话可查询（Agent 记忆层）
- 主要语言：JavaScript/TypeScript
- 指标：⭐ 298 · License AGPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[PRODUCT.md](https://github.com/tommy0103/obelisk/blob/main/PRODUCT.md)

> 分析基于 2026-08-06 抓取的 README、app/packages 结构与产品文档。

## 这是什么（非技术版）

- **这是什么**：一个"AI 会话档案馆"。把你过去用 Claude Code、Codex、Kimi、Pi 干过的活全部索引到本地 SQLite，你的 Agent 可以搜索查询，你也可以用桌面应用浏览。
- **能拿来干什么**：找回"以前是怎么解决的"、让 Agent 基于历史会话继续工作。
- **适合谁**：重度 AI 编程用户、想积累会话资产的人。
- **快速判断**：如果你总在重复问 AI 同样的问题，它很有价值；否则不需要。

## 分类

- 主分类：4. 记忆 / 上下文 / 知识管理（会话索引）
- 副分类：2. Coding Harness / 工程向 Agent
- 理由：README 自述 "Past Claude Code, Codex, Kimi Code, and Pi sessions -- queryable by your agent, browsable by you"。

## 项目方向与定位

同一 SQLite 索引两面：Agent 侧（obelisk CLI 拥有本地运行时 + agent skill 教编码 Agent 搜索会话历史）；App 侧（Electron 桌面应用浏览会话、管理记忆、查看用量统计与周报）。

## 主要功能（能做什么）

- 多 Agent 历史会话索引（Claude Code/Codex/Kimi/Pi）
- Agent 侧：CLI + skill 查询会话（写 JS 查询本地执行）
- App 侧：浏览、记忆管理、用量统计、周报卡片

## 架构设计

```text
app/            Electron 桌面
packages/       共享核心（SQLite 索引）
install.sh packaging/
```

## 实现思路与核心逻辑

- 会话即数据：SQLite 统一索引，Agent 与人共享
- Agent 查询走本地 JS 执行，结果以自然语言返回
- 双端（CLI/skill + App）覆盖"让 Agent 查"和"人浏览"

## 亮点

- 298 stars，"会话记忆"角度与帖子"记忆/上下文"类别契合
- 多 Agent 兼容 + 本地 SQLite 隐私友好
- AGPL-3.0 开源

## 局限与风险（可选）

- 依赖各 CLI Agent 会话格式，兼容面需持续维护
- AGPL-3.0 派生分发受限

## 分析说明

基于 README、app/packages 与 PRODUCT.md；未运行。
