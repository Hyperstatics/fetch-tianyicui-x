# LING71671/open-reverselab 分析报告

- 仓库：[LING71671/open-reverselab](https://github.com/LING71671/open-reverselab)
- 方向：开源逆向工程实验室（178 篇知识库 + 100+ MCP 自动化工具）
- 主要语言：Python
- 指标：⭐ 969 · License GPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[README](https://github.com/LING71671/open-reverselab)

> 分析基于 2026-08-06 抓取的 README、kb/boards 结构与文档。

## 这是什么（非技术版）

- **这是什么**：一个"AI 逆向工程工作台"。覆盖 CTF 渗透、APK 反编译、PE 二进制分析、密码学与协议破解、游戏作弊分析；内置知识库路由和 100+ 工具，Agent 按"信号 → 知识 → 工具"自动干活。
- **能拿来干什么**：安全研究、逆向分析、CTF 解题；把逆向经验组织成可复用的知识库 + MCP 工具。
- **适合谁**：安全研究人员、逆向工程师、CTF 玩家。
- **快速判断**：如果你做逆向/安全分析且想要"Agent 化工具链"，它很有价值；否则用不上。

## 分类

- 主分类：6. 特定领域 / 其他（安全/逆向工程工具链）
- 副分类：2. Coding Harness / 工程向 Agent（Agent-native 工作流）
- 理由：README 自述 "Open-source reverse engineering lab... Agent-native, directory-as-convention"。

## 项目方向与定位

把逆向工程方法论固化为知识库（178 篇）+ MCP 工具（100+），按"目录即约定"组织：`Signal → kb_router → Attack chain → MCP tool mapping → Execution`。覆盖 CTF 网站/APK/PE/密码协议/游戏作弊五大类。

## 主要功能（能做什么）

- 知识库路由：按信号类型（HTTP/APK/PE/Crypto 等）路由到对应技术与工具
- 100+ MCP 自动化工具（http_probe、ghidra_headless、frida、rizin、x64dbg 等）
- boards/ 案例分析、gui/、exports/ 导出
- 免责声明与 AI 使用规范（DISCLAIMER/AI-USAGE）

## 架构设计

```text
kb/            知识库（分类技术文章，Scenario→Signal→Method→Chain→Tool）
boards/        场景/案例
gui/           界面
.mcp.json      工具服务
docs/ exports/ logs/
```

## 实现思路与核心逻辑

- 知识即路由：每个技术条目自带"输入信号 → 攻击链 → 工具映射"，Agent 按图索骥
- MCP 工具族：把 ghidra/frida/rizin 等封装为可调用工具
- 目录即约定：文件结构即路由规则，可扩展

## 亮点

- 安全逆向领域的 Agent 化工具链，定位稀缺
- 知识库规模（178 篇）与工具覆盖（100+）扎实
- GPL-3.0 开源 + 中文社区

## 局限与风险（可选）

- **GPL-3.0**：派生分发需遵守 copyleft
- 安全工具使用有法律/合规边界（README 有免责声明）
- 与"Agent Harness 内测"主题相关度中等（垂直领域工具链）

## 分析说明

基于 README、kb/boards 结构与文档；未运行工具。
