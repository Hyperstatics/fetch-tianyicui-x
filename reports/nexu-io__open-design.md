# nexu-io/open-design 分析报告

- 仓库：[nexu-io/open-design](https://github.com/nexu-io/open-design)
- 方向：开源的 Claude Design 替代品——agent-native 的本地优先设计工具
- 主要语言：TypeScript（+ 多平台原生组件）
- 指标：⭐ 83,388 · License Apache-2.0 · 最近推送 2026-08-03
- 主页/文档：[open-design.ai](https://open-design.ai/)

> 分析基于 2026-08-04 抓取的 README、目录树与产品文档；仓库约 1.7GB，未克隆，采用 API-only 分析。

## 这是什么（非技术版）

- **这是什么**：一个本地运行的开源"AI 设计师"。你描述需求，它直接生成网页、PPT、海报、视频动效等设计成品，产出的是真实可用的 HTML/PDF/MP4，而不是画布上的图。
- **能拿来干什么**：快速出原型、做品牌素材、生成可交付的设计稿；设计规范写在 `DESIGN.md` 里，AI 会一直按你的品牌风格产出。
- **适合谁**：设计师、产品经理、创业者、开发者；喜欢"用命令/对话驱动设计"的人。
- **快速判断**：如果你想要一个开箱即用、会按品牌规范批量出稿的设计工具，可以试；如果你只想要传统 Figma 式手动设计，不需要它。

## 分类

- 主分类：6. 特定领域 / 其他（AI 设计工具）
- 副分类：1. 通用 Agent Runtime / Harness（依托编码 Agent CLI）
- 理由：README 自述 "open-source Claude Design alternative"、"agent-native loop"，通过 25+ CLI 编码 Agent 驱动。

## 项目方向与定位

"你的 CLI 变成设计引擎，你的电脑变成设计工作室"。把 Anthropic Claude Design 的 agent-native 工作流（brief → 锁定方向 → 流式产出 → 评审 → 交付）开源化，用"可被 Agent 读写的技能文件系统"替代封闭画布。定位是 Figma 的 Agent 时代替代品 + 本地优先桌面应用（macOS/Windows）。

## 主要功能（能做什么）

- 生成 web / desktop / mobile 原型、live dashboards/artifacts、PPT、图片、视频、HyperFrames 动效
- 品牌级 `DESIGN.md` 设计系统 + 可组合 skills + 即装即用 plugins
- 沙箱 iframe 预览；导出 HTML / PDF / PPTX / MP4
- 支持 Claude Code、Codex、Cursor、OpenCode、Qwen、Copilot 等 25+ CLI 编码 Agent，以及任意 OpenAI 兼容端点（BYOK）
- Open Design Cloud：官方模型服务（GPT/Claude/Gemini/DeepSeek，按 token 计费）
- Fellow 计划、多语言文档、PRIVACY.md 等治理文件

## 架构设计

```text
apps/ (desktop, web, daemon, packaged, landing-page)
craft/   功能 skills / 设计模板 / plugins（以文件系统形式暴露给 Agent）
clipper/ 素材采集
data/   资源与数据
deploy/ 部署
```

- 核心思想：设计能力 = 可读写的文件（skills、渲染模板、设计系统、插件），编码 Agent 直接读写，无需专属 UI 协议
- 多端：桌面应用 + Web + daemon + 打包产物

## 实现思路与核心逻辑

- agent-native loop：把"发现简报 → 锁定方向 → 流式产出 → 评审批评 → 交付"变成可执行循环
- 设计即代码：产出真实 CSS/字体/组件，导出即交付物；`DESIGN.md` 作为团队品牌契约被 Agent 读取
- 多 Agent 兼容：适配 25+ CLI 与 OpenAI 兼容协议，避免绑定单一宿主

## 亮点

- 83k stars，是"开源 Claude Design"赛道的头号项目，增长极快
- 本地优先 + 沙箱预览 + 多格式导出，交付闭环完整
- 技能/设计系统文件化，可复用、可版本管理、可团队共享
- 官方云服务（按量计费）+ 开源核心并行，商业模式清晰

## 局限与风险（可选）

- 仓库约 1.7GB，体积巨大，安装/分发成本高
- 强依赖外部编码 Agent CLI 作为执行引擎
- 开源核心与收费云服务的边界需自行评估；新功能迭代快，稳定性待观察
- 与帖子"Agent Harness 内测"主题相关性一般（偏设计应用层）

## 分析说明

API-only 分析（元数据 + README + 目录树），未克隆源码，未验证运行时行为。
