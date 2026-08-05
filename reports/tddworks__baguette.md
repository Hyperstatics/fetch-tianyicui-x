# tddworks/baguette 分析报告

- 仓库：[tddworks/baguette](https://github.com/tddworks/baguette)
- 方向：Headless iOS Simulator 管理器 + 主机侧输入注入（iOS 26）
- 主要语言：Swift
- 指标：⭐ 1,596 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/tddworks/baguette)

> 分析基于 2026-08-04 抓取的 README、Sources/Tests 结构与文档。

## 这是什么（非技术版）

- **这是什么**：一个"不开 Xcode 也能遥控 iOS 模拟器"的命令行工具。启动设备、60fps 看屏幕、模拟点击/滑动/多指手势/键盘、读日志、看辅助功能树、截图录像，还能把 Mac 摄像头喂给模拟器。
- **能拿来干什么**：iOS 自动化测试、UI 演示、无需图形界面的 CI/远程控制模拟器。
- **适合谁**：iOS 开发者、测试工程师、做移动端 Agent 自动化的人。
- **快速判断**：如果你要"无头/脚本化操作 iOS 模拟器"，它很对口；如果只在 Xcode 里点一点，不需要。

## 分类

- 主分类：6. 特定领域 / 其他（iOS 模拟器自动化工具）
- 副分类：2. Coding Harness / 工程向 Agent（移动端 Agent 执行底座）
- 理由：README 自述 "Headless iOS Simulator manager + host-side input injection for iOS 26"。

## 项目方向与定位

单 Swift CLI（`baguette`）+ 自带 Web UI，无头控制 iOS 模拟器：设备启动、60fps 屏幕流、全手势注入、日志、accessibility tree、截图/录像、摄像头注入（0.1.72+）。定位是 iOS 模拟器自动化基础设施。

## 主要功能（能做什么）

- Boot 设备、60fps 屏幕流、Web UI 控制
- 注入 tap/swipe/多指/系统手势/键盘/硬件按钮
- unified log、accessibility tree 检查
- 截图与录像、Mac 摄像头注入模拟器相机

## 架构设计

```text
Sources/    Swift CLI 与核心
Tests/     单元测试
scripts/ build.sh Makefile  构建
.claude-plugin / skills / .claude  Agent 集成
```

## 实现思路与核心逻辑

- 主机侧输入注入：直接驱动模拟器输入通道，替代 XCTest 框架依赖
- CLI + Web UI 双入口：脚本化和可视化兼顾
- Agent 友好：内置 Claude 插件与 skills 配置

## 亮点

- 1.6k stars，iOS 模拟器无头自动化稀缺工具
- 功能面广（手势/摄像头/日志/accessibility），CI/coverage 规范好
- 为移动端 Agent（如 UI 自动化 Agent）提供真实执行底座

## 局限与风险（可选）

- 仅 macOS 15+ / Xcode 26 / iOS 26 环境
- 与"Agent Harness 内测"主题相关度中等（偏移动测试工具）

## 分析说明

基于 README、Sources/Tests 结构与文档；未运行 CLI。
