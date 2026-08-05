# peisp/catdb 分析报告

- 仓库：[peisp/catdb](https://github.com/peisp/catdb)
- 方向：跨平台桌面数据库管理工具
- 主要语言：Go（Wails）+ Vue
- 指标：⭐ 28 · License Apache-2.0（LICENSE 确认）· 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/peisp/catdb)

> 分析基于 2026-08-06 抓取的 README、internal/frontend 结构与文档。元数据标 NOASSERTION，LICENSE 实为 Apache-2.0。

## 这是什么（非技术版）

- **这是什么**：一个"数据库图形管理工具"。跨平台桌面应用，支持 MySQL、PostgreSQL、SQLite 和达梦（DM），更多数据库通过驱动插件扩展。
- **能拿来干什么**：日常数据库管理、可视化操作。
- **适合谁**：开发者、DBA。
- **快速判断**：如果你要一个轻量跨平台数据库客户端，它值得看；否则 Navicat/DBeaver 等更成熟。

## 分类

- 主分类：6. 特定领域 / 其他（数据库工具）
- 副分类：无
- 理由：README 自述 "A cross-platform desktop database management tool"。

## 项目方向与定位

Wails v3 + Vue 3 桌面数据库工具：编译期注册驱动插件扩展数据库支持。

## 主要功能（能做什么）

- MySQL/PostgreSQL/SQLite/DM 支持
- 驱动插件扩展
- macOS/Windows/Linux

## 架构设计

```text
internal/      Go 核心
frontend/      Vue 前端
docs/ DESIGN.md ARCHITECTURE.md
```

## 实现思路与核心逻辑

- 编译期驱动注册：新增数据库不改核心
- Wails 桌面壳 + Vue 界面

## 亮点

- 28 stars，跨平台数据库工具
- 设计/架构文档完善
- Apache-2.0（已核对）

## 局限与风险（可选）

- 与"Agent Harness 内测"完全无关
- 成熟度待提升

## 分析说明

基于 README、internal/frontend 与文档；未运行。
