# CJackHwang/ds2api 分析报告

- 仓库：[CJackHwang/ds2api](https://github.com/CJackHwang/ds2api)
- 方向：把 DeepSeek Web 对话能力转换为 OpenAI / Claude / Gemini 兼容 API 的网关
- 主要语言：Go（核心）+ React（WebUI）
- 指标：⭐ 4,759 · License AGPL-3.0 · 最近推送 2026-08-03
- 主页/文档：[文档导航](https://github.com/CJackHwang/ds2api/blob/main/docs/README.md) · [架构说明](https://github.com/CJackHwang/ds2api/blob/main/docs/ARCHITECTURE.md)

> 分析基于 2026-08-04 抓取的 README、cmd/internal 结构与免责声明。许可证为 AGPL-3.0（copyleft，派生/网络服务分发需开源）。

## 这是什么（非技术版）

- **这是什么**：一个"API 翻译器"。把 DeepSeek 网页版聊天背后的能力包装成标准 API 格式（OpenAI/Claude/Gemini 都能调），方便程序/工具接入。
- **能拿来干什么**：让不支持 DeepSeek 的工具通过标准接口使用 DeepSeek 网页能力；自建中转服务。
- **适合谁**：开发者、想复用 DeepSeek Web 对话能力的个人/团队。
- **快速判断**：如果你有 DeepSeek 账号且想要标准 API 接入方式，它可以试；**注意项目免责声明：仅供学习研究，可能面临账号封禁等风险**。

## 分类

- 主分类：6. 特定领域 / 其他（API 网关/协议转换）
- 副分类：1. 通用 Agent Runtime / Harness（模型接入层）
- 理由：README 自述"将 DeepSeek Web 对话能力转换为 OpenAI、Claude 与 Gemini 兼容 API"。

## 项目方向与定位

针对"DeepSeek Web 好用但 API 受限/成本"的痛点，做协议桥接：Go 后端实现核心网关，Vercel 流式桥接用少量 Node Runtime，React WebUI 做管理台。Linux.do 社区热门项目，强调"仅限学习研究"。

## 主要功能（能做什么）

- 转换 DeepSeek Web 对话为 OpenAI / Claude / Gemini 兼容 API
- 流式响应（Vercel 桥接）；Docker / Zeabur / Vercel 部署
- WebUI 管理台（`webui/`，构建到 `static/admin`）
- 配置化（config.example.json）、文档完善

## 架构设计

```text
cmd/ internal/   Go 核心（网关、会话、协议转换）
api/ API.md      接口定义与文档
pow/  webui/     前端与构建
docker-compose.yml / Dockerfile  部署
```

## 实现思路与核心逻辑

- 核心是"会话复用 + 协议翻译"：维护 DeepSeek Web 会话，对外暴露标准 API 形态
- 流式桥接单独用 Node Runtime（Vercel 环境友好）
- 管理台与网关分离，部署方式多选

## 亮点

- 4.8k stars，Linux.do 社区高人气，Docker 一键部署
- 三种兼容协议覆盖广，工具生态接入成本低

## 局限与风险（可选）

- **AGPL-3.0 许可证**：派生分发需遵守 copyleft
- **合规风险**：使用网页能力做中转可能违反 DeepSeek 条款，README 已明确"账号封禁等风险自负"
- 依赖 DeepSeek Web 会话稳定性，接口可能随官方变化失效

## 分析说明

基于 README、目录结构、API 文档与免责声明；未运行服务，未细读 internal 全部源码。
