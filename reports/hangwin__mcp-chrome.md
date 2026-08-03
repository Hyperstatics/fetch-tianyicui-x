# hangwin/mcp-chrome 分析报告

- 仓库：[hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome)
- 方向：Chrome 扩展 + MCP Server——把用户日常浏览器变成 AI 助手
- 主要语言：TypeScript（+ WebAssembly SIMD）
- 指标：⭐ 12,248 · License MIT · 最近推送 2026-01-06
- 主页/文档：[README_zh](https://github.com/hangwin/mcp-chrome/blob/main/README_zh.md)

> 分析基于 2026-08-04 抓取的 README、app/、packages/ 结构。

## 这是什么（非技术版）

- **这是什么**：一个"给 AI 配的浏览器遥控器"。装个 Chrome 扩展后，AI 就能直接操作你日常使用的浏览器——看标签页、截图、点按钮、搜书签历史，还能跨多个标签页干活。
- **能拿来干什么**：让 AI 帮你操作网页、自动填表、分析页面内容；因为用的是你自己的浏览器，登录状态、插件、配置都还在。
- **适合谁**：重度浏览器用户、想用 AI 代替重复网页操作的人、开发者。
- **快速判断**：如果你想"AI 用我自己的浏览器干活"（不用重开无头浏览器、不用重新登录），它就是；如果只是写常规网页脚本，Playwright 那类工具更稳。

## 分类

- 主分类：6. 特定领域 / 其他（浏览器自动化 MCP 工具）
- 副分类：1. 通用 Agent Runtime / Harness（MCP 工具服务器）
- 理由：README 自述 "Chrome extension-based Model Context Protocol (MCP) server that exposes your Chrome browser functionality to AI assistants"。

## 主要功能（能做什么）

- 20+ 工具：截图、网络监控、交互操作、书签管理、浏览历史等
- 复用日常 Chrome：登录态、用户配置、插件全部保留
- 跨标签页上下文 + 语义搜索（内置向量库，SIMD WebAssembly 4-8x 加速）
- 智能内容提取与相似度匹配
- Streamable HTTP 连接；Claude Code / Codex 可视化编辑器支持
- 完全本地运行，隐私友好

## 架构设计

```text
app/
  chrome-extension  浏览器扩展（前端 + 采集）
  native-server     本地 MCP server（Node）
packages/
  shared            共享类型/工具
  wasm-simd         WebAssembly SIMD 向量加速
docs/ prompt/ releases/  文档、提示词模板、发布产物
```

## 实现思路与核心逻辑

- 与 Playwright 方案相反：不启动独立浏览器，直接驱动用户真实 Chrome，天然复用登录态与用户环境
- 扩展负责访问 Chrome 原生 API，本地 server 对外提供 MCP 协议
- 语义搜索用内置向量库（wasm-simd 加速），提升跨标签内容召回

## 亮点

- 12.2k stars，浏览器 MCP 方向头部项目，"免登录复用日常浏览器"差异化明显
- 完全本地、隐私友好；SIMD 加速是工程亮点
- 工具面广（书签/历史/网络/截图），支持多种模型/客户端

## 局限与风险（可选）

- README 自述 early stage，稳定性和功能迭代中（最近推送 2026-01）
- 依赖 Chrome 扩展，跨浏览器/移动端覆盖有限
- 授予 AI 浏览器控制权，权限与安全边界需要用户把关

## 分析说明

基于 README、app/packages 结构；未运行扩展，未细读 native-server 实现。
