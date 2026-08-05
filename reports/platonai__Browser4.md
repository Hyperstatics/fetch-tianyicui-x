# platonai/Browser4 分析报告

- 仓库：[platonai/Browser4](https://github.com/platonai/Browser4)
- 方向：浏览器 Agent 自动化平台（模块化，多语言/多后端）
- 主要语言：Kotlin（Java 系）
- 指标：⭐ 1,095 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/platonai/Browser4)

> 分析基于 2026-08-06 抓取的 README、browser4-* 模块结构与 CLI 文档。

## 这是什么（非技术版）

- **这是什么**：一个"浏览器自动化平台"。让 AI/脚本控制浏览器：交互页面、抓数据、批量处理，还能把 HTML 直接转成表格（号称零 token）；提供 CLI 和多种集成。
- **能拿来干什么**：网页自动化、数据采集、浏览器 Agent 开发。
- **适合谁**：开发者、爬虫/自动化工程师、做浏览器 Agent 的团队。
- **快速判断**：如果你要"浏览器级 Agent 底座 + 模块化"，它很合适；如果只偶尔抓个页面，用现成插件更快。

## 分类

- 主分类：6. 特定领域 / 其他（浏览器自动化平台）
- 副分类：2. Coding Harness / 工程向 Agent（Agent 工具）
- 理由：README 自述为浏览器 Agent 平台，提供 agentic 模块与 CLI。

## 项目方向与定位

模块化浏览器自动化平台：core/apps/agentic/pdk（插件开发包）/plugins/rest 分层；支持交互、数据提取、规模化处理、HTML→表格零 token 转换；CLI 人类友好，状态持久化，附测试夹具服务器（MockSite）。中文社区与 Gitee 镜像友好。

## 主要功能（能做什么）

- 页面交互、数据提取、规模化处理
- HTML 转电子表格（零 token）
- CLI 完整命令参考、超时环境变量、状态持久化
- 插件体系（browser4-pdk/plugins）、Agent 工具（browser4-agent-tools/agentic）
- 多平台启动脚本（b4w.sh/bat/ps1）

## 架构设计

```text
browser4-core / boot / rest   核心与启动
browser4-apps / agentic / agent-tools  应用与 Agent 层
browser4-pdk / plugins        插件体系
browser4-tests / MockSite     测试夹具
```

## 实现思路与核心逻辑

- 模块化分层：核心、Agent 层、插件层分离，可组合
- CLI 优先：人类可读的完整命令集，兼顾脚本化
- 测试驱动：MockSite 提供可复现的测试页面

## 亮点

- 1.1k stars，浏览器 Agent 平台模块化程度高
- HTML→表格零 token 等实用特性有差异化
- 中英双语 + Gitee 镜像，中文生态友好

## 局限与风险（可选）

- 浏览器自动化赛道竞争激烈（midscene/mcp-chrome 等）
- 平台整体复杂度高，上手需要时间

## 分析说明

基于 README、模块结构与 CLI 文档；未运行。
