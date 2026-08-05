# Cai-aa/CAE-Agent-Hub 分析报告

- 仓库：[Cai-aa/CAE-Agent-Hub](https://github.com/Cai-aa/CAE-Agent-Hub)
- 方向：工程仿真（CAE）Agent 工具集：MCP 服务器 + 技能 + 结果查看器
- 主要语言：Python（MCP/skills）
- 指标：⭐ 670 · License MIT · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/Cai-aa/CAE-Agent-Hub)

> 分析基于 2026-08-06 抓取的 README、MCP/Skill/Subagent 结构与文档。

## 这是什么（非技术版）

- **这是什么**：一个"让 AI 操作工程仿真软件"的工具包。让 Codex/Cursor/Claude Code 能真正驱动 Abaqus、ANSYS Fluent、Workbench、HFSS 等仿真软件，而不是只生成离线的示例代码；还带一个浏览器结果查看器。
- **能拿来干什么**：AI 辅助有限元/流体/电磁仿真；把仿真经验固化为技能复用。
- **适合谁**：CAE 工程师、仿真团队、想用 AI 驱动商业软件的开发者。
- **快速判断**：如果你做工程仿真且想让 AI 直接操作软件，它很有价值；否则用不上。

## 分类

- 主分类：6. 特定领域 / 其他（CAE 工程仿真工具）
- 副分类：2. Coding Harness / 工程向 Agent（Agent 工具层）
- 理由：README 自述 "collection of MCP servers, reusable agent skills, solver automation scripts... for mainstream engineering simulation software"。

## 项目方向与定位

让 AI 编码客户端（Codex/Cursor/Claude Code/Claude Desktop）与真实 CAE 工具协作：Abaqus/CAE、ANSYS Fluent、Workbench Mechanical、ANSYS Electronics Desktop/HFSS 的 MCP 服务器；Abaqus 有限元技能；Text to CAE 浏览器查看器；示例工作流保持求解器二进制/许可证/私有路径/结果不入库。

## 主要功能（能做什么）

- MCP servers：Abaqus/CAE、Fluent、Workbench、HFSS
- Abaqus 全流程有限元技能（Skill/Subagent）
- Text to CAE 结果查看器（result_mesh.json）
- 示例工作流与模板；MCP/models/viewer 目录

## 架构设计

```text
MCP/        各仿真软件 MCP 服务器
Skill/ Subagent/  技能与子代理
viewer/     浏览器结果查看器
models/ examples/
```

## 实现思路与核心逻辑

- AI 客户端 → MCP/skill → 真实 CAE 应用或求解脚本 → 原生结果
- 技能按工作流阶段组织，可复用
- 敏感内容（许可证/路径/结果）通过约定排除在源码外

## 亮点

- 垂直领域稀缺：让 AI 真正驱动商业仿真软件
- MCP + Skills + viewer 工具链完整
- MIT 开源，中文/英文双语

## 局限与风险（可选）

- 依赖商业仿真软件环境（Abaqus/ANSYS），无法独立运行
- 与"Agent Harness 内测"主题相关度低（垂直工具）

## 分析说明

基于 README、MCP/Skill 结构与文档；未连接商业软件测试。
