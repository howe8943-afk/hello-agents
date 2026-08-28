# Hello-Agents 学习记录

这是我的 AI Agent 学习与实践仓库，学习主线来自 Datawhale 的 [Hello-Agents](https://datawhalechina.github.io/hello-agents/#/) 教程。

这里不重复维护官方课程内容，而是记录我实际读过什么、写过什么、遇到什么问题，以及每个阶段留下的可运行成果。

## 当前状态

| 项目     | 状态                                                                     |
| -------- | ------------------------------------------------------------------------ |
| 学习阶段 | Stage 0：理解 Agent 基础概念                                             |
| 当前目标 | 跑通最小 Agent Loop，并理解工具调用过程                                  |
| Python   | 3.12+                                                                    |
| 包管理   | [uv](https://docs.astral.sh/uv/)                                          |
| 仓库     | [howe8943-afk/hello-agents](https://github.com/howe8943-afk/hello-agents) |

## 环境与运行

```powershell
uv sync
uv run hello-agent
```

需要 API Key 的练习，将本地配置写入 `.env`。可以从 `.env.example` 开始；真实密钥不会提交到 Git。

日常实验统一放在 `experiments/`，每个实验可以单独建立目录和 README：

```powershell
uv run python experiments/<实验目录>/main.py
```

## 我的学习路线

这份路线参考官方教程和相关资料，我会根据自己的理解与实践进度更新状态。

### Stage 0：理解 Agent

- [X] 区分 chatbot、workflow、agent 和 multi-agent。
- [X] 理解 `observe -> think -> act -> observe` 基本循环。
- [X] 记录一个适合 Agent、而不是普通脚本的实际场景。
- [X] 完成 Hello-Agents 入门章节笔记。

**阶段产出：** 一篇基础概念笔记，以及对一个真实应用场景的判断。

### Stage 1：实现最小 Agent Loop

- [X] 调用一个 LLM API 完成对话。
- [ ] 让模型输出结构化 JSON。
- [ ] 编写一个简单工具，例如计算器、搜索或文件读取。
- [ ] 解析 tool call，执行工具并把结果传回模型。
- [ ] 加入最大步数、超时和错误处理。

**阶段产出：** 一个可以自主选择并调用工具的最小 Agent。

### Stage 2：工具、RAG 与记忆

- [ ] 完成一次 `chunk -> embed -> retrieve -> answer` 流程。
- [ ] 比较短期上下文、会话记忆和长期记忆。
- [ ] 处理空结果、工具失败、重复调用和无依据引用。
- [ ] 为回答保留来源或证据。

**阶段产出：** 一个能够搜索资料、总结内容并输出引用的研究助手。

### Stage 3：研究 Agent Harness

- [ ] 读懂一个 Agent 项目的目录结构。
- [ ] 找出 Agent Loop、Tool Registry、权限控制和会话存储。
- [ ] 理解上下文压缩、日志和 Trace 的作用。
- [ ] 给现有示例增加一个自己的工具。

**阶段产出：** 一个包含运行说明、示例输入输出和失败记录的 Harness Demo。

### Stage 4：多 Agent 协作

- [ ] 理解 planner、executor、reviewer 和 router 的职责。
- [ ] 为每个 Agent 定义输入、输出和停止条件。
- [ ] 处理循环、任务漂移和上下文膨胀。
- [ ] 对比单 Agent 与多 Agent 的效果和成本。

**阶段产出：** 一个 `research -> write -> review -> revise` 小型系统。

### Stage 5：Skills 与协议

- [ ] 区分 Tool、Prompt、Skill 和 MCP。
- [ ] 编写一个包含触发条件、步骤和验收标准的 `SKILL.md`。
- [ ] 给 Skill 增加脚本或模板。
- [ ] 为 Skill 编写 smoke test。

**阶段产出：** 一个可复用的代码审查、研究报告或迁移助手 Skill。

### Stage 6：浏览器与计算机操作

- [ ] 使用 Playwright 或 browser-use 操作公开网页。
- [ ] 处理页面变化、弹窗、加载失败和定位失败。
- [ ] 记录截图、DOM 和动作日志。
- [ ] 为高风险操作增加确认和权限边界。

**阶段产出：** 一个只操作公开网页的浏览器 Agent。

### Stage 7：评测、安全与可观测性

- [ ] 建立固定测试集和成功标准。
- [ ] 记录成功率、失败原因、调用次数、成本和延迟。
- [ ] 为危险工具加入人工确认。
- [ ] 学习 prompt injection、data exfiltration 和 tool abuse。

**阶段产出：** 至少包含 20 个任务的 Agent Eval 表格。

### Stage 8：完成一个真实项目

- [ ] 明确用户、任务和成功标准。
- [ ] 加入日志、重试、超时和成本上限。
- [ ] 提供 CLI、Web、机器人或 GitHub Action 入口。
- [ ] 写清运行方式、配置方法、扩展方式和限制。

**阶段产出：** 一个别人可以 clone 后运行的 Agent 项目。

## 实践项目

| 项目                | 阶段    | 状态   | 记录                       |
| ------------------- | ------- | ------ | -------------------------- |
| Hello Agent 初始化  | Stage 0 | 已完成 | `src/hello_agent/`       |
| Calculator Agent    | Stage 1 | 未开始 | 待实现工具调用循环         |
| Web Research Agent  | Stage 2 | 未开始 | 待实现搜索、引用和总结     |
| PDF QA Agent        | Stage 2 | 未开始 | 待实现 RAG 与文档问答      |
| Coding Review Agent | Stage 3 | 未开始 | 待实现 diff 分析与风险排序 |

## 学习笔记

每次学习尽量留下以下内容，避免只收藏链接：

- **日期：**
- **学习主题：**
- **参考资料：**
- **我理解的核心概念：**
- **动手实现：**
- **遇到的问题：**
- **下一步：**

后续笔记和实验代码会按主题放入对应目录，并在这里补充入口链接。

## 主要资料

- [Hello-Agents 官方教程](https://datawhalechina.github.io/hello-agents/#/)
- [Hello-Agents GitHub 仓库](https://github.com/datawhalechina/hello-agents)
- [Anthropic：Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [OpenAI：A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [ReAct 论文](https://arxiv.org/abs/2210.03629)
- [Lilian Weng：LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)

## 仓库约定

- 使用 `uv sync` 同步依赖，使用 `uv run` 执行命令。
- 新增实验时，同时补充运行命令、实验结果和问题记录。
- 不提交 `.env`、API Key 或其他敏感信息。
- 先做小而可验证的实验，再扩展到复杂 Agent。
