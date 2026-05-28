# Isaac's Skills Collection

> 善及万物 - Isaac 的部分自用 Skills

## 项目简介

这个仓库收集了一批可直接落地的 Skill 模块，目标是让 AI 助手在学习辅导、决策分析、技能治理和工作流自动化中更稳定、更好用。

每个 Skill 都围绕一个明确问题设计，包含触发条件、使用边界和执行流程，便于你按需组合。

## 当前收录 Skills

> 已同步为仓库实际存在的目录（共 17 个）

| 分类 | Skill | 说明 |
| --- | --- | --- |
| Learning | `paogen-wendi` | 学一个东西卡住了，但不知道卡在哪？这个 skill 帮你一路往回找，揪出你真正缺的那块知识，补上了再往前走 |
| Learning | `article-easier-reader` | 英文文章读得头大？丢给它，帮你转成好读的中文笔记——生词、长难句、隐藏的逻辑线，全给你拆开 |
| Academic | `ielts-writing-review` | 帮你改雅思或学术作文。原则很简单：先确保把话说清楚，再考虑要不要换高级词。反对模板句堆砌，主张你独立表达 |
| Academic | `literary-analysis-reader-revision` | 你写了篇文学分析论文，但老师没读过原著？这个 skill 帮你重写，让你的论文不再假设读者都知道背景 |
| Academic | `meaningful-life-interview-analysis` | 做了一堆采访，不知道从哪开始分析？这个 skill 帮你从采访稿里找出共同规律、对比不同人的回答、填好分析表格 |
| Narrative Presentation/Slides | `defense-presentation-narrative-reviewer` | 答辩 PPT 准备好了没？这个 skill 帮你检查：故事线顺不顺、证据够不够硬、每一页到底有没有必要存在 |
| Writing / Analysing | `option-enumerator` | 面对几个方案不知道怎么选？这个 skill 帮你把每个选项的优点、坑、代价都摆到桌面上，排好推荐顺序 |
| Writing / Analysing | `curate-skills` | 你的 skill 文件夹越堆越乱？这个 skill 帮你整理——删重复的、修写错的、归好类，剩下清爽的一套 |
| Writing / Analysing | `question-praise-reflection-coach` | 写了篇日记或反思，不知道接下来怎么往下想？这个 skill 从你写的东西里抓出你自己都没注意到的亮点，然后问几个好问题，推你继续深挖 |
| Writing | `khazix-writer` | 想用数字生命卡兹克的风格写公众号长文？这个 skill 帮你按他的写作方法论出稿——从选题判断、风格把控到四层质检，完整走完一篇有活人感的文章 |
| Writing | `natural-chinese-writing` | 写出来的中文总像 AI 翻译的？这个 skill 帮你把译文感、顾问腔、套话过渡全洗掉，改成自然、直接、像真人写的中文 |
| Coding | `macos-command-launcher` | 想在 Mac 上做个一键启动命令的小工具（比如一键开服务、一键跑脚本）？这个 skill 帮你搭出来 |
| Coding | `opensource-release-guard` | 代码准备开源？这个 skill 先帮你扫一遍有没有泄露的密码、私人信息、不该出现的文件，然后告诉你安全发布分几步 |
| Agent | `agent-config-audit` | 不确定你的 AI 助手配置有没有写错？这个 skill 帮你全部检查一遍，只告诉你哪里不对，不动你的任何文件 |
| Agent | `repo-harness-minimal` | 想让 AI 帮你写代码，但每次都得从头解释项目背景？这个 skill 帮你生成一套最小配置文件，下次 AI 进来就知道项目是什么、规则是什么 |
| General | `normally` | 想用正常人聊天的方式解释一个概念？这个 skill 帮你写出来不像 AI 写的，像朋友在跟你说话 |
| Agent | `personal-harness` | 有好几个 AI 工具不知道什么活该交给谁？这个 skill 帮你做总调度——看一眼任务类型，直接告诉你调哪个 skill 最合适 |

## 安装与使用

### 方式一：直接复制目录

```bash
# 复制某个 skill 到你的 skills 目录
cp -R teacher-style-review /path/to/your/skills/
```

### 方式二：以仓库为子模块

```bash
git submodule add https://github.com/<your-org>/<your-repo>.git skills-collection
```

### 方式三：完整克隆后按需引用

```bash
git clone https://github.com/<your-org>/<your-repo>.git
```

> 不同 AI 运行时对技能加载方式不同，请以你所用平台文档为准。

## 目录约定

每个 Skill 建议遵循以下结构：

```text
skill-name/
├── SKILL.md          # 必需：技能定义与执行说明
├── references/       # 可选：背景资料、规范、案例
├── scripts/          # 可选：自动化脚本
└── examples/         # 可选：示例输入输出
```

## 如何新增一个 Skill

1. 创建目录：`mkdir your-skill-name`
2. 编写 `SKILL.md`（建议包含：目标、触发条件、边界、流程、验证）
3. 如有需要补充 `references/` 或 `scripts/`
4. 自测至少 1~2 个真实用例
5. 提交 PR

## 贡献原则

- 内容必须原创，或已获得明确授权
- 触发条件清晰，避免“大而全”描述
- 边界明确，说明“不该用在什么场景”
- 示例可复现，避免仅有口号式说明

## 路线图

- [ ] 增加更多跨场景实用 Skills
- [ ] 为常用 Skill 增加标准化样例
- [ ] 补充自动化验证脚本
- [ ] 建立轻量质量评估机制

## 许可证

本项目采用 [MIT License](LICENSE)。

---

**善及万物，分享智慧。**
