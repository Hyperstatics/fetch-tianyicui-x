# Vizards/deepseek-v4-for-copilot 分析报告

- 仓库：[Vizards/deepseek-v4-for-copilot](https://github.com/Vizards/deepseek-v4-for-copilot)
- 方向：把 DeepSeek V4 放进 GitHub Copilot Chat 的 VS Code 扩展
- 主要语言：TypeScript
- 指标：⭐ 1,276 · License MIT · 最近推送 2026-08-03
- 主页/文档：[VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Vizards.deepseek-v4-for-copilot)

> 分析基于 2026-08-04 抓取的 README、src/ 与 package.json 结构。

## 这是什么（非技术版）

- **这是什么**：一个 VS Code 小插件。装完后，你就能在 Copilot Chat 的模型列表里直接选 DeepSeek V4，其他（Agent 模式、工具调用、MCP）都照常用。
- **能拿来干什么**：喜欢 Copilot 的界面和功能、又想用 DeepSeek 模型省钱的人。
- **适合谁**：VS Code / GitHub Copilot 用户、DeepSeek 用户。
- **快速判断**：如果你订阅了 Copilot 且想用 DeepSeek V4，它很实用；如果不用 Copilot，用不上。

## 分类

- 主分类：6. 特定领域 / 其他（IDE 扩展/模型接入）
- 副分类：2. Coding Harness / 工程向 Agent（扩展 Copilot Agent 能力）
- 理由：README 自述 "Pick DeepSeek V4 from the Copilot Chat model picker — and keep everything else Copilot already gives you"。

## 项目方向与定位

"Don't replace Copilot — power it up."：不换界面，只往模型选择器里加 DeepSeek V4 Pro/Flash。附带 vision 代理（把图片交给另一个 Copilot 模型描述后喂给 DeepSeek）、思考模式（Thinking Effort None/High/Max）、BYOK（密钥存 OS keychain）。

## 主要功能（能做什么）

- Copilot Chat 模型选择器中加入 DeepSeek V4 Pro / Flash
- Agent 模式、工具调用、MCP、skills 全部保留
- Vision 代理：文本模型看图
- Thinking 模式；BYOK，密钥存 keychain 不落盘

## 架构设计

```text
src/          扩展实现
package.json / package.nls*.json  清单与本地化
vscode.proposed.languageModelThinkingPart.d.ts  思考模式 API
docs/ resources/
```

## 实现思路与核心逻辑

- 复用 Copilot Chat 的模型选择接口注册自定义模型，零学习成本
- Vision 代理：透明转发图片 → 描述 → DeepSeek
- BYOK 直连 DeepSeek API，绕开中间商

## 亮点

- 1.3k stars，VS Code Marketplace / Open VSX 双分发
- 思路巧妙（"增强而非替代 Copilot"），实用性高
- MIT 开源，0.4MB 轻量

## 局限与风险（可选）

- 依赖 Copilot 与 DeepSeek API 的可用性；vision 代理依赖另一 Copilot 模型
- 与"Agent Harness 内测"主题相关度低（是模型接入插件）

## 分析说明

基于 README、src/ 与 package.json；未在 VS Code 中实测。
