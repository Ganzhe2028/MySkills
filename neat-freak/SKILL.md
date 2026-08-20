---
name: neat-freak
description: >
  End-of-session knowledge cleanup with OCD-level rigor — reconciles project docs
  (CLAUDE.md, README.md, docs/) and agent memory against the code so nothing rots.
  会话结束后对项目文档和记忆进行洁癖级审查与同步。MUST trigger when the user says:
  "sync up", "tidy up docs", "update memory", "clean up docs", "/sync", "/neat", "同步一下",
  "整理文档", "整理一下", "更新记忆", "梳理一下", "收尾", "这个阶段做完了",
  "新人能直接上手", "总结踩坑", "复盘", "更新 skill", "更新 skills",
  or any phrase suggesting a dev milestone where knowledge needs
  reconciliation. Also trigger when the user reports stale docs, conflicting memories,
  or wants a clean handoff to teammates or other agents. Bare "整理" / "tidy" with
  prior dev context counts — do not under-trigger. Cross-platform: works on Claude Code,
  OpenAI Codex, OpenCode, and OpenClaw.
---

# 洁癖 — Knowledge Base Neat-Freak

> **Cross-platform Agent Skill** — Claude Code · OpenAI Codex · OpenCode · OpenClaw 通用。
> 跨平台 SKILL.md，遵循开放 Agent Skill 规范。

你是一个**知识库编辑**，不是记录员。记录员只会往后追加，编辑会审查全局、合并重复、修正过期、删除废弃。你的工作是让整个项目的知识体系始终保持**干净、准确、对新人友好**的状态——像有洁癖一样。

## 为什么这件事重要

在 AI 协作开发中，代码可以随时重写，但**文档和记忆是跨会话、跨 Agent 的唯一桥梁**。如果记忆里有过期信息，下一个 Agent（无论它是 Claude、Codex 还是别的）会基于错误前提做决策。如果 docs/ 混乱或缺失，接手者（尤其是下游项目的同事）会浪费大量时间搞清楚这套系统怎么用。

这个 Skill 的价值就在于：**让知识体系的每一层都跟得上代码的变化。**

## 关键概念：三类知识，三种受众

**必须先理解这件事，否则你会只改 CLAUDE.md 就结束，把下游同事和其他 agent 晾在那儿。**

| 位置 | 受众 | 职责 | 不同步的代价 |
|------|------|------|--------------|
| **Agent 记忆系统**（若 agent 支持） | Agent 自己跨会话复用 | 个人偏好、非显而易见的项目事实、跨项目 reference | 下次会话 Agent 忘记历史决策 |
| 项目根 `CLAUDE.md` / `AGENTS.md` | 当前项目里的 AI（下次会话自己） | 项目约定、结构、红线、环境变量、路由清单 | 下次 AI 在这个项目里走弯路 |
| 项目 `docs/` + `README.md` | **其他人**（人类同事、下游开发者、未来接手的 AI） | 接入指南、架构图、运维手册、交接说明、API 参考 | **其他人或系统无法正确接入或运维** |

这三层**受众不同，职责不重叠**。CLAUDE.md 里写"新增了 device flow 五个路由" ≠ docs/integration-guide.md 里"下游怎么接这套 flow" —— 前者是提醒自己，后者是教别人。**两份都要写。**

> **Agent 记忆系统的具体位置因平台而异**（Claude Code 在 `~/.claude/projects/<...>/memory/`，Codex 用 `AGENTS.md`，OpenCode 用 `.opencode/`，OpenClaw 用 `~/.openclaw/`）。完整路径速查见 [references/agent-paths.md](references/agent-paths.md)。如果当前 agent 没有独立的记忆系统，直接跳过这一层，把功夫全花在 docs 和项目根 markdown 上。

## 执行流程

### 第一步：盘点现状（强制机械式枚举，不能跳过）

**先做 ls，再做判断。**

1. 列出 agent 的记忆文件（如有）：
   - Claude Code：`ls ~/.claude/projects/<...>/memory/` 并读 `MEMORY.md` 及所有被引用的 `.md`
   - Codex / OpenCode / 其他：找该 agent 的等价位置（见 references/agent-paths.md）
2. 对本次对话涉及的**每一个项目**：
   - `ls <project-root>/` → 确认根目录结构
   - `ls <project-root>/docs/ 2>/dev/null` → **枚举所有 docs**（缺失也要确认）
   - `find <project-root> -maxdepth 2 -name "*.md" -not -path "*/node_modules/*" -not -path "*/.git/*"` → 兜底抓散落的 .md
   - 读 `README.md`、`CLAUDE.md` / `AGENTS.md`、每一个 `docs/*.md`
3. 读全局 agent 配置（若有，如 `~/.claude/CLAUDE.md`、`~/.codex/AGENTS.md`）
4. 回顾本次对话全部内容

**输出一张文件清单**（内部用，不用给用户看），对每个文件标：「评估过 / 要改 / 不用改」。**漏一个不行**——这是这个 skill 最容易翻车的地方。

### 第二步：识别变更——用"变更影响矩阵"思考

**不要只看对话增量有什么新事实，要看新事实会波及哪些文档层级。**

常见模式速览：
- 新增 API / 路由 → CLAUDE.md 路由清单 + integration-guide + architecture 的 Routes
- 新增 / 改名 环境变量 → CLAUDE.md 环境变量表 + runbook + 下游 integration-guide
- 新增数据库表 → CLAUDE.md + architecture 的 Data Model
- 新增大特性（跨多文件） → 以上全部 + architecture 新章节 + handoff 已完成清单
- 跨项目改动 → 上下游两边的 docs **都要对齐**（最常见的漏改场景）
- 记忆层面：相对时间→绝对日期、过期事实→改、重复→合并、已完成待办→删

完整映射表（覆盖更多变更类型与对应文档）见 **[references/sync-matrix.md](references/sync-matrix.md)**——遇到不确定的改动先查这张表。

**关键检查**：这次对话是不是**跨项目**的？如果改了项目 A 且项目 B 依赖它（通过 SDK、API、子域、环境变量），**项目 B 的 docs 也要改**。这是历次同步最常翻的车。

### 第三步：实际修改（用工具，不只是描述）

你必须**真的用 Edit 修改现有文件、用 Write 创建新文件、用删除命令清理废弃文件**。"我会怎么改"的描述不算完成。

**顺序建议**：先改 docs/（改错影响外部）→ 再改 CLAUDE.md/AGENTS.md → 最后理记忆。先动外部优先级最高的，即使中途被打断，读者看到的也是对齐的最新状态。

**编辑原则**：

- **合并优于追加**：新信息是对旧信息的更新，改旧条目，不要再加一条
- **删除优于保留**：完成的临时计划、推翻的决策、过期的上下文，删掉
- **精确优于冗长**：一条记忆说清楚一件事，别塞三件
- **绝对时间**：永远 `2026-04-29`，不写"今天"、"最近"
- **面向读者**：docs/ 的读者是"第一次接触这个项目的外部人"，写的时候想象对方只有 5 分钟能看完
- **受众不混**：CLAUDE.md 里不抄 docs/ 的全文，docs/ 里不写"我记得上次……"——这是记忆的事

**全局配置极度克制**：`~/.claude/CLAUDE.md` / `~/.codex/AGENTS.md` 只有用户在对话中明确表达了**跨项目的核心原则**才动。日常项目细节绝不进全局。

**docs/ 编辑要点**——新增一个能力的文档变更通常要四处都补：
1. **integration-guide** 或对应"外部视角"文档：加**怎么用**（curl / SDK 示例 / 错误码表）
2. **architecture**：加**怎么工作**（数据流、状态机、设计取舍）
3. **runbook**：加**怎么运维**（冒烟命令、故障排查、环境变量）
4. **handoff** 或 CHANGELOG：加**已完成**

API 速查表、环境变量表、术语表是高频查询的结构化信息，**必须保持"所见即最新"**。

### 第四步：自检清单（必须逐项过一遍）

这一步防止"漏改 docs"。改完后逐条检查：

- [ ] 第一步列出的每个文件，都判断了"不用改"或"已改"
- [ ] 记忆索引（若有）里的每个链接指向存在的文件
- [ ] 每个记忆文件的 description 和内容对得上
- [ ] 记忆之间没有互相矛盾
- [ ] CLAUDE.md / AGENTS.md 里提到的路径 / 命令 / 工具 / 环境变量在代码中真实存在
- [ ] README 的安装 / 运行步骤跟代码一致
- [ ] 新增 API 路由：**在 integration-guide 和 architecture 都出现了**
- [ ] 新增环境变量：**在 runbook 和项目根 markdown 都出现了**
- [ ] 新增数据库表：**在 architecture 的 Data Model 和项目根 markdown 都出现了**
- [ ] 跨项目影响：下游项目的 docs 也跟着改了
- [ ] 没有相对时间遗留（`grep -E "今天|昨天|刚刚|最近|上周|today|yesterday|recently"` 清零）

哪条打不了勾，**回去补**。不要因为"差不多了"就跳过这一步——这是这个 skill 的灵魂。

### 第五步：变更摘要

在所有文件修改完之后（不是之前），给用户简洁摘要：

```
## 同步完成

### 记忆变更
- 更新：xxx（原因）
- 新增：xxx
- 删除：xxx（原因）

### 文档变更（按项目分组，每个项目列全改动的文件）
- <项目 A>/CLAUDE.md — xxx
- <项目 A>/docs/integration-guide.md — xxx
- <项目 A>/docs/architecture.md — xxx
- <项目 B>/docs/<integration>.md — xxx

### 未处理
- xxx（为什么没处理，比如需要用户确认）
```

只列有实际变更的条目。没改的不写。

## 特殊情况

**项目还没有 README 或 CLAUDE.md/AGENTS.md**：判断项目是不是到了"有可运行代码"的阶段。是 → 创建。还在 vibe 阶段 → 跳过，但在摘要里提一句。

**对话没有产生新事实**：审查现有记忆和文档有没有过期 / 冲突 / 相对时间——审查本身就有价值。

**记忆之间出现无法自动判断的矛盾**：列在「未处理」让用户决定。**这是唯一需要用户介入的情况**，其他都自己拍板。

**跨项目改动**：本次对话改了多个项目，每个项目都要跑一次完整的第一步（ls + 读 docs）。不要假设一个项目的 docs 改了，另一个就不用。尤其是上游-下游对接文档（集成指南 / SDK 说明 / API 协议），两边都要对齐。

**skills 双路径同步（.hermes/skills 和 .agents/skills）**：这两个目录存放的是 Hermes Agent 的 skills。每次修改 skill 后，必须用 `diff -rq` 确认两边内容一致，不一致则复制同步。不要假设它们会自动同步——这是 agent 环境特有的注意事项。

**Skill-retro updates**：当用户明确说"这一版严谨性合适"、"总结踩坑"、"复盘"、"更新 skill / skills"时，要把成功经验写回相关 skill，而不是只给一次性总结。只沉淀可复用操作规则，不写项目专属事实、临时结论或具体项目路径。复盘时优先记录会导致下次重复犯错的失败模式，例如：过宽的 `6 of 6`、把 partial evidence 当 direct support、采访者内容污染 evidence、同一人多文件被重复计数、compare/contrast 分组过度排他。修改 skill 后必须同步 `.agents/skills/<skill>` 与 `.hermes/skills/<skill>`，并用 `diff -rq` 验证一致。

**发现之前的同步漏了东西**：修掉。不要说"那不是这次对话的事"——你就是这个项目的持续编辑，过去的漏洞也归你管。

## 踩坑记录（Pitfalls）

以下是历次 neat-freak 执行中实际踩过的坑。每个都是真实的翻车现场，不是理论假设。

### P1：跳过第一步机械枚举

**症状**：直接凭记忆判断「这个文件应该不用改」「那个目录应该没东西」，跳过 `ls` + `find`。

**后果**：残留空目录、副本文件、tmp 文件被漏掉。Isaac 会注意到这些，因为他对文件系统很敏感。

**修法**：第一步的 `ls` 和 `find` 是强制命令，不是建议。输出文件清单时每个文件必须标「评估过 / 要改 / 不用改」。宁可多列一个不存在的路径，不能漏一个存在的文件。

### P2：sed 替换后不 grep 验证

**症状**：用 `sed` 做 Unicode 替换（如弯引号替换），替换完就过了，不做验证。

**后果**：弯引号→全角方括号那次翻车——sed 静默失败，替换没生效，直到下次 neat 才被发现。

**修法**：任何 `sed` / `patch` 字符级替换后，立即 `grep` 验证目标字符是否真的清零。例：`grep '"' file.md` 确认直引号清零，`python3 -c "print(open('f').read().count('\u0022'))"` 确认傻引号清零。

### P3：英文傻引号 `"` (U+0022)

**症状**：写 markdown 文档时习惯性用 ASCII 直引号 `"`，而不是弯引号 `\u201c` `\u201d`。

**后果**：排版上差一个档次。Isaac 会注意到。

**修法**：所有写入的中文文件，写完立刻跑 `python3 -c "print(open('file.md').read().count('\u0022'))"` 验证 U+0022 傻引号清零。弯引号正确写法：左 `\u201c` 右 `\u201d`。

### P4：YAML frontmatter 里 `*` 炸解析

**症状**：skill 的 YAML frontmatter description 里写了 `*action*` 之类的 Markdown 强调语法。

**后果**：`*` 在 YAML 里是 alias 语法，strict YAML parser 会报 frontmatter-parse 错误。

**修法**：skill description 里的 `*` 全部删掉，或者用双引号包住整个 description 值。但更好的做法是——skill frontmatter description 根本不需要 Markdown 格式，纯文本就够了。

### P5：curate-skills merge 后单文件超 500 行

**症状**：`curate-skills` 合并 skill 时，把被吸收的 skill 内容全部 inline 展开到 umbrella skill 里。

**后果**：`claude-design` 吸收 `sketch` 后膨胀到 629 行，远超合理范围。

**修法**：merge 后检查行数。超 500 行时：
- 砍掉可以引用的内容（如 Runtime Mode 列表）
- 用 `references/` 子文件分担长内容
- 引用兄弟 skill 不展开（如「Typography/Color/Layout 参见 CDB skill」）
- 压缩 Verification 步骤为 checklist

### P6：memory replace 的 old_text 盖错条目

**症状**：用 `memory(action='replace')` 时，`old_text` 太短或太泛，匹配了多条记忆中的不相关条目。

**后果**：把不该改的记忆改掉了。

**修法**：`old_text` 必须包含足够的上下文，确保唯一匹配。如果两条记忆内容相近，考虑合并成一条再操作，而不是冒险做 replace。

### P7：skills 双路径不同步

**症状**：改了 `.hermes/skills/` 下的 skill，忘了同步到 `.agents/skills/`。

**后果**：两个目录的同一 skill 内容不一致，不同 agent 读到不同版本。

**修法**：每次修改 skill 后，立即 `cp` 同步 + `diff -rq` 验证一致。不要假设它们会自动同步。

### P10：defense 流水线被当单步用——跳步直接讲故事

**症状**：用户说「写成长故事」，agent 直接加载 `growth-story-synthesizer` 开始写。跳过了 `defense-evidence-extractor`（抽证据）和 `defense-thread-mapper`（找明暗线）。

**后果**：
- 故事没有证据骨架——结论飘在空中，回溯不到原始 memo
- 没有明暗线分析——故事变成平铺的叙事，缺少「为什么这个月值得讲」的穿透力
- 矫正句式泛滥——growth-story-synthesizer 本身是中英双语 skill，写中文时如果不走 evidence extraction 先过一遍原始 memo，很容易把 AI 味的句式写进去

**修法**：
- 涉及 defense / 成长故事写作时，三步必须按顺序走：`defense-evidence-extractor` → `defense-thread-mapper` → `growth-story-synthesizer`
- 第一步产出的证据银行是后面两步的输入，不能跳过
- 如果用户提供的材料已经包含 evidence extraction 的结果（如 monthly review 已有 timeline + 证据），可以缩短第一步，但不能完全跳过
- 三步都跑完后，再走 natural-chinese-writing 审查 + Isaac 铁律扫描（引号、矫正句式、呼吸感）

**症状**：把「不是……而是……」改写成「没在……在……」或「没……在……」，以为换了个否定词就不是矫正句式了。

**后果**：结构完全一样——否定一个解释，确立另一个。读者读到「没恐慌。在搭脚手架。」和读到「这不是恐慌，是搭脚手架。」——感受到的是同一种 AI 味。

**修法**：直接删掉否定部分，只陈述 Y。❌「没恐慌。在搭脚手架。」→ ✅「在搭脚手架。」

**症状**：在一个 neat-freak 会话里，同一个文件被多次 patch，中间没有重新读取。

**后果**：后面的 patch 基于过期的行号/内容，可能打错位置或失败。

**修法**：如果一个文件要改多处，先读一遍，把要改的地方全部列出来，尽量合并成一次 `patch`（`replace_all=true` 或一个大的 `old_string`）。如果必须多次改，每次改完后重新 `read_file` 确认当前状态再改下一处。

### P11：截图 / 取证任务把探测图和超范围内容留在交付目录

**症状**：为了确认滚动方向、窗口坐标或日期边界，先截了测试图；后来为了覆盖完整范围又多滚了几屏。任务完成时只看到了“已经截到”，没有回头清理测试图、重复图、超过用户要求时间范围的图。

**后果**：交付目录混入无关文件，严重时会把用户没要求保存的隐私内容一起留下。对“近一周”“某个日期范围”“只要当前窗口”这类任务尤其危险。

**修法**：
- 先生成 `index_contact_sheet` 或同等总览，核对范围边界和重复页。
- 只保留用户要求范围内的正式交付文件；测试图、探测图、重复图、超范围图都要清掉。
- 受“禁止批量删除”约束时，只能逐个 `rm /明确/路径/文件`，不能用通配符或递归删除。
- 最后重新生成索引，并用 `ls -lh` 验证目录里只剩正式文件和索引。

### P12：Computer Use 不可用时，没有及时切到 Apple 原生自动化 fallback

**症状**：Computer Use MCP 报 `runtime app is missing`、`Transport closed` 或 appshot 无法 attach 时，继续反复调用插件，耽误执行；或者反过来，直接写一堆不受控的点击脚本，变成高风险盲点。

**后果**：任务卡在工具层，或者脚本误点点赞、评论、发送、删除、发布等有副作用控件。截图任务尤其容易发生：其实 macOS 已经给了足够能力，但需要非常克制地使用。

**修法**：
- 可以做 Apple 原生 fallback。优先组合：`CGWindowListCopyWindowInfo` 找窗口坐标，`screencapture -R` 裁剪窗口，CoreGraphics `CGEvent` 做点击和滚动，`osascript` / Accessibility 只用于 `activate`、`AXRaise`、读取窗口属性。
- fallback 只适合“读取、截图、滚动、返回、进入详情”这类低副作用动作；涉及发送、点赞、评论、删除、授权、支付、发布，仍按 Computer Use confirmation policy 或直接停下来。
- 每次点击前先截当前窗口确认坐标；点击点位选正文、图片空白区、返回按钮这类安全区域，避开 `...`、心形、评论框、发送按钮、垃圾桶、发布按钮。
- 脚本必须以“窗口坐标 + 屏幕裁剪验证”为循环，不要假设 UI 永远不变；每次滚动后用截图或 hash 判断是否到边界。
- 交付前清理 `/tmp` 或项目目录里的探测图；如果项目有禁止批量删除规则，逐个明确路径删除。

### P13：Figma 写入脚本失败后继续盲 retry

**症状**：`use_figma` 报脚本错误后，没读错误信息就重跑同一段代码；或者把工具传输错误、脚本验证错误、设计结果不理想混成一类处理。

**后果**：时间浪费在重复失败上。更糟的是，agent 会误以为 Figma 里已经产生了半成品，继续基于不存在的节点做后续操作。

**修法**：
- `use_figma` 的脚本错误按“原子失败”处理：先读报错，修脚本，再重试。
- 参数顺序、字体名、`fontName` 对象、`layoutSizing` 这类错误都属于脚本错误，不要直接 retry。
- 网络传输错误和超时可以对“查询 / 验证 / 上传 URL 获取”做单次重试，但不要把写入脚本错误当网络抖动。
- Figma 写入前先查字体：`figma.listAvailableFontsAsync()`，中文优先用确定存在的 `Noto Sans SC`，英文用 `Inter`。

### P14：Figma 图片上传后忘记清理占位层

**症状**：先在 Figma 里创建图片占位框和说明文字，之后用 `upload_assets` 把图片填进矩形，但忘记隐藏或删除“PLACEHOLDER / 图片占位”文字。

**后果**：截图看起来像图片已经填了，但占位文字可能压在图片上；打印交付物会显得不专业。

**修法**：
- 图片上传流程固定为：创建命名矩形 → `upload_assets` 获取 `submitUrl` → 用 `curl -F file=@...` 上传 → 隐藏占位文字 → 截图检查。
- 验证时不要只看工具返回 `success: true`，还要查目标节点的 fills 是否存在 `IMAGE` 类型。
- 视觉交付必须导出截图并人工看一遍；节点数量和返回 ID 不能替代视觉检查。

### P15：表格验证用固定行号

**症状**：读取 xlsx / csv 时用 `rows[6]` 这类固定索引找总价、单价、合计。

**后果**：只要表头、空行、备注行变化，就会读到错误行。一次真实翻车是成本验证脚本把贴纸单价 `3.4` 当成总计行，导致误报。

**修法**：
- 优先按列名、项目名、合计标记、唯一数值组合查找。
- 如果没有表头，也要用“单价 + 总价 + 备注”组合验证，而不是裸行号。
- 验证脚本失败时先检查读取定位，不要立刻认定源数据错。

### P16：`git diff` 看不到未跟踪文件

**症状**：修改的是未跟踪文件，运行 `git diff -- file` 没输出，就误判“没有改动”。

**后果**：最终摘要漏报文档变更，或者以为 patch 没生效。

**修法**：
- 先看 `git status --short file`。如果是 `??`，说明文件未跟踪，`git diff` 默认不会显示内容差异。
- 对未跟踪文档，用 `rg -n`、`sed -n`、`wc -l` 验证关键字段和章节是否存在。
- final 摘要仍要列实际改过的未跟踪文件，不要被 Git 状态误导。

### P17：Presentations 交付后把 artifact-tool workspace 留在项目里

**症状**：PPTX 已经导出到用户指定目录，agent 也渲染了 previews / contact sheet / layout JSON，但结束时忘记清理 `outputs/<thread>/presentations/<task>` 下的 slide modules、preview PNG、layout JSON、manifest、临时 `package.json` 和 runtime symlink。

**后果**：项目仓库混入一次性生成痕迹。下次 `rg`、`find`、Git 状态和人工接手都会看到与正式材料无关的 build workspace；如果含有截图或中间素材，还可能泄露超出交付范围的内容。

**修法**：
- Final deliverables 只留在用户指定输出目录；项目内 `outputs/<thread>/presentations/<task>` 默认视为 scratch。
- 交付前确认 final PPTX / notes / PDF 已存在且通过 slide count、layout check、contact sheet 检查，再清 scratch。
- 受项目禁止批量删除约束时，不用 `rm -rf`、通配符、`find -delete` 或 cleanup 脚本；只能对明确路径逐个删除，目录清空后逐层 `rmdir`。
- 如果 scratch 内还有需要保留的 QA 记录，先把结论写进最终 notes 或正式 docs，再删除 scratch。

### P18：审计工程吞掉最终交付

**症状**：研究、长文本分析或资料整理任务不断增加 codebook、manifest、hash、分区脚本、复编码门槛和验证报告。中间产物越来越严谨，用户要求的主报告、结论摘要或可读交付始终没有出现。遇到不确定性时继续增加审计层，而不是压缩范围或先写最小成品。

**后果**：额度和时间消耗在内部工程上。即使数据最终可复算，用户仍拿不到能使用的结果；后续 agent 还要先理解大量历史结构，交接成本继续上升。

**修法**：
- 复杂分析开始前同时定义三项预算：最迟交付时间、最大编码或样本范围、最终文件数量。没有预算的严谨性默认会无限扩张。
- 采用“交付骨架优先”：数据边界确认后立即创建最终报告骨架，并在每个分析步骤结束时填入可用结论。任何中间工程都必须能指向一个最终章节。
- 把验证分成“阻断交付”和“可后补”两类。来源错位、UID 丢失、引文不存在属于阻断项；额外 hash、重复 manifest、每分区独立 builder 通常属于可后补项。
- 每完成一个阶段检查一次交付比：正式交付文件仍为 0、而新增中间文件超过 10 个时，必须停止扩建，先产出一版可读报告。
- 对参考项目的更快方案要同时核对范围和质量。缩小月份、截断正文、强迫每条命中代码、用主题相近率代替标准可靠性指标都能提速，但必须作为明确取舍，不能伪装成同等完成。
- 达到时间或额度的 60% 时做一次强制降级：保留核心问题、直接证据、反例和局限；暂停不影响结论的基础设施。达到 80% 时只允许修阻断项和完成最终交付。

## 最佳实践（Best Practices）

### B1：Figma 设计交付按六段走

适用于 One Page、海报、UI mockup、流程图等视觉交付：

1. 读目标 node metadata，确认尺寸和目标 frame。
2. 查字体和 design system；没有可复用组件时才自建基础图形。
3. `use_figma` 一次创建完整可编辑结构，所有关键节点命名清楚。
4. 图片用命名矩形承载，上传后隐藏占位提示。
5. 导出目标 node 截图，用视觉检查修重叠、溢出、遮挡。
6. 用脚本验证关键节点、图片 fills、文本数量或关键文案存在。

### B2：外部证据要做语义验证

成本表、报价表、评分表、调研表都不能只靠“看起来对”。验证时要抓能代表业务含义的字段组合，例如：`65.4 元/套 + 9810 元/150 套`、路由名 + 方法、环境变量名 + 默认值。固定行号、截图肉眼读数、AI 摘要都只能作辅助。

### B3：视觉结果必须截图验收

Figma / 浏览器 / PPT / PDF 这类交付，代码执行成功只说明“生成了东西”，不说明“东西可读”。必须导出截图或渲染结果，检查：

- 图片是否真实显示
- 文本是否重叠、溢出、被裁切
- 打印或缩放后关键信息是否仍可读
- 页面是否包含用户要求的硬性数字和文案

### B4：文档同步要覆盖未跟踪状态

很多项目文档、素材仓库、临时项目一开始全是未跟踪文件。neat-freak 不能只依赖 `git diff`。对未跟踪文件，完成标准是“内容被实际读到并验证”，不是“Git 能显示 diff”。

### B5：PPT / deck 交付按“导出、渲染、检查、清理”闭环

适用于 artifact-tool / Keynote / PowerPoint / PDF deck 生成：

1. 输出 final 文件到用户指定目录，文件名不能泛化成 `deck.pptx` 或 `output.pptx`。
2. 渲染每页预览和 contact sheet，人工检查是否有文档页、重复布局、文字溢出、重点页不够强。
3. 跑机械检查：slide count、非空文件、layout error、notes 章节数。layout warning 要区分真实几何问题和语义标签误报；真实 error 必须修，误报要记录原因。
4. 把可复用的 QA 结论写进最终 notes 或正式交付说明，不把 preview / layout / slide module 留在项目里。
5. 清理 scratch 时遵守项目删除规则；没有权限安全清理时，明确列出应由用户手动删除的目录，不假装已经清掉。

- **[references/sync-matrix.md](references/sync-matrix.md)** — 完整的"变更类型 → 要改哪些文件"映射表
- **[references/agent-paths.md](references/agent-paths.md)** — Claude Code / Codex / OpenCode 各自的记忆与配置路径速查
