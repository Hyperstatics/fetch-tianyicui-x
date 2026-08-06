# 仓库分析索引

> 由 `reports/SUMMARY.csv` 与 259 份分析报告生成。每份报告包含：这是什么（非技术版）、分类、方向定位、功能、架构、实现思路、亮点、局限。

## 总览

- 报告总数：259
- 汇总 Star：551,303

### 分类分布

| 分类 | 数量 |
| --- | ---: |
| 6. 特定领域 / 其他 | 89 |
| 1. 通用 Agent Runtime / Harness / 桌面客户端 | 76 |
| 2. Coding Harness / 工程向 Agent | 49 |
| 3. 多 Agent 编排 / 协作系统 | 24 |
| 4. 记忆 / 上下文 / 知识管理 | 17 |
| 5. 评测 / Benchmark 工具 | 4 |

### 许可证分布

| 类型 | 数量 |
| --- | ---: |
| 宽松许可 | 175 |
| 无许可证/待核对 | 42 |
| 强 copyleft | 23 |
| 非商用 | 6 |
| 自定义/分层 | 5 |
| BSL（商用受限） | 4 |
| 弱 copyleft | 1 |
| 宽松（CC） | 1 |
| 待核对 | 1 |
| 非商用（CC） | 1 |

> 完整许可证明细见 [LICENSE-notes.csv](LICENSE-notes.csv)；非宽松许可项目已单独标注。

## 6. 特定领域 / 其他（89）

| 仓库 | ⭐ | 方向 | 报告 |
| --- | ---: | --- | --- |
| [nexu-io/open-design](https://github.com/nexu-io/open-design) | 83,388 | "你的 CLI 变成设计引擎，你的电脑变成设计工作室"。把 Anthropic Claude Design 的 agen | [nexu-io/open-design](reports/nexu-io__open-design.md) |
| [readest/readest](https://github.com/readest/readest) | 23,050 | 用现代技术栈重写经典阅读器 Foliate：Next.js 16 + Tauri v2，覆盖 macOS/Windows | [readest/readest](reports/readest__readest.md) |
| [web-infra-dev/midscene](https://github.com/web-infra-dev/midscene) | 14,477 | 字节跳动 web-infra 团队出品的视觉驱动自动化框架：以多模态模型"看截图"理解界面，替代传统 DOM 选择器/坐 | [web-infra-dev/midscene](reports/web-infra-dev__midscene.md) |
| [hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome) | 12,248 |  | [hangwin/mcp-chrome](reports/hangwin__mcp-chrome.md) |
| [tt-a1i/archify](https://github.com/tt-a1i/archify) | 8,809 | 把"架构文档/代码库"转化为**可交互、可信任、可分享**的系统地图：5 种技术图类型、4 种视觉预设、深色/浅色主题、 | [tt-a1i/archify](reports/tt-a1i__archify.md) |
| [crisxuan/bestJavaer](https://github.com/crisxuan/bestJavaer) | 6,615 | cxuan-ai-labs：记录"实际试过什么、哪里坏了、怎么修"的 AI 编码实践实验室——明确不是新闻聚合、也不是教 | [crisxuan/bestJavaer](reports/crisxuan__bestJavaer.md) |
| [DerekYRC/mini-spring](https://github.com/DerekYRC/mini-spring) | 6,371 | 抽取 Spring 核心逻辑、极度简化、保留功能：IoC、AOP、资源加载、事件监听、类型转换、容器扩展点、Bean 生 | [DerekYRC/mini-spring](reports/DerekYRC__mini-spring.md) |
| [drakeet/MultiType](https://github.com/drakeet/MultiType) | 5,759 | 解决 RecyclerView 多类型列表的样板代码问题：用 `ItemViewDelegate` 注册机制，新增 it | [drakeet/MultiType](reports/drakeet__MultiType.md) |
| [CJackHwang/ds2api](https://github.com/CJackHwang/ds2api) | 4,759 | 针对"DeepSeek Web 好用但 API 受限/成本"的痛点，做协议桥接：Go 后端实现核心网关，Vercel 流 | [CJackHwang/ds2api](reports/CJackHwang__ds2api.md) |
| [MaaXYZ/MaaFramework](https://github.com/MaaXYZ/MaaFramework) | 4,583 | MAA 团队（明日方舟助手）开源的核心框架：用图像识别做黑盒 UI 自动化，提供 C++20 核心 + Python/N | [MaaXYZ/MaaFramework](reports/MaaXYZ__MaaFramework.md) |
| [ZSeven-W/openpencil](https://github.com/ZSeven-W/openpencil) | 4,582 | 区别于 Figma 兼容的另一个同名项目：本仓库专注 **AI-native design-to-code**——设计产 | [ZSeven-W/openpencil](reports/ZSeven-W__openpencil.md) |
| [binaricat/Netcatty](https://github.com/binaricat/Netcatty) | 4,576 | 把 SSH 工作台与 AI Agent 结合：Electron + React + xterm.js 构建，内置 AI  | [binaricat/Netcatty](reports/binaricat__Netcatty.md) |
| [oomol-lab/open-connector](https://github.com/oomol-lab/open-connector) | 4,178 | "Connect once. Use everywhere."——用户账号授权一次，向 Agent 和应用暴露统一目录（ | [oomol-lab/open-connector](reports/oomol-lab__open-connector.md) |
| [crafter-station/petdex](https://github.com/crafter-station/petdex) | 3,683 | 三件套：Web 画廊（社区提交/审核/展示 Codex sprite 格式宠物）、CLI（一条命令安装到 Codex）、 | [crafter-station/petdex](reports/crafter-station__petdex.md) |
| [XiaoMi/xiaomi-miloco](https://github.com/XiaoMi/xiaomi-miloco) | 3,185 | Miloco 2.0 重构为 OpenClaw 插件：以米家摄像头音视频为全模态感知入口、MiMo 大模型为大脑，编排全 | [XiaoMi/xiaomi-miloco](reports/XiaoMi__xiaomi-miloco.md) |
| [kubeovn/kube-ovn](https://github.com/kubeovn/kube-ovn) | 2,362 | 把 OVN（Open vSwitch 的虚拟网络）与 Kubernetes 深度集成，提供 VPC 多租户、Namesp | [kubeovn/kube-ovn](reports/kubeovn__kube-ovn.md) |
| [compio-rs/compio](https://github.com/compio-rs/compio) | 1,823 | thread-per-core 异步运行时，直接对标 monoio/tokio 系列的高性能路线：每个核心一个线程、任务 | [compio-rs/compio](reports/compio-rs__compio.md) |
| [tddworks/baguette](https://github.com/tddworks/baguette) | 1,596 | 单 Swift CLI（`baguette`）+ 自带 Web UI，无头控制 iOS 模拟器：设备启动、60fps 屏 | [tddworks/baguette](reports/tddworks__baguette.md) |
| [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | 1,590 | 纯本地、私有、开源的自进化跨平台内容发现 Agent：从跨平台使用/反馈/对话中持续深化心理画像，主动去 B 站/小红书 | [whiteguo233/OpenBiliClaw](reports/whiteguo233__OpenBiliClaw.md) |
| [Vizards/deepseek-v4-for-copilot](https://github.com/Vizards/deepseek-v4-for-copilot) | 1,276 | "Don't replace Copilot — power it up."：不换界面，只往模型选择器里加 DeepSe | [Vizards/deepseek-v4-for-copilot](reports/Vizards__deepseek-v4-for-copilot.md) |
| [platonai/Browser4](https://github.com/platonai/Browser4) | 1,095 | 模块化浏览器自动化平台：core/apps/agentic/pdk（插件开发包）/plugins/rest 分层；支持交 | [platonai/Browser4](reports/platonai__Browser4.md) |
| [QuantumBFS/Yao.jl](https://github.com/QuantumBFS/Yao.jl) | 1,037 | Yao（"幺"）是 Julia 生态的量子计算框架，服务于量子算法设计、量子软件 2.0 与量子计算教育。early-r | [QuantumBFS/Yao.jl](reports/QuantumBFS__Yao.jl.md) |
| [LING71671/open-reverselab](https://github.com/LING71671/open-reverselab) | 969 | 把逆向工程方法论固化为知识库（178 篇）+ MCP 工具（100+），按"目录即约定"组织：`Signal → kb_ | [LING71671/open-reverselab](reports/LING71671__open-reverselab.md) |
| [xuzhougeng/wisp-science](https://github.com/xuzhougeng/wisp-science) | 859 | AI 科研助手 + 科学计算工作台：OpenAI/Anthropic 兼容模型、本地/WSL/SSH/GPU 的持久 P | [xuzhougeng/wisp-science](reports/xuzhougeng__wisp-science.md) |
| [xlang-ai/OpenCUA](https://github.com/xlang-ai/OpenCUA) | 809 | 为 Computer-Use Agent 提供开放基础：OpenCUA 系列模型（7B/32B/72B）、AgentNe | [xlang-ai/OpenCUA](reports/xlang-ai__OpenCUA.md) |
| [Cai-aa/CAE-Agent-Hub](https://github.com/Cai-aa/CAE-Agent-Hub) | 670 | 让 AI 编码客户端（Codex/Cursor/Claude Code/Claude Desktop）与真实 CAE 工 | [Cai-aa/CAE-Agent-Hub](reports/Cai-aa__CAE-Agent-Hub.md) |
| [QmiAI/Qmedia](https://github.com/QmiAI/Qmedia) | 629 | 面向创作者的内容搜索与解析：检索图文/短视频素材，AI 分析并整合信息，输出内容卡片与来源。服务端 mm_server  | [QmiAI/Qmedia](reports/QmiAI__Qmedia.md) |
| [YoungCan-Wang/WyckoffTradingAgent](https://github.com/YoungCan-Wang/WyckoffTradingAgent) | 558 | 自然语言驱动的威科夫分析自动化链路：日线行情（TickFlow 实时拉取）、威科夫结构识别、AI 研报、持仓风控、形态复 | [YoungCan-Wang/WyckoffTradingAgent](reports/YoungCan-Wang__WyckoffTradingAgent.md) |
| [eunomia-bpf/agentsight](https://github.com/eunomia-bpf/agentsight) | 556 | 无 SDK、无代理、无厂商集成：用 eBPF + TLS 流量追踪观测 Claude Code、Codex、Gemini | [eunomia-bpf/agentsight](reports/eunomia-bpf__agentsight.md) |
| [Orkas-AI/Orkas-VideoStudio](https://github.com/Orkas-AI/Orkas-VideoStudio) | 520 | "不是黑盒视频 Agent"：视频 = 可读、可 diff、可重渲的 plan.json。项目提供知识（什么是好视频、走 | [Orkas-AI/Orkas-VideoStudio](reports/Orkas-AI__Orkas-VideoStudio.md) |
| [anymouschina/TapCanvas](https://github.com/anymouschina/TapCanvas) | 502 | 画布式连续生产：文本/图像/视频/分镜在单一画布流转；Agents 编排、多模型接入、项目化资产沉淀。有独立 AI 运行 | [anymouschina/TapCanvas](reports/anymouschina__TapCanvas.md) |
| [GitHubxsy/nanoAgent](https://github.com/GitHubxsy/nanoAgent) | 494 | 三套系列：从零理解大模型（Token/Embedding/Attention/Transformer/训练/推理/Sca | [GitHubxsy/nanoAgent](reports/GitHubxsy__nanoAgent.md) |
| [flashrt-project/FlashRT](https://github.com/flashrt-project/FlashRT) | 480 | 手写内核库组成静态图（无 ONNX/无编译/无按驱动重建）：norm/激活/融合/RoPE/FP8/NVFP4 GEMM | [flashrt-project/FlashRT](reports/flashrt-project__FlashRT.md) |
| [bex-co/bex](https://github.com/bex-co/bex) | 415 | AI 原生的自托管部署平台：Git → HTTPS，开发者与编码 Agent 统一控制面。CLI + dashboard | [bex-co/bex](reports/bex-co__bex.md) |
| [addsumtech/slides_maker](https://github.com/addsumtech/slides_maker) | 357 | "reads your actual work, never invents a number, ships fully | [addsumtech/slides_maker](reports/addsumtech__slides_maker.md) |
| [physiclaw/PhysiClaw](https://github.com/physiclaw/PhysiClaw) | 294 | 把"屏幕当 API"：摄像头读屏、触控笔做手势，对手机来说与真人手指无异（无指纹、难以检测）。面向无公开 API 的日常 | [physiclaw/PhysiClaw](reports/physiclaw__PhysiClaw.md) |
| [sigcli/sigcli](https://github.com/sigcli/sigcli) | 279 | 解决"Agent 需要访问工作系统但凭据不能进 shell history/环境变量/上下文"的问题：sig 做浏览器  | [sigcli/sigcli](reports/sigcli__sigcli.md) |
| [gupsammy/Claudest](https://github.com/gupsammy/Claudest) | 269 | 精选型 Claude Code 插件市场：claude-memory、claude-research、claude-co | [gupsammy/Claudest](reports/gupsammy__Claudest.md) |
| [helixnow/deep-student](https://github.com/helixnow/deep-student) | 236 | "不是学习难，是学习工具太散"：研究笔记本 + 知识工作区 + 思维导图 + 练习 + 翻译一体化，共享学习数据与工作流 | [helixnow/deep-student](reports/helixnow__deep-student.md) |
| [chainreactors/aiscan](https://github.com/chainreactors/aiscan) | 234 | LLM Agent + 传统安全扫描引擎：Scan（确定性流水线 + 可选 AI 辅助）、Agent（自然语言自主评估） | [chainreactors/aiscan](reports/chainreactors__aiscan.md) |
| [mainline-org/mainline](https://github.com/mainline-org/mainline) | 181 | 把工程判断层加入 Git：原始目标、推理路径、关键决策、权衡、验证、显式约束、放弃路线、承载提交。Hosted Hub  | [mainline-org/mainline](reports/mainline-org__mainline.md) |
| [cloudwego/dynamicgo](https://github.com/cloudwego/dynamicgo) | 180 | 字节跳动 CloudWeGo 生态的序列化加速库：运行时解析 Thrift IDL、通用处理 Thrift/Protob | [cloudwego/dynamicgo](reports/cloudwego__dynamicgo.md) |
| [2921323707/CPA_Orbit](https://github.com/2921323707/CPA_Orbit) | 88 | 本地优先的 AI 订阅控制面：订阅/供应商归档、账户健康、价格情报、CPA/Sub2API 伙伴。Wails 桌面（Wi | [2921323707/CPA_Orbit](reports/2921323707__CPA_Orbit.md) |
| [libra-tools/libra](https://github.com/libra-tools/libra) | 80 | Git 兼容、可渐进采用：与 Claude Code/Codex/Gemini CLI 等配合，记录开发上下文/Agen | [libra-tools/libra](reports/libra-tools__libra.md) |
| [PzMNo1/PzMCiphertool](https://github.com/PzMNo1/PzMCiphertool) | 74 | 个人 Agent 工具箱：Redis + Spring Boot 后端 + http-server 前端（另有 Rust | [PzMNo1/PzMCiphertool](reports/PzMNo1__PzMCiphertool.md) |
| [kuangre123/codex-switch](https://github.com/kuangre123/codex-switch) | 58 | 解决 Codex provider 切换痛点：官方与自定义 provider 同时保留在配置，切换只改默认路由；内置国内 | [kuangre123/codex-switch](reports/kuangre123__codex-switch.md) |
| [QuantumBFS/quantum.harness](https://github.com/QuantumBFS/quantum.harness) | 57 | 专家驱动的方法库 + Agent 技能：模型卡（Hamiltonian/对称性）、数值方法与工具使用技能（参数配置/资源 | [QuantumBFS/quantum.harness](reports/QuantumBFS__quantum.harness.md) |
| [Tainyusz/Voice-Phone-Agent](https://github.com/Tainyusz/Voice-Phone-Agent) | 46 | Web 语音 → 模型识别 → 指令规划 → ADB 执行闭环；无线调试、敏感操作确认与人工接管；基于并集成 Open- | [Tainyusz/Voice-Phone-Agent](reports/Tainyusz__Voice-Phone-Agent.md) |
| [UniversePeak/Supervisor.skill](https://github.com/UniversePeak/Supervisor.skill) | 41 | 导师 Skill 生成：Method Core + Academic Style + Persona + Graduat | [UniversePeak/Supervisor.skill](reports/UniversePeak__Supervisor.skill.md) |
| [CodingThrust/problem-reductions](https://github.com/CodingThrust/problem-reductions) | 34 | 100+ 问题与归约规则库 + 自动归约路径搜索 + pred CLI；PDF 手册含理论与证明。 | [CodingThrust/problem-reductions](reports/CodingThrust__problem-reductions.md) |
| [peisp/catdb](https://github.com/peisp/catdb) | 28 | Wails v3 + Vue 3 桌面数据库工具：编译期注册驱动插件扩展数据库支持。 | [peisp/catdb](reports/peisp__catdb.md) |
| [Zane456/PCB-Agent-Teams](https://github.com/Zane456/PCB-Agent-Teams) | 27 | KiCad 10 多项目 PCB 工作区：10 个 skills 驱动 Phase 0–5 管道（拓扑讨论 → Gerb | [Zane456/PCB-Agent-Teams](reports/Zane456__PCB-Agent-Teams.md) |
| [xaixapi/xai](https://github.com/xaixapi/xai) | 26 | 文档型仓库：XAI 路由服务架构说明，强调 BYOK、零加价、端到端加密。 | [xaixapi/xai](reports/xaixapi__xai.md) |
| [byewind1/openbrep](https://github.com/byewind1/openbrep) | 23 | AI 辅助 ArchiCAD/GDL 开发：编译验证、知识驱动、资产可追溯；桌面包 + CLI/pipx 双形态。 | [byewind1/openbrep](reports/byewind1__openbrep.md) |
| [rustscript-lang/rustscript](https://github.com/rustscript-lang/rustscript) | 18 | 脚本语言 RustScript + RSS 语言 + pd-vm：VM、编译器、标准库、字节码/AOT、WASM、调试契 | [rustscript-lang/rustscript](reports/rustscript-lang__rustscript.md) |
| [Octo-o-o-o/deepseek-harness-applicants](https://github.com/Octo-o-o-o/deepseek-harness-applicants) | 15 | 开发者为中心的数据工程：X 身份 → GitHub 身份 → 代表项目；项目是证据而非主实体；保留不确定性（unlink | [Octo-o-o-o/deepseek-harness-applicants](reports/Octo-o-o-o__deepseek-harness-applicants.md) |
| [vst93/ttm](https://github.com/vst93/ttm) | 11 | Bubble Tea 终端 SSH 书签管理器：管理/同步/连接，跨平台（Linux/macOS/Windows/And | [vst93/ttm](reports/vst93__ttm.md) |
| [termlnk/termlnk](https://github.com/termlnk/termlnk) | 10 | 现代可扩展终端：SSH/SFTP + 内置 AI + 片段 + 端口转发 + 跨设备同步 + 主题 + 扩展，跨平台多语 | [termlnk/termlnk](reports/termlnk__termlnk.md) |
| [yuanchenglu/llm-harness-agent](https://github.com/yuanchenglu/llm-harness-agent) | 7 | 研究知识库：模型能力≠产品能力；Harness 放大或引入错误；需基于固定源码、协议测试和任务 benchmark 评估 | [yuanchenglu/llm-harness-agent](reports/yuanchenglu__llm-harness-agent.md) |
| [zhuangbiaowei/smart_prompt](https://github.com/zhuangbiaowei/smart_prompt) | 7 | Ruby LLM DSL：OpenAI 兼容 + Claude 原生（多模态）、clean/composable/cus | [zhuangbiaowei/smart_prompt](reports/zhuangbiaowei__smart_prompt.md) |
| [CNife/pi-extensions](https://github.com/CNife/pi-extensions) | 6 | pi 扩展生态：产品/个人/退役三层，workspaces 分发。 | [CNife/pi-extensions](reports/CNife__pi-extensions.md) |
| [arcabotai/clawfix](https://github.com/arcabotai/clawfix) | 6 | OpenClaw 诊断：本地扫描、secret 脱敏、确定性规则匹配、可选 AI 解释；安全原则（AI 输出不执行 sh | [arcabotai/clawfix](reports/arcabotai__clawfix.md) |
| [liaocaoxuezhe/FigmaX](https://github.com/liaocaoxuezhe/FigmaX) | 6 | 跨 AI 客户端 Skill：Figma 官方 MCP（读：解析 URL/截图/设计令牌）+ figma_editor  | [liaocaoxuezhe/FigmaX](reports/liaocaoxuezhe__FigmaX.md) |
| [clubmatto/vetrina](https://github.com/clubmatto/vetrina) | 5 | 多项目 monorepo：ai-kit、fakedata 等，Homebrew Formula、CI。 | [clubmatto/vetrina](reports/clubmatto__vetrina.md) |
| [wcq-glhf/prex-quant](https://github.com/wcq-glhf/prex-quant) | 5 | 开源客户端：开放量化工作流、API 协议（openapi.yaml）、调用示例与报告工具；回测引擎在 PREX 服务端。 | [wcq-glhf/prex-quant](reports/wcq-glhf__prex-quant.md) |
| [JameryW/XhsGrowthAgent](https://github.com/JameryW/XhsGrowthAgent) | 4 | 小红书垂直增长 Agent：LangGraph 多 Agent、内容生命周期自动化、Demo + API/backend | [JameryW/XhsGrowthAgent](reports/JameryW__XhsGrowthAgent.md) |
| [ZhenHuangLab/pi-xai-search](https://github.com/ZhenHuangLab/pi-xai-search) | 4 | pi 的 X 实时搜索扩展：轻量（0.1MB）、npm 分发、CI。 | [ZhenHuangLab/pi-xai-search](reports/ZhenHuangLab__pi-xai-search.md) |
| [Chasen-Liao/SuperMew](https://github.com/Chasen-Liao/SuperMew) | 3 | 实验场：LangChain Agent + LangGraph RAG；Milvus 依赖（docker-compose | [Chasen-Liao/SuperMew](reports/Chasen-Liao__SuperMew.md) |
| [dothinkerlab/AgentMeter](https://github.com/dothinkerlab/AgentMeter) | 3 | Apple Watch 应用：AI 编码配额监控；App Store 分发。 | [dothinkerlab/AgentMeter](reports/dothinkerlab__AgentMeter.md) |
| [shuwenhe/neurx](https://github.com/shuwenhe/neurx) | 3 | S 语言 AI 框架：模型/张量原语、自动微分、分布式训练、推理服务、CUDA + Ascend CANN。 | [shuwenhe/neurx](reports/shuwenhe__neurx.md) |
| [PaRr0tBoY/Pola-Agent](https://github.com/PaRr0tBoY/Pola-Agent) | 2 | SolidWorks 垂直 Agent：COM 驱动、AI 建模、标准件库；Windows 环境。 | [PaRr0tBoY/Pola-Agent](reports/PaRr0tBoY__Pola-Agent.md) |
| [shuwenhe/s](https://github.com/shuwenhe/s) | 2 | 自举系统语言：种子编译器、前端/后端、运行时、stdlib、架构支持。 | [shuwenhe/s](reports/shuwenhe__s.md) |
| [yuanchenglu/oh-my-deepseek-harness](https://github.com/yuanchenglu/oh-my-deepseek-harness) | 2 | Hermes + DeepSeek 集成插件：mcp/packages/plugins 分层，兼容基线 Hermes v | [yuanchenglu/oh-my-deepseek-harness](reports/yuanchenglu__oh-my-deepseek-harness.md) |
| [Techdoll00/aicompass](https://github.com/Techdoll00/aicompass) | 1 | 基于 Morphic 定制：中文知识工作流 + 学生友好搜索模式；Vercel OSS。 | [Techdoll00/aicompass](reports/Techdoll00__aicompass.md) |
| [XvHaoR/fittracker](https://github.com/XvHaoR/fittracker) | 1 | 本地优先健身 App：训练/饮食/跑步跟踪 + AI，SQLite 本地存储。 | [XvHaoR/fittracker](reports/XvHaoR__fittracker.md) |
| [YuYingRay/LaoYu-Professional-Screenwriter](https://github.com/YuYingRay/LaoYu-Professional-Screenwriter) | 1 | 结构化编剧工作流：governance/control-plane-contract.md 为唯一规范源；agents/ | [YuYingRay/LaoYu-Professional-Screenwriter](reports/YuYingRay__LaoYu-Professional-Screenwriter.md) |
| [ale-160/web-text](https://github.com/ale-160/web-text) | 1 | 本地优先在线 MD 编辑器：Next.js，数据不离开浏览器。 | [ale-160/web-text](reports/ale-160__web-text.md) |
| [liaocaoxuezhe/ChromeX](https://github.com/liaocaoxuezhe/ChromeX) | 1 | 本地浏览器自动化：MCP Server（26 工具）+ Chrome 扩展（Manifest V3，chrome.deb | [liaocaoxuezhe/ChromeX](reports/liaocaoxuezhe__ChromeX.md) |
| [minmengxhw-cpu/mingmeng-history-research](https://github.com/minmengxhw-cpu/mingmeng-history-research) | 1 | 内部研究工作台：7 大境外档案系统 + 国内史料层；抓取/清洗/翻译/全文索引/引用/事件梳理/研究卡片。 | [minmengxhw-cpu/mingmeng-history-research](reports/minmengxhw-cpu__mingmeng-history-research.md) |
| [oliverzhu823/vizruna](https://github.com/oliverzhu823/vizruna) | 1 | Pi Agent 可视化：可见/可控/可复核；e2e 测试。 | [oliverzhu823/vizruna](reports/oliverzhu823__vizruna.md) |
| [yuelangmanle/plankton](https://github.com/yuelangmanle/plankton) | 1 | 多端工具：Web 原型 + Android 主 App + 语音助手；本地优先。 | [yuelangmanle/plankton](reports/yuelangmanle__plankton.md) |
| [249469326i-lang/api-monitor](https://github.com/249469326i-lang/api-monitor) | 0 | 桌面 API 监控：定时测速、故障切换、密钥加密、托盘常驻。 | [249469326i-lang/api-monitor](reports/249469326i-lang__api-monitor.md) |
| [CisaSettle/bluffking](https://github.com/CisaSettle/bluffking) | 0 | 扑克引擎 + mental poker：audits/ 安全审计、blog。 | [CisaSettle/bluffking](reports/CisaSettle__bluffking.md) |
| [DerekYRC/DerekYRC](https://github.com/DerekYRC/DerekYRC) | 0 | 个人主页：展示联系方式与背景。 | [DerekYRC/DerekYRC](reports/DerekYRC__DerekYRC.md) |
| [Drinkwater0922/workhorse-ai](https://github.com/Drinkwater0922/workhorse-ai) | 0 | 单机 MVP：FastAPI + SQLite + 沙箱 + OpenRouter 多模型。 | [Drinkwater0922/workhorse-ai](reports/Drinkwater0922__workhorse-ai.md) |
| [IT-Bill/what-the-health](https://github.com/IT-Bill/what-the-health) | 0 | 健康管理 Web 应用：现代技术栈（Next 16/pgvector/Prisma/AI Chat/ASR）。 | [IT-Bill/what-the-health](reports/IT-Bill__what-the-health.md) |
| [JackWPP/fox-say](https://github.com/JackWPP/fox-say) | 0 | 学习/考试辅助 + 文档解析研究。 | [JackWPP/fox-say](reports/JackWPP__fox-say.md) |
| [XiaoWeiKIN/RepoFoundryAI](https://github.com/XiaoWeiKIN/RepoFoundryAI) | 0 | Agent-native 工程：engineering-benchmark/case-study/execution-p | [XiaoWeiKIN/RepoFoundryAI](reports/XiaoWeiKIN__RepoFoundryAI.md) |
| [vst93/floter](https://github.com/vst93/floter) | 0 | 悬浮终端 + 启动器：快捷键唤出、模糊/拼音搜索、Action bar、多显示器。 | [vst93/floter](reports/vst93__floter.md) |

## 1. 通用 Agent Runtime / Harness / 桌面客户端（76）

| 仓库 | ⭐ | 方向 | 报告 |
| --- | ---: | --- | --- |
| [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | 13,885 | 把 Claude Code 的能力封装成跨平台桌面工作区（macOS/Windows/Linux），并在终端之外补齐：会 | [NanmiCoder/cc-haha](reports/NanmiCoder__cc-haha.md) |
| [YaoApp/yao](https://github.com/YaoApp/yao) | 7,557 | 核心理念："cage, not an animal"——AI 是动物，运行时是笼子；行为由笼子（Hook/边界）决定。Y | [YaoApp/yao](reports/YaoApp__yao.md) |
| [op7418/CodePilot](https://github.com/op7418/CodePilot) | 6,339 | 多提供商统一桌面界面：17+ AI 提供商开箱即用，对话中途切换模型/提供商不丢上下文；MCP 与 Skills 扩展； | [op7418/CodePilot](reports/op7418__CodePilot.md) |
| [ThinkInAIXYZ/deepchat](https://github.com/ThinkInAIXYZ/deepchat) | 6,187 | 围绕 Tape.systems 理念（会话录制/回放/恢复）构建的本地优先 Agent 客户端：兼容任意 OpenAI/ | [ThinkInAIXYZ/deepchat](reports/ThinkInAIXYZ__deepchat.md) |
| [liliMozi/openhanako](https://github.com/liliMozi/openhanako) | 5,730 | 弥合普通人与 Agent 的缝隙：不做"只属于命令行"的工具，强化 Agent 的"人味"（记忆 + 人格）与办公场景工 | [liliMozi/openhanako](reports/liliMozi__openhanako.md) |
| [KunAgent/Kun](https://github.com/KunAgent/Kun) | 5,635 | "不是另一个只会生成回答的聊天框"：Kun 把需求、上下文、计划、文件改动、测试、审查与最终交付放进一条连续工作流。桌面 | [KunAgent/Kun](reports/KunAgent__Kun.md) |
| [nextlevelbuilder/goclaw](https://github.com/nextlevelbuilder/goclaw) | 3,502 | 生产级多租户 AI 网关：单二进制、20+ LLM 提供商、7 个渠道（含 WebSocket/浏览器/CLI 等）、多 | [nextlevelbuilder/goclaw](reports/nextlevelbuilder__goclaw.md) |
| [EverMind-AI/Raven](https://github.com/EverMind-AI/Raven) | 3,494 | 基于 EverOS（持久用户记忆/Agent 记忆/世界知识）构建的自我改进 Harness：跨会话持续优化工具、技能、 | [EverMind-AI/Raven](reports/EverMind-AI__Raven.md) |
| [OpenMinis/OpenMinis](https://github.com/OpenMinis/OpenMinis) | 3,084 | 把"给 AI 一台真电脑"做到移动端：设备内沙箱 Alpine Linux（可装包/跑脚本/操作文件）、浏览器自动化、设 | [OpenMinis/OpenMinis](reports/OpenMinis__OpenMinis.md) |
| [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | 1,969 | 轻量状态内核 + Agent 无关的本地控制面：让 Codex、Claude Code、Cursor 或自研运行时在"有 | [huangruiteng/loopx](reports/huangruiteng__loopx.md) |
| [proma-ai/Proma](https://github.com/proma-ai/Proma) | 1,895 | "不是只面向闲聊的聊天框，而是长期沉淀个人工作流的 Agent 工作台"：简单问题 Chat、复杂任务 Agent；内置 | [proma-ai/Proma](reports/proma-ai__Proma.md) |
| [makecindy/cindy](https://github.com/makecindy/cindy) | 1,779 | "Consider it done."——开箱即用的开源 Agent 客户端：首个支持 Claude Code 与 Co | [makecindy/cindy](reports/makecindy__cindy.md) |
| [maka-agent/maka-agent](https://github.com/maka-agent/maka-agent) | 1,210 | 以"执行事实（recoverable execution facts）"为核心的 Agent 工作台：模型消息、工具调用 | [maka-agent/maka-agent](reports/maka-agent__maka-agent.md) |
| [ShenSeanChen/waku-agent](https://github.com/ShenSeanChen/waku-agent) | 895 | "Your own AI assistant. On your laptop. In code you can read | [ShenSeanChen/waku-agent](reports/ShenSeanChen__waku-agent.md) |
| [hAcKlyc/MyAgents](https://github.com/hAcKlyc/MyAgents) | 787 | 把对话、工作区、文件、工具、模型、任务和长期记忆放进同一桌面系统。三大块：本地优先客户端（多标签/文件树/内嵌终端/内嵌 | [hAcKlyc/MyAgents](reports/hAcKlyc__MyAgents.md) |
| [AQBot-Desktop/AQBot](https://github.com/AQBot-Desktop/AQBot) | 737 | 多语言（中/英/日/韩/法/德等）AI 桌面客户端：对话与模型管理、知识库、记忆、Agent 询问与权限审批、API 网 | [AQBot-Desktop/AQBot](reports/AQBot-Desktop__AQBot.md) |
| [basionwang-bot/HermesPet](https://github.com/basionwang-bot/HermesPet) | 592 | 原生 macOS AI 桌宠 + 任务控制面：7 类 AI 终端接入、实时系统诊断、多任务并行、手机配套端规划。Appl | [basionwang-bot/HermesPet](reports/basionwang-bot__HermesPet.md) |
| [SII-Holos/synergy](https://github.com/SII-Holos/synergy) | 540 | 以"持久、可恢复"为核心的开源工作区：软件与知识工作的统一运行时，会话/代理/文件/浏览器/工具/自动化互联。MIT 开 | [SII-Holos/synergy](reports/SII-Holos__synergy.md) |
| [RongleCat/grok-app](https://github.com/RongleCat/grok-app) | 531 | 为本地 grok CLI 提供桌面工作台：会话、项目、媒体、自动化管理；Tauri 2 三平台（macOS/Window | [RongleCat/grok-app](reports/RongleCat__grok-app.md) |
| [xicilion/boxsh](https://github.com/xicilion/boxsh) | 328 | 基于 dash 的沙箱 shell + MCP server：OS 原生沙箱（Linux namespaces/secc | [xicilion/boxsh](reports/xicilion__boxsh.md) |
| [mkurman/zorai](https://github.com/mkurman/zorai) | 321 | 持久多 Agent 执行平台：daemon 拥有工作/记忆/审批/工具/长期目标；运行时可规划工作、跑工具、派生有界子  | [mkurman/zorai](reports/mkurman__zorai.md) |
| [zgiai/zgi](https://github.com/zgiai/zgi) | 311 | Go + Next.js 的 Agent Runtime 工作区：agents、workflows、skills、kno | [zgiai/zgi](reports/zgiai__zgi.md) |
| [Caxson/swiftagentx](https://github.com/Caxson/swiftagentx) | 221 | 核心思想：ReAct 是探索手段，不是最终运行时路径。模式被验证可重复后，编译成可复用 Scenario（预编译执行链） | [Caxson/swiftagentx](reports/Caxson__swiftagentx.md) |
| [Zleap-AI/Zleap-Agent](https://github.com/Zleap-AI/Zleap-Agent) | 207 | workspace-first：上下文按工作区裁剪，减少噪音与 token。支持本地与 OpenAI 兼容模型；早期 p | [Zleap-AI/Zleap-Agent](reports/Zleap-AI__Zleap-Agent.md) |
| [yologdev/yoagent](https://github.com/yologdev/yoagent) | 173 | Rust Agent 循环：prompt → LLM 流式 → 工具执行 → 循环。多协议抽象（7 种）、crates. | [yologdev/yoagent](reports/yologdev__yoagent.md) |
| [zqiren/Orbital](https://github.com/zqiren/Orbital) | 128 | 以"项目"而非"会话"为单元：文件夹内维护状态/决策/教训/任务队列/产物；新任务基于历史上下文启动；可派发 Claud | [zqiren/Orbital](reports/zqiren__Orbital.md) |
| [noumena-labs/Sipp](https://github.com/noumena-labs/Sipp) | 102 | Rust 为核心的基础设施（apps + bindings），强调可靠性与易用性平衡。 | [noumena-labs/Sipp](reports/noumena-labs__Sipp.md) |
| [MoFox-Studio/Neo-MoFox](https://github.com/MoFox-Studio/Neo-MoFox) | 88 | Python 3.11+ 的 AI 伙伴引擎：高度弹性、插件化（AI插件编写规范），Docker 部署。 | [MoFox-Studio/Neo-MoFox](reports/MoFox-Studio__Neo-MoFox.md) |
| [Ephemeral-AI-Lab/ephemeral-sandbox](https://github.com/Ephemeral-AI-Lab/ephemeral-sandbox) | 59 | Rust 沙箱基础设施：并行编码 Agent 隔离工作区、冲突处理、原子发布；提供 CLI/MCP 接口、独立测试仓库。 | [Ephemeral-AI-Lab/ephemeral-sandbox](reports/Ephemeral-AI-Lab__ephemeral-sandbox.md) |
| [majiayu000/harness](https://github.com/majiayu000/harness) | 53 | 多 Agent 编排 + 策略引擎 + 可观测（OTLP）+ MCP Server：AI Agent 舰队交付代码，策略 | [majiayu000/harness](reports/majiayu000__harness.md) |
| [DarkNoah/aime-chat](https://github.com/DarkNoah/aime-chat) | 40 | 跨平台桌面 AI 聊天客户端（AIME Chat），MIT 开源，文档站。 | [DarkNoah/aime-chat](reports/DarkNoah__aime-chat.md) |
| [Pretend-to/mio-chat-backend](https://github.com/Pretend-to/mio-chat-backend) | 36 | Mio-Chat 生态后端：对话转发 + Hooks 机制 + PM2 部署；生态全家桶（frontend/previe | [Pretend-to/mio-chat-backend](reports/Pretend-to__mio-chat-backend.md) |
| [cubeplexai/cubepi](https://github.com/cubeplexai/cubepi) | 33 | Pythonic、async-native、高性能、生产级持久化的 Agent 框架；线性循环替代图编排，强调可读性与可 | [cubeplexai/cubepi](reports/cubeplexai__cubepi.md) |
| [tao12345666333/amcp](https://github.com/tao12345666333/amcp) | 32 | "想要立刻有用的 Agent，而不是先组装框架"：文件编辑、Shell、Web、记忆、skills、subagents、 | [tao12345666333/amcp](reports/tao12345666333__amcp.md) |
| [hawkingrei/agenthub](https://github.com/hawkingrei/agenthub) | 31 | 自托管 Agent 控制面：长期 Agent、ACP 时间线、Team 协作、远程执行节点。Rust 实现、Bazel  | [hawkingrei/agenthub](reports/hawkingrei__agenthub.md) |
| [vorojar/AgentClaw](https://github.com/vorojar/AgentClaw) | 29 | 理解意图、规划任务、调度工具/技能；多 IM 渠道待命；Hive 模式下每个 Agent 独立记忆空间、工具白名单、技能 | [vorojar/AgentClaw](reports/vorojar__AgentClaw.md) |
| [terryso/open-agent-sdk-swift](https://github.com/terryso/open-agent-sdk-swift) | 28 | Swift 6.1、macOS 13+：Agent 能力 SDK，覆盖 CI/coverage，BMAD 方法，Prod | [terryso/open-agent-sdk-swift](reports/terryso__open-agent-sdk-swift.md) |
| [Chasen-Liao/pi-agent-desktop](https://github.com/Chasen-Liao/pi-agent-desktop) | 26 | pi 的 Electron 桌面客户端：更原生体验，个人极简定位。 | [Chasen-Liao/pi-agent-desktop](reports/Chasen-Liao__pi-agent-desktop.md) |
| [cosmtrek/jeju](https://github.com/cosmtrek/jeju) | 26 | "Jeju 之于 Agent 如 K8s manifest 之于部署"：一个 manifest 定义 Agent，hea | [cosmtrek/jeju](reports/cosmtrek__jeju.md) |
| [felixzhang-glitch/codeClaw](https://github.com/felixzhang-glitch/codeClaw) | 18 | "能力归 agent，编排归 harness"：飞书/微信桥接、渠道适配（格式化/分段/图片）、后端路由切换；pi 默认 | [felixzhang-glitch/codeClaw](reports/felixzhang-glitch__codeClaw.md) |
| [fffonion/yahu](https://github.com/fffonion/yahu) | 15 | 非侵入式：通过 API Server 与 Hermes 并存，不装插件/不改数据；UI 覆盖聊天/会话/cron/记忆/ | [fffonion/yahu](reports/fffonion__yahu.md) |
| [abcwyc/pi-agent-desktop](https://github.com/abcwyc/pi-agent-desktop) | 14 | pi 桌面化：会话浏览/恢复、实时可见性（thinking/tools/context/cost/compaction） | [abcwyc/pi-agent-desktop](reports/abcwyc__pi-agent-desktop.md) |
| [YangKGcsdms/antlegion-platform](https://github.com/YangKGcsdms/antlegion-platform) | 13 | AntLegion：fact bus + dcu-workspace + ecu；TypeScript 5.x、Node | [YangKGcsdms/antlegion-platform](reports/YangKGcsdms__antlegion-platform.md) |
| [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) | 10 | 多客户端 harness 框架：.claude-plugin/.codex-plugin/.cursor-plugin/ | [btspoony/mstar-harness](reports/btspoony__mstar-harness.md) |
| [synvo-ai/mobile-cocoa](https://github.com/synvo-ai/mobile-cocoa) | 8 | 移动端 + 后端生态：Expo 手机界面、服务端操作/文件管理、LLM 驱动的 UI/全栈编码与调试。 | [synvo-ai/mobile-cocoa](reports/synvo-ai__mobile-cocoa.md) |
| [13f/aman](https://github.com/13f/aman) | 6 | ALPHA Agent：安全架构（消毒/过滤/沙箱/审计）、API/架构文档、防诈骗声明。 | [13f/aman](reports/13f__aman.md) |
| [hareonna-hina/XHAUS_FINAL](https://github.com/hareonna-hina/XHAUS_FINAL) | 5 | 人格 + Skill 运行时 + Satellite 自进化流水线 + 动态生活沙盒 + MobileGym GUI；W | [hareonna-hina/XHAUS_FINAL](reports/hareonna-hina__XHAUS_FINAL.md) |
| [openmodu/modu](https://github.com/openmodu/modu) | 5 | Go Agent 工具包：能力组件化，应用自主掌控 prompts/tools/persistence/deployme | [openmodu/modu](reports/openmodu__modu.md) |
| [zhuangbiaowei/smart_agent](https://github.com/zhuangbiaowei/smart_agent) | 5 | Ruby Agent 框架：MCP、工具、多 LLM、声明式 DSL；gem 分发（0.2.6）。 | [zhuangbiaowei/smart_agent](reports/zhuangbiaowei__smart_agent.md) |
| [Lancetwang/friday](https://github.com/Lancetwang/friday) | 3 | 本地通用 Agent：Windows/macOS 桌面、uv 打包、benchmarks。 | [Lancetwang/friday](reports/Lancetwang__friday.md) |
| [arcana-core/arcana](https://github.com/arcana-core/arcana) | 3 | Agent 平台：persona/记忆/模块化技能；执行/隔离/可观测；社媒/视频/工作流/直播场景。 | [arcana-core/arcana](reports/arcana-core__arcana.md) |
| [caiuswang/regin](https://github.com/caiuswang/regin) | 3 | harness 半边（Guides 前馈 + 反馈机制）：技能/文档引导先行，审查/回滚兜底；引用 LangChain  | [caiuswang/regin](reports/caiuswang__regin.md) |
| [cubeplexai/cubeplex](https://github.com/cubeplexai/cubeplex) | 3 | CubePi 的平台版：backend + frontend（web packages）。 | [cubeplexai/cubeplex](reports/cubeplexai__cubeplex.md) |
| [longyijdos/kana](https://github.com/longyijdos/kana) | 3 | 精简 Agent 运行时：手搓 Agent loop/TUI/MCP/OAuth/provider 流式/会话；eval | [longyijdos/kana](reports/longyijdos__kana.md) |
| [SUNRNEHUI/agent-reliability-harness](https://github.com/SUNRNEHUI/agent-reliability-harness) | 2 | Plan-native 可靠性 skill：默认轻、跨边界时物化契约、高风险时加审计。 | [SUNRNEHUI/agent-reliability-harness](reports/SUNRNEHUI__agent-reliability-harness.md) |
| [stonega/cusco](https://github.com/stonega/cusco) | 2 | GNOME 原生 AI 工作区：持久会话、provider 切换、记忆、本地工具、skills、桌面集成。 | [stonega/cusco](reports/stonega__cusco.md) |
| [FoxRick/Collie](https://github.com/FoxRick/Collie) | 1 | 非程序员友好的本地 harness：英语请求→可审查工作；Windows 11 x64。 | [FoxRick/Collie](reports/FoxRick__Collie.md) |
| [Setsuna-Agent/setsuna-desktop](https://github.com/Setsuna-Agent/setsuna-desktop) | 1 | 跨平台 Agent 工作区：理解/编辑/运行/审查代码。 | [Setsuna-Agent/setsuna-desktop](reports/Setsuna-Agent__setsuna-desktop.md) |
| [VIONWILLIAMS/agent-os-harness](https://github.com/VIONWILLIAMS/agent-os-harness) | 1 | DeepSeek-native 证据优先 Agent：工作区检查、本地工具、副作用审批、工具历史回放、证据轨迹（不存 r | [VIONWILLIAMS/agent-os-harness](reports/VIONWILLIAMS__agent-os-harness.md) |
| [Winsaney/brainstorming](https://github.com/Winsaney/brainstorming) | 1 | 设计期 harness：阶段/规则/状态约束 Agent，先理解→方案→规格。 | [Winsaney/brainstorming](reports/Winsaney__brainstorming.md) |
| [ai2humanagent/ai2humanwork](https://github.com/ai2humanagent/ai2humanwork) | 1 | 人类兜底：blocked 工作转人工、完成结果链上证明与支付；whitepaper。 | [ai2humanagent/ai2humanwork](reports/ai2humanagent__ai2humanwork.md) |
| [gobing-ai/spur](https://github.com/gobing-ai/spur) | 1 | harness 工具包：Agent 检测/健康检查、约束检查、工作流编排、会话历史导入与分析。 | [gobing-ai/spur](reports/gobing-ai__spur.md) |
| [kowyo/mini-agent](https://github.com/kowyo/mini-agent) | 1 | 最小终端 Agent：预构建分发（macOS/Linux）。 | [kowyo/mini-agent](reports/kowyo__mini-agent.md) |
| [samelabs/Kungfu](https://github.com/samelabs/Kungfu) | 1 | Go + PostgreSQL 平台：可移植记忆、付费任务交付；migrations。 | [samelabs/Kungfu](reports/samelabs__Kungfu.md) |
| [wowyuarm/Loom](https://github.com/wowyuarm/Loom) | 1 | 每部署一个 Runtime Instance 承载一个 Agent Individual：连续时间/工作空间/认知器官/ | [wowyuarm/Loom](reports/wowyuarm__Loom.md) |
| [xueyufish/hecate](https://github.com/xueyufish/hecate) | 1 | 企业 Agent 平台：多租户、MCP-first、自托管/云 SaaS；alembic 迁移、CI。 | [xueyufish/hecate](reports/xueyufish__hecate.md) |
| [yuanchenglu/deepseekagent](https://github.com/yuanchenglu/deepseekagent) | 1 | Hermes 深度改造：Harness 层让 DeepSeek 达到顶级；ACP adapter/registry。 | [yuanchenglu/deepseekagent](reports/yuanchenglu__deepseekagent.md) |
| [zhoudongliang-lut/agent-runtime](https://github.com/zhoudongliang-lut/agent-runtime) | 1 | 轻量（65MB）、安全（4 层防御）、简单（单进程）、灵活（混合 Skill）。 | [zhoudongliang-lut/agent-runtime](reports/zhoudongliang-lut__agent-runtime.md) |
| [zhuangbiaowei/smart_bot](https://github.com/zhuangbiaowei/smart_bot) | 1 | 基于 SmartAgent + SmartPrompt 的 CLI/Agent。 | [zhuangbiaowei/smart_bot](reports/zhuangbiaowei__smart_bot.md) |
| [Onion-L/carrent](https://github.com/Onion-L/carrent) | 0 | 项目级 Agent 桌面：线程/运行时控制/审批/终端/项目上下文。 | [Onion-L/carrent](reports/Onion-L__carrent.md) |
| [XaoticLabs/grimoire](https://github.com/XaoticLabs/grimoire) | 0 | Agent 服务化：identity/mailbox/supervisor；Claude Code 默认，pi/open | [XaoticLabs/grimoire](reports/XaoticLabs__grimoire.md) |
| [a2eprotocol/python-sdk](https://github.com/a2eprotocol/python-sdk) | 0 | A2E 协议 SDK：PyPI 发布、cookbook/codewiki。 | [a2eprotocol/python-sdk](reports/a2eprotocol__python-sdk.md) |
| [kinpoe-ray/evidence-harness](https://github.com/kinpoe-ray/evidence-harness) | 0 | 把 LLM 当作**不可信的意图生成器**，由确定性内核接管执行、工具、上下文、生命周期、可观测性、验证、治理与证据，只 | [kinpoe-ray/evidence-harness](reports/kinpoe-ray__evidence-harness.md) |
| [onesmash/slm-as-harness](https://github.com/onesmash/slm-as-harness) | 0 | SLM 作 harness：上下文索引 + 持久工作流运行时技能。 | [onesmash/slm-as-harness](reports/onesmash__slm-as-harness.md) |
| [yuanchenglu/deepseek_runtime](https://github.com/yuanchenglu/deepseek_runtime) | 0 | DeepSeek 本地 Runtime：协议/合同/审批/受限执行/预算/恢复/证据/发布全处理。 | [yuanchenglu/deepseek_runtime](reports/yuanchenglu__deepseek_runtime.md) |
| [zhulin025/LaoA-Harness](https://github.com/zhulin025/LaoA-Harness) | 0 | 本地优先 Runtime：OmniRoute auto 路由免费模型、macOS Wails 桌面 + CLI/TUI。 | [zhulin025/LaoA-Harness](reports/zhulin025__LaoA-Harness.md) |

## 2. Coding Harness / 工程向 Agent（49）

| 仓库 | ⭐ | 方向 | 报告 |
| --- | ---: | --- | --- |
| [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) | 29,806 | DeepSeek 生态的终端编码 Agent：单静态 Go 二进制、配置驱动（`reasonix.toml`，无硬编码模 | [esengine/DeepSeek-Reasonix](reports/esengine__DeepSeek-Reasonix.md) |
| [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | 26,609 | Qwen 官方的一体化编码 Agent：框架与 Qwen 模型共同开源、共同演进，无厂商锁定（支持 OpenAI/Ant | [QwenLM/qwen-code](reports/QwenLM__qwen-code.md) |
| [yologdev/yoyo-evolve](https://github.com/yologdev/yoyo-evolve) | 1,852 | "200 lines of Rust. Zero human code. One rule: evolve or die | [yologdev/yoyo-evolve](reports/yologdev__yoyo-evolve.md) |
| [clacky-ai/openclacky](https://github.com/clacky-ai/openclacky) | 1,158 | 以"token 效率"为核心卖点的 Agent：16 个工具（避免 schema 膨胀）、~100% 缓存命中、suba | [clacky-ai/openclacky](reports/clacky-ai__openclacky.md) |
| [CreminiAI/skillpack](https://github.com/CreminiAI/skillpack) | 1,129 | "技能如乐高，SkillPack 是成品"：把 skills/tools 组装成完整可运行的本地 Agent，团队在 S | [CreminiAI/skillpack](reports/CreminiAI__skillpack.md) |
| [weiesky/cc-viewer](https://github.com/weiesky/cc-viewer) | 1,056 | 给 Claude Code 加"经验层"：把真实开发过程蒸馏为可复用经验，配置与经验跨设备同步。npm / Homebr | [weiesky/cc-viewer](reports/weiesky__cc-viewer.md) |
| [runesleo/claude-code-workflow](https://github.com/runesleo/claude-code-workflow) | 708 | 不替代 Agent、不套仪式：把长期验证有效的行为压缩成 1,604 字节共享 Core，提供 dry-run、备份、隔 | [runesleo/claude-code-workflow](reports/runesleo__claude-code-workflow.md) |
| [haseeb-heaven/open-agent](https://github.com/haseeb-heaven/open-agent) | 279 | 零门槛终端 Agent：免费模型（OpenRouter）、本地模型（Ollama/LM Studio）、BYOK 云模型 | [haseeb-heaven/open-agent](reports/haseeb-heaven__open-agent.md) |
| [DerekYRC/mini-claude-code](https://github.com/DerekYRC/mini-claude-code) | 174 | 作者 mini-spring 系列的教学延伸：按章节拆解编码 Agent 核心机制，每章独立分支、保留最小代码。覆盖 A | [DerekYRC/mini-claude-code](reports/DerekYRC__mini-claude-code.md) |
| [thinkany-ai/dscode](https://github.com/thinkany-ai/dscode) | 121 | 不追求"功能最多"，而是保持运行时本地可检查：provider-aware 模型路由、本地会话、安全补丁、并行 Agen | [thinkany-ai/dscode](reports/thinkany-ai__dscode.md) |
| [TabbyML/pochi](https://github.com/TabbyML/pochi) | 117 | Tabby（自托管代码补全）团队出品的 Agent：IDE 内操作、命令工具包执行复杂任务；VS Code Market | [TabbyML/pochi](reports/TabbyML__pochi.md) |
| [Dimon94/dverity](https://github.com/Dimon94/dverity) | 110 | 完整产品契约只在 DVERITY.md：以证据为中心的交付流程，配合 devflow（工作流）与 acceptance（ | [Dimon94/dverity](reports/Dimon94__dverity.md) |
| [simple-agent-lab/simple-long-horizon-agent](https://github.com/simple-agent-lab/simple-long-horizon-agent) | 97 | "Simple by design. Effective over long horizons."：少即是多，面向多轮真 | [simple-agent-lab/simple-long-horizon-agent](reports/simple-agent-lab__simple-long-horizon-agent.md) |
| [dazuiba/handoff](https://github.com/dazuiba/handoff) | 79 | Agent 间交接：Claude Code/Codex ↔ DeepSeek 双向；简单活 DeepSeek 快且便宜， | [dazuiba/handoff](reports/dazuiba__handoff.md) |
| [ZacharyZhang-NY/Kigi-CLI](https://github.com/ZacharyZhang-NY/Kigi-CLI) | 54 | "The world's first CLI with built-in Graph Engineering"：目标→依 | [ZacharyZhang-NY/Kigi-CLI](reports/ZacharyZhang-NY__Kigi-CLI.md) |
| [lwmxiaobei/xbcode](https://github.com/lwmxiaobei/xbcode) | 48 | 早期开源产品：务实、可读、易扩展。流式输出、本地工具、持久任务、skills、MCP、轻量多 Agent；文档完善（Ro | [lwmxiaobei/xbcode](reports/lwmxiaobei__xbcode.md) |
| [mileson/openprd](https://github.com/mileson/openprd) | 47 | 轻量结构化 PRD harness：需求澄清、Agent 后台维护的事实与决策、图形化评审、非阻断式风险提醒、结构化交接 | [mileson/openprd](reports/mileson__openprd.md) |
| [ythx-101/agent-sop](https://github.com/ythx-101/agent-sop) | 46 | 目标不是让 Agent 更自主，而是按风险挑流程重量：高风险走完整可审计序列，低风险走轻路径；tier 定义在 SKIL | [ythx-101/agent-sop](reports/ythx-101__agent-sop.md) |
| [ZhenHuangLab/collaborating-with-claude-code](https://github.com/ZhenHuangLab/collaborating-with-claude-code) | 39 | Codex skill + `scripts/claude_code_bridge.py`：SOTA context e | [ZhenHuangLab/collaborating-with-claude-code](reports/ZhenHuangLab__collaborating-with-claude-code.md) |
| [ZhenHuangLab/collaborating-with-gemini-cli](https://github.com/ZhenHuangLab/collaborating-with-gemini-cli) | 30 | Codex skill + `scripts/gemini_cli_bridge.py`：默认只读（--no-full- | [ZhenHuangLab/collaborating-with-gemini-cli](reports/ZhenHuangLab__collaborating-with-gemini-cli.md) |
| [yanhua1010/build-your-own-coding-agent](https://github.com/yanhua1010/build-your-own-coding-agent) | 22 | 主线 pi（TS/MIT）+ codex/grok-build（Rust/Apache）对比；步骤式实现（steps/0 | [yanhua1010/build-your-own-coding-agent](reports/yanhua1010__build-your-own-coding-agent.md) |
| [cicialgo/rockycode](https://github.com/cicialgo/rockycode) | 21 | DeepSeek V4 优化：research mode、bench 验证（SWE-bench 79.8%、V4-pro | [cicialgo/rockycode](reports/cicialgo__rockycode.md) |
| [Sakura520222/Sakura-AI-Reviewer](https://github.com/Sakura520222/Sakura-AI-Reviewer) | 19 | FastAPI 后端 + Docker 部署：主动探索代码库、PR 审查、Issue 分析；Live Demo + An | [Sakura520222/Sakura-AI-Reviewer](reports/Sakura520222__Sakura-AI-Reviewer.md) |
| [its-ahoh/codey](https://github.com/its-ahoh/codey) | 14 | macOS 编程助手：release 分发、文档站、中英双语。 | [its-ahoh/codey](reports/its-ahoh__codey.md) |
| [linkerdog/rara](https://github.com/linkerdog/rara) | 14 | 本地优先终端 Agent：模型自由（Claude/DeepSeek/Gemini/Ollama 等）、TUI 流式/高亮 | [linkerdog/rara](reports/linkerdog__rara.md) |
| [taxueseek/kimix](https://github.com/taxueseek/kimix) | 13 | 跨平台 Rust 终端 AI 代理，Apache-2.0。 | [taxueseek/kimix](reports/taxueseek__kimix.md) |
| [rocky2431/ultra-builder-pro](https://github.com/rocky2431/ultra-builder-pro) | 10 | 真实工程 harness：六阶段 spine、review lenses、TDD、证据纪律、hook 契约。已迁移：新  | [rocky2431/ultra-builder-pro](reports/rocky2431__ultra-builder-pro.md) |
| [rust-infra/tact](https://github.com/rust-infra/tact) | 9 | Rust 终端 Agent：快速开始、特性、架构文档（ARCHITECTURE.md）。 | [rust-infra/tact](reports/rust-infra__tact.md) |
| [linearuncle/xharness](https://github.com/linearuncle/xharness) | 8 | 项目级 AI 编程搭档：直接动手干活而非复制粘贴；GUI（macOS Apple Silicon）。 | [linearuncle/xharness](reports/linearuncle__xharness.md) |
| [geminixiang/mikan](https://github.com/geminixiang/mikan) | 7 | 多平台 coding agent：conversation-scoped workspaces + sandbox ex | [geminixiang/mikan](reports/geminixiang__mikan.md) |
| [CJackHwang/SunamAI](https://github.com/CJackHwang/SunamAI) | 5 | 浏览器内 Agent 工作区：BYO 模型（OpenAI-compatible）、WebContainer 隔离、可恢复 | [CJackHwang/SunamAI](reports/CJackHwang__SunamAI.md) |
| [heimoshuiyu/opencode](https://github.com/heimoshuiyu/opencode) | 5 | opencode fork：保持上游能力，社区先行落地测试（作者在帖子中说明参与 opencode v2 测试）。 | [heimoshuiyu/opencode](reports/heimoshuiyu__opencode.md) |
| [lznauy/NekoCode](https://github.com/lznauy/NekoCode) | 5 | 轻量单文件 AI 编程助手：人格化 UI + 多模型 + 代码操作。 | [lznauy/NekoCode](reports/lznauy__NekoCode.md) |
| [Codegass/Setup-Agent](https://github.com/Codegass/Setup-Agent) | 4 | 学术论文驱动的配置 Agent：Docker 隔离执行、engine-owned phase machine（provi | [Codegass/Setup-Agent](reports/Codegass__Setup-Agent.md) |
| [La-fe/vercel-claude-code](https://github.com/La-fe/vercel-claude-code) | 4 | Claude Code 逆向重构：22 个核心能力在 Vercel AI SDK 上重建；证明 SDK 原语可替代大规模 | [La-fe/vercel-claude-code](reports/La-fe__vercel-claude-code.md) |
| [XiaomingX/mimofan](https://github.com/XiaomingX/mimofan) | 4 | Rust 终端 Agent：MiMo 原生 + 主流模型兼容 + MCP；架构文档完善。 | [XiaomingX/mimofan](reports/XiaomingX__mimofan.md) |
| [Yorha9e/oh-my-kimi-code](https://github.com/Yorha9e/oh-my-kimi-code) | 4 | 社区 fork：多代理编排先行实验、与上游并存（omkc 独立命令/`~/.omkc` 数据目录）。 | [Yorha9e/oh-my-kimi-code](reports/Yorha9e__oh-my-kimi-code.md) |
| [shi275773124/Falsify](https://github.com/shi275773124/Falsify) | 4 | 审查优先：对抗性审查（针对假绿）+ 框架审查（针对长期腐化）+ Cutline 分级（Must Fix/Debt/Del | [shi275773124/Falsify](reports/shi275773124__Falsify.md) |
| [ladydd/token-overload](https://github.com/ladydd/token-overload) | 3 | 分层执行：强模型规划/验收、弱模型执行、程序验证兜底；53 tests。 | [ladydd/token-overload](reports/ladydd__token-overload.md) |
| [xin-yi33/RxyCode](https://github.com/xin-yi33/RxyCode) | 3 | 计划-执行 Agent：验证机制、安全工具编排、API server（流式）。 | [xin-yi33/RxyCode](reports/xin-yi33__RxyCode.md) |
| [Mashiro2000/We0Code](https://github.com/Mashiro2000/We0Code) | 2 | Python TUI/ACP 编码 Agent。 | [Mashiro2000/We0Code](reports/Mashiro2000__We0Code.md) |
| [CSZHK/goal-conditions](https://github.com/CSZHK/goal-conditions) | 1 | 针对 /goal 条件表述问题的增强 skill：帮助写准确、可评估的条件。 | [CSZHK/goal-conditions](reports/CSZHK__goal-conditions.md) |
| [Viking602/azem](https://github.com/Viking602/azem) | 1 | Go 终端 Agent：受治理工具、持久会话、副作用恢复、MCP/skills/多 Agent。 | [Viking602/azem](reports/Viking602__azem.md) |
| [nolotus/nolo-cli](https://github.com/nolotus/nolo-cli) | 1 | 维护者 Agent 自动化：agent-runtime、email/delete/grant 等命令；npm 发布（no | [nolotus/nolo-cli](reports/nolotus__nolo-cli.md) |
| [oines/astral-code](https://github.com/oines/astral-code) | 1 | Codex fork：provider-neutral、保留 Rust 核心/沙箱/TUI。 | [oines/astral-code](reports/oines__astral-code.md) |
| [iancjy-creator/antigravity-agent-rigor-guard](https://github.com/iancjy-creator/antigravity-agent-rigor-guard) | 0 | fail-closed 护栏：工具调用拦截、审计证据、测试退化检测、完成门禁。 | [iancjy-creator/antigravity-agent-rigor-guard](reports/iancjy-creator__antigravity-agent-rigor-guard.md) |
| [pakco77/mishu.skill](https://github.com/pakco77/mishu.skill) | 0 | 秘书 skill：统一项目线索、项目管理辅助。 | [pakco77/mishu.skill](reports/pakco77__mishu.skill.md) |
| [praxstack/agent-org](https://github.com/praxstack/agent-org) | 0 | 门控自主编码：coder 不能提交 + 真实验证门 + 评审委员会。 | [praxstack/agent-org](reports/praxstack__agent-org.md) |
| [yuanchenglu/deepcode](https://github.com/yuanchenglu/deepcode) | 0 | DeepSeek V4 编程助手：Alpha 阶段，安装文档站。 | [yuanchenglu/deepcode](reports/yuanchenglu__deepcode.md) |

## 3. 多 Agent 编排 / 协作系统（24）

| 仓库 | ⭐ | 方向 | 报告 |
| --- | ---: | --- | --- |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 79,136 | DeerFlow 2.0 是**从零重写**的超级 Agent Harness（与 1.x 深研框架无代码共享）。定位： | [bytedance/deer-flow](reports/bytedance__deer-flow.md) |
| [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent) | 6,710 | 与"固定流程图"相反：运行时根据目标动态规划任务 DAG（有向无环图），支持任意 LLM，强调可观测性、可靠性与安全。n | [open-multi-agent/open-multi-agent](reports/open-multi-agent__open-multi-agent.md) |
| [Team-Commonly/commonly](https://github.com/Team-Commonly/commonly) | 1,283 | "Chat with your agents. Ship real work."——把多种 Agent 运行时（Clau | [Team-Commonly/commonly](reports/Team-Commonly__commonly.md) |
| [Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas) | 1,036 | 本地优先、可自进化的 AI 劳动力：Commander（理解上下文、拆解目标、选 Agent/技能/连接器/工具）+ 专 | [Orkas-AI/Orkas](reports/Orkas-AI__Orkas.md) |
| [mco-org/squad](https://github.com/mco-org/squad) | 619 | 极简多 Agent 终端协作：无 daemon、无后台进程，每条命令一次完成；通过 shell 命令 + SQLite  | [mco-org/squad](reports/mco-org__squad.md) |
| [solo-agent/solo](https://github.com/solo-agent/solo) | 562 | 本地优先的人机协同：渠道 + 线程对话 + 任务板 + channel 团队，协调多个 AI 编码 Agent。Go 后 | [solo-agent/solo](reports/solo-agent__solo.md) |
| [mco-org/mco](https://github.com/mco-org/mco) | 471 | 轻量 CLI-first 编排层：一个任务 → 多个 Agent/模型并行 → 对比原始回答 → 行动。可从终端或由另一 | [mco-org/mco](reports/mco-org__mco.md) |
| [tt-a1i/hive](https://github.com/tt-a1i/hive) | 451 | 本地多 Agent 协作：Orchestrator 规划委派，workers 以真实 PTY 进程执行并回报。一个浏览器 | [tt-a1i/hive](reports/tt-a1i__hive.md) |
| [firstintent/ccteam](https://github.com/firstintent/ccteam) | 112 | 让"各自孤岛"的 coding CLI 组成团队：Claude Code 规划最深、Codex 长跑稳、Grok 最快、 | [firstintent/ccteam](reports/firstintent__ccteam.md) |
| [citarreikee/visible_manus](https://github.com/citarreikee/visible_manus) | 111 | 多 Agent 编排 + 实时可视化：后端（Python WebSocket server）+ 前端画布；planner | [citarreikee/visible_manus](reports/citarreikee__visible_manus.md) |
| [agent-team-foundation/first-tree](https://github.com/agent-team-foundation/first-tree) | 108 | Agent 团队基础设施：Open App + npm 包（first-tree），多 Agent 协作开发平台（age | [agent-team-foundation/first-tree](reports/agent-team-foundation__first-tree.md) |
| [Sma1lboy/kobe](https://github.com/Sma1lboy/kobe) | 93 | 把"终端分屏"体验带给 Agent：并行会话、独立 worktree/branch、detach/reattach 继续 | [Sma1lboy/kobe](reports/Sma1lboy__kobe.md) |
| [yofine/Mexus](https://github.com/yofine/Mexus) | 85 | 多 Agent 执行统一层：每个 Agent 作为受管执行面板（创建/关闭/重启/恢复），实时状态指示，底部浮动终端；从 | [yofine/Mexus](reports/yofine__Mexus.md) |
| [Dqz00116/opencode-solo](https://github.com/Dqz00116/opencode-solo) | 31 | opencode 的编排层：closed-loop orchestrator + specialized subagen | [Dqz00116/opencode-solo](reports/Dqz00116__opencode-solo.md) |
| [CiferaTeam/GitIM](https://github.com/CiferaTeam/GitIM) | 22 | "消息即 commit"：GitIM 把协作（频道/DM/Kanban/Agent 队友）表达为仓库文件；Git 托管为 | [CiferaTeam/GitIM](reports/CiferaTeam__GitIM.md) |
| [talesofai/cohub](https://github.com/talesofai/cohub) | 11 | 公司内部每周烧 100 亿 token 的 Spaces：对话/文件/会话/任务/预览 + checkpoint 保存/ | [talesofai/cohub](reports/talesofai__cohub.md) |
| [chukong-creator/agent-os-skill](https://github.com/chukong-creator/agent-os-skill) | 4 | Agent OS v0.5 / Agent Shift v2：认知中枢协调隔离执行节点；证据、审查、回滚闭环；Pytho | [chukong-creator/agent-os-skill](reports/chukong-creator__agent-os-skill.md) |
| [La-fe/multi-agent-factory](https://github.com/La-fe/multi-agent-factory) | 3 | 多 Agent 并行开发工厂：自动化编排（Issue→PR）、可视化模式、安全并行、质量门、一键审查。 | [La-fe/multi-agent-factory](reports/La-fe__multi-agent-factory.md) |
| [trynhexagon/hermes-console](https://github.com/trynhexagon/hermes-console) | 3 | Agent OS 控制面：静态展示 + 实时后端（FastAPI + DeepSeek v4 pro），需求分析→PRD | [trynhexagon/hermes-console](reports/trynhexagon__hermes-console.md) |
| [Arcadia822/mystra](https://github.com/Arcadia822/mystra) | 2 | 基于 Open Agents 参考架构的编排平台：HTTP/CLI/MCP 提交、本地优先持久化、可插拔接缝、沙箱 pu | [Arcadia822/mystra](reports/Arcadia822__mystra.md) |
| [hahhforest/linka](https://github.com/hahhforest/linka) | 1 | Agent Team 平台：Bot 面向人、room 给 Agent Team；可观测/干预/编程。 | [hahhforest/linka](reports/hahhforest__linka.md) |
| [shanyuzhe/research-fleet](https://github.com/shanyuzhe/research-fleet) | 1 | 研究 AI 团队：audit trail 优先；Claude Code 插件。 | [shanyuzhe/research-fleet](reports/shanyuzhe__research-fleet.md) |
| [xfx-studio/claworld-hermes-plugin](https://github.com/xfx-studio/claworld-hermes-plugin) | 1 | Hermes 插件：实时聊天世界、Agent 身份、agent-to-agent 对话、报告带回。 | [xfx-studio/claworld-hermes-plugin](reports/xfx-studio__claworld-hermes-plugin.md) |
| [sdougbrown/avenor](https://github.com/sdougbrown/avenor) | 0 | 多级编排：jockey 只读派活、horse/mule 写执行；8 后端；MCP server（avenor mcp）。 | [sdougbrown/avenor](reports/sdougbrown__avenor.md) |

## 4. 记忆 / 上下文 / 知识管理（17）

| 仓库 | ⭐ | 方向 | 报告 |
| --- | ---: | --- | --- |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 77,339 | 以 Claude Code 插件为第一形态，把代码理解从"人肉读代码"变成"AI 建图谱 + 交互式仪表盘"。核心理念： | [Egonex-AI/Understand-Anything](reports/Egonex-AI__Understand-Anything.md) |
| [chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat) | 38,503 | 国内最知名的开源中文知识库问答方案之一（早期叫 Langchain-ChatGLM）。定位：对中文场景与开源模型友好、可 | [chatchat-space/Langchain-Chatchat](reports/chatchat-space__Langchain-Chatchat.md) |
| [tommy0103/obelisk](https://github.com/tommy0103/obelisk) | 298 | 同一 SQLite 索引两面：Agent 侧（obelisk CLI 拥有本地运行时 + agent skill 教编码 | [tommy0103/obelisk](reports/tommy0103__obelisk.md) |
| [however-yir/knowledgeops-agent](https://github.com/however-yir/knowledgeops-agent) | 188 | 生产导向的平台原型（非"未经验证的成品声明"）：Agent 工作流引擎、混合检索、知识图谱、长短记忆持久化、DeepRe | [however-yir/knowledgeops-agent](reports/however-yir__knowledgeops-agent.md) |
| [zhuzhaoyun/Molio](https://github.com/zhuzhaoyun/Molio) | 94 | 本地优先工作台：以 Obsidian vault 为数据源与落点，AI 基于你的积累干活并写回；第三方服务器不参与。Do | [zhuzhaoyun/Molio](reports/zhuzhaoyun__Molio.md) |
| [synvo-ai/local-cocoa](https://github.com/synvo-ai/local-cocoa) | 57 | 完全本地（llama.cpp 驱动）：文件→记忆→上下文→洞察→行动链路；插件体系，跨平台。 | [synvo-ai/local-cocoa](reports/synvo-ai__local-cocoa.md) |
| [pumblus/okf-harness](https://github.com/pumblus/okf-harness) | 31 | 融合 Karpathy LLM Wiki（Agent 维护的活知识库）与 Google OKF（可移植 Markdown | [pumblus/okf-harness](reports/pumblus__okf-harness.md) |
| [ldclabs/anda-bot](https://github.com/ldclabs/anda-bot) | 22 | Rust 终端 Agent：图谱长期记忆（Anda Brain）、跨会话推理、长程目标、工具（Claude Code/C | [ldclabs/anda-bot](reports/ldclabs__anda-bot.md) |
| [Xnmk029/ETharness](https://github.com/Xnmk029/ETharness) | 17 | 独立记忆寻址系统：解决"会话记忆受限于上下文窗口、跨会话靠重复阐述"问题；暂缓开发（依赖 DeepSeek 磁盘前缀缓存 | [Xnmk029/ETharness](reports/Xnmk029__ETharness.md) |
| [hydelovegood/paperweave](https://github.com/hydelovegood/paperweave) | 8 | 本地优先论文工作流：PDF 导入（SHA256 去重）、DeepXiv/PyMuPDF 解析、结构化摘要 + revie | [hydelovegood/paperweave](reports/hydelovegood__paperweave.md) |
| [trynhexagon/tide](https://github.com/trynhexagon/tide) | 5 | 本地优先多 Agent 工作助手：日报、任务、风险、跨聊主题、关系图、主题演化；frontend + backend + | [trynhexagon/tide](reports/trynhexagon__tide.md) |
| [GodOnlyKn0w/mnema](https://github.com/GodOnlyKn0w/mnema) | 1 | 拓扑而非向量：append-only 哈希链条目 → strands/trees/scopes；进程/模型可替换，拓扑持 | [GodOnlyKn0w/mnema](reports/GodOnlyKn0w__mnema.md) |
| [TuanVibeCode/longctx](https://github.com/TuanVibeCode/longctx) | 0 | 本地长上下文：锚点分块剔除 + 分层摘要，消费级 GPU 32K+。 | [TuanVibeCode/longctx](reports/TuanVibeCode__longctx.md) |
| [percena/memfuse](https://github.com/percena/memfuse) | 0 | 本地记忆服务：知道"有什么/在哪"，适时给信号，细节自然淡忘。 | [percena/memfuse](reports/percena__memfuse.md) |
| [xscanzm/recall](https://github.com/xscanzm/recall) | 0 | 主动上下文助理：观察→结构化记忆→任务/项目/提醒/日报周报；截图仅作模型输入。 | [xscanzm/recall](reports/xscanzm__recall.md) |
| [zhuangbiaowei/smart_brain](https://github.com/zhuangbiaowei/smart_brain) | 0 | 记忆运行时：commit_turn（写链路）+ compose_context（读装配）；联动 SmartRAG。 | [zhuangbiaowei/smart_brain](reports/zhuangbiaowei__smart_brain.md) |
| [zhuangbiaowei/smart_rag](https://github.com/zhuangbiaowei/smart_rag) | 0 | 混合 RAG：向量+全文+主题/标签；本地/URL 文档导入；API 文档。 | [zhuangbiaowei/smart_rag](reports/zhuangbiaowei__smart_rag.md) |

## 5. 评测 / Benchmark 工具（4）

| 仓库 | ⭐ | 方向 | 报告 |
| --- | ---: | --- | --- |
| [minghinmatthewlam/openbench](https://github.com/minghinmatthewlam/openbench) | 118 | 聚焦 harness 层对比：CLI 工具在 run loop/工具集/权限策略上的差异。提供 obench CLI（` | [minghinmatthewlam/openbench](reports/minghinmatthewlam__openbench.md) |
| [Xnmk029/Xnmk_Prompt_Library_1.0](https://github.com/Xnmk029/Xnmk_Prompt_Library_1.0) | 25 | 标准化 Benchmark 套件：L1 基础工具/脚本（5）、L2 中级 Web/游戏（11）、L3 高级 3D/物理（ | [Xnmk029/Xnmk_Prompt_Library_1.0](reports/Xnmk029__Xnmk_Prompt_Library_1.0.md) |
| [xiaozhenliu/micro-eval](https://github.com/xiaozhenliu/micro-eval) | 5 | 本地优先评测：tasks × configs × reps 矩阵、沙箱隔离、证据链、guarded decision（强 | [xiaozhenliu/micro-eval](reports/xiaozhenliu__micro-eval.md) |
| [alexalexalex222/Loop-Factory-mcp-public](https://github.com/alexalexalex222/Loop-Factory-mcp-public) | 0 | 本地优先、零依赖、MCP over stdio：worker 提议、verifier 裁决、operator 控制晋升。 | [alexalexalex222/Loop-Factory-mcp-public](reports/alexalexalex222__Loop-Factory-mcp-public.md) |

---

数据快照：2026-08 抓取；star 数为各仓库抓取时点值。