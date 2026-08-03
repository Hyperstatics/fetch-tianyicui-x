# crafter-station/petdex 分析报告

- 仓库：[crafter-station/petdex](https://github.com/crafter-station/petdex)
- 方向：Codex 的动画伙伴画廊（Web 图库 + CLI + 桌面宠物）
- 主要语言：TypeScript（Next.js + Bun）
- 指标：⭐ 3,683 · License MIT · 最近推送 2026-08-03
- 主页/文档：[petdex.dev](https://petdex.dev)

> 分析基于 2026-08-04 抓取的 README 与目录结构。

## 这是什么（非技术版）

- **这是什么**：给 Codex 等编码 Agent 配的"桌面宠物"。一个网页画廊收集各种动画小宠物，一条命令安装到你的电脑，桌面上会浮一只小宠物，实时跟随你编码 Agent 的活动动起来。
- **能拿来干什么**：让编码过程更生动/有趣；给 Agent 加状态可视化。
- **适合谁**：开发者、喜欢桌面自定义的人。
- **快速判断**：如果你想让编码 Agent 更有"陪伴感"，它很可爱；功能上不是生产力工具。

## 分类

- 主分类：6. 特定领域 / 其他（桌面趣味应用/画廊）
- 副分类：1. 通用 Agent Runtime / Harness（Agent 状态可视化）
- 理由：README 自述 "The public gallery of animated companions for Codex... reacts to your coding agent's activity in real time"。

## 项目方向与定位

三件套：Web 画廊（社区提交/审核/展示 Codex sprite 格式宠物）、CLI（一条命令安装到 Codex）、桌面应用（屏幕上浮动宠物并实时响应 Agent 活动）。定位是 Agent 生态的趣味/情感层。

## 主要功能（能做什么）

- petdex.dev 社区画廊
- npm CLI 一键安装宠物
- 桌面宠物应用，实时反映编码 Agent 状态
- drizzle 数据库 + Next.js + packages 多包结构

## 架构设计

```text
packages/  多包（CLI/桌面/共享）
web（根）  Next.js 画廊站点
drizzle/   数据库 schema 与迁移
pets/      宠物资源
docs/ plans/
```

## 实现思路与核心逻辑

- 生态位切入：Codex 没有官方桌面宠物/状态可视化，Petdex 补位
- 社区驱动：画廊靠提交/审核运转，CLI 降低安装门槛

## 亮点

- 3.7k stars，增长快，差异化明显（趣味 + 情感化）
- 三端闭环（画廊/CLI/桌面）设计完整

## 局限与风险（可选）

- 非生产力工具，天花板有限
- 依赖 Codex 生态；桌面宠物性能/兼容性待观察
- 与"Agent Harness 内测"主题相关度低

## 分析说明

基于 README 与目录结构；未运行桌面应用。
