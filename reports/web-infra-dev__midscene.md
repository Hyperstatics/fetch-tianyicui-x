# web-infra-dev/midscene 分析报告

- 仓库：[web-infra-dev/midscene](https://github.com/web-infra-dev/midscene)
- 方向：视觉驱动的 UI 自动化/测试——用自然语言控制任意平台
- 主要语言：TypeScript
- 指标：⭐ 14,477 · License MIT · 最近推送 2026-08-03
- 主页/文档：[midscenejs.com](https://midscenejs.com)

> 分析基于 2026-08-04 抓取的 README 与目录树；仓库约 497MB，未克隆，采用 API-only 分析。

## 这是什么（非技术版）

- **这是什么**：一个"看得见的 AI 自动化工具"。你直接用中文/英文描述"帮我在表单里注册并提交"，AI 通过截图理解界面，自己操作网页、手机 App 或电脑软件。
- **能拿来干什么**：写自动化测试、自动填表、批量操作 UI、做演示；不用写复杂的选择器脚本。
- **适合谁**：测试工程师、需要 UI 自动化的团队、想用 AI 操作电脑/手机的人。
- **快速判断**：如果你的测试/自动化总因界面变化而挂，它值得试；如果只是简单脚本，传统工具也够。

## 分类

- 主分类：6. 特定领域 / 其他（UI 测试与自动化）
- 副分类：2. Coding Harness / 工程向 Agent（Agent 驱动的自动化）
- 理由：README 自述 "Open-source, vision-driven UI testing — write tests in natural language, automate any platform"。

## 项目方向与定位

字节跳动 web-infra 团队出品的视觉驱动自动化框架：以多模态模型"看截图"理解界面，替代传统 DOM 选择器/坐标脚本。支持 Web、iOS、Android、鸿蒙、桌面系统，并配套录制器、可视化与 MCP/Skills 生态（OpenClaw 集成）。

## 主要功能（能做什么）

- 自然语言编写 UI 测试与自动化操作
- 多平台：Web / iOS / Android / HarmonyOS / 桌面（Win/Mac/Linux）
- UI-TARS 系列视觉模型 + 任意多模态模型接入
- 录制器（recorder）、可视化调试（visualizer）、CLI
- Midscene Skills：与 OpenClaw 配合控制任意平台

## 架构设计

```text
packages/
  core            统一核心（自然语言 → 视觉理解 → 动作）
  web-integration / webdriver / computer / ios / android / harmony  平台适配层
  cli / recorder / visualizer / shared / playground
apps/             示例与配套应用
```

## 实现思路与核心逻辑

- 视觉优先：截图 + 多模态模型理解页面结构与操作点，天然抗 DOM 变化
- 核心与平台解耦：core 定义统一语义，各平台适配器执行
- 自然语言作为 DSL：降低测试编写门槛

## 亮点

- 14.5k stars，字节出品，Web 自动化方向头部项目之一
- 视觉驱动的思路在"界面频繁变动"场景优势明显
- 平台覆盖广 + 录制/可视化工具链完整 + OpenClaw 生态联动

## 局限与风险（可选）

- 依赖多模态模型能力与成本，离线/本地模型效果需验证
- 仓库约 497MB，体积大
- 复杂交互（拖拽、弹窗、非标准组件）仍需人工兜底

## 分析说明

API-only 分析（README + 目录树 + packages 列表），未克隆源码，未运行测试。
