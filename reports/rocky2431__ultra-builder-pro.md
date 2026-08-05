# rocky2431/ultra-builder-pro 分析报告

- 仓库：[rocky2431/ultra-builder-pro](https://github.com/rocky2431/ultra-builder-pro)
- 方向：面向真实工程的 harness（已归档，迁移至 ultra-builder-pro-cli）
- 主要语言：Python
- 指标：⭐ 10 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/rocky2431/ultra-builder-pro)

> 分析基于 2026-08-06 抓取的 README、agents/hooks 与文档。⚠️ 仓库已归档（read-only），开发迁移到 ultra-builder-pro-cli。

## 这是什么（非技术版）

- **这是什么**：一个"给真实工程用的 AI 编码 harness"。六阶段流程、TDD 与证据纪律、审查视角；已归档，新版本（ultra-builder-pro-cli）以可安装包形式支持 Claude Code/Codex/OpenCode/Kimi/Grok 五端。
- **能拿来干什么**：AI 编码质量流程参考；了解六阶段脊柱设计。
- **适合谁**：开发者、Agent 工作流设计者。
- **快速判断**：如果你想参考"工程级 harness 设计"，它有价值；注意已归档。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent
- 副分类：1. 通用 Agent Runtime / Harness
- 理由：README 自述六阶段脊柱、PHILOSOPHY 四目标五戒律、TDD 与证据纪律。

## 项目方向与定位

真实工程 harness：六阶段 spine、review lenses、TDD、证据纪律、hook 契约。已迁移：新 CLI 无 MCP/SQLite/daemon，以"owner 可读文件 + Git 为唯一权威"。

## 主要功能（能做什么）

- 六阶段工作流、TDD/证据纪律
- hooks/commands/output-styles
- 迁移到 ultra-builder-pro-cli（五端）

## 架构设计

```text
agents/ hooks/ commands/ output-styles/
```

## 实现思路与核心逻辑

- 流程纪律先行：证据与测试门禁
- 简化迁移：去掉常驻服务，文件+Git 为权威

## 亮点

- 10 stars，工程级 harness 设计参考
- 迁移方向（更薄、更简单）体现迭代思考

## 局限与风险（可选）

- **已归档**：使用请转向 ultra-builder-pro-cli
- 与"内测 Harness"主题相关度中等

## 分析说明

基于 README、agents/hooks 与文档；未运行。
