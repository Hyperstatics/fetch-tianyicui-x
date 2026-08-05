# ZacharyZhang-NY/Kigi-CLI 分析报告

- 仓库：[ZacharyZhang-NY/Kigi-CLI](https://github.com/ZacharyZhang-NY/Kigi-CLI)
- 方向：内置 Graph Engineering 的终端 Coding Agent（/graph 依赖图）
- 主要语言：Rust
- 指标：⭐ 54 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/ZacharyZhang-NY/Kigi-CLI)

> 分析基于 2026-08-06 抓取的 README、crates/ 与文档。

## 这是什么（非技术版）

- **这是什么**：一个终端 AI 编程助手，首创"图工程"：`/graph` 把一个大目标拆成一组相互依赖、自动验证的 Agent 循环图，规划、并行、对抗性验证、合并，端到端完成。
- **能拿来干什么**：复杂任务拆解并行执行、终端日常 AI 编程。
- **适合谁**：开发者、想用"目标→依赖图"模式的人。
- **快速判断**：如果你喜欢"把任务画成图让 AI 并行干"，它很有特色；否则普通 Agent 即可。

## 分类

- 主分类：2. Coding Harness / 工程向 Agent
- 副分类：3. 多 Agent 编排 / 协作系统（依赖图编排）
- 理由：README 自述 "/graph turns one objective into a dependency graph of autonomous, self-verifying agent loops"。

## 项目方向与定位

"The world's first CLI with built-in Graph Engineering"：目标→依赖图→自验证 agent loops→并行/对抗验证/合并。支持登录主流账号（Claude/ChatGPT/Copilot/Grok）或 BYOK（OpenAI/Anthropic/Google/DeepSeek/Groq/Moonshot 等二十多家）。

## 主要功能（能做什么）

- /graph 依赖图编排
- 全屏终端、CI 无头（-p）、ACP 编辑器对接
- 多提供商登录/BYOK

## 架构设计

```text
crates/       Rust 核心
bin/ about.toml
```

## 实现思路与核心逻辑

- 图工程：目标拆解为依赖图，节点为自验证 agent loop
- 并行 + 对抗性验证 + 合并回主干

## 亮点

- 54 stars，Graph Engineering 概念有差异化
- 多提供商免 API key（用现有订阅）设计贴心
- Apache-2.0

## 局限与风险（可选）

- 项目较新，图模式的稳定性待验证
- 与"Agent Harness 内测"主题相关度中等

## 分析说明

基于 README、crates/ 与文档；未运行。
