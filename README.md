# Isaac’s Skills Collection

> 善及万物 - Isaac 的部分自用 Skills

## 项目简介

这个仓库收集了一批可直接落地的 Skill 模块，目标是让 AI 助手在学习辅导、决策分析、技能治理和工作流自动化中更稳定、更好用。

每个 Skill 都围绕一个明确问题设计，包含触发条件、使用边界和执行流程，便于你按需组合。

## 当前收录 Skills

> 已同步为仓库实际存在的目录（共 13 个）

| 分类 | Skill | 说明 |
| --- | --- | --- |
| Learning | `adaptive-learning-workbook` | 自学或练习做到一半，不知道下一步该练什么？这个 skill 读你最近做的练习和批注，找出当下最该补的那个小缺口，生成下一页可以直接改的 Notion 练习页。雅思和英语自学尤其适用 |
| Design | `cdb-design-foundations` | 还没想清楚设计要干什么就动手了？这个 skill 先帮你定观众、信息、约束，再定功能、效率、情感三个目标，顺便分清自我表达和设计交付的差别 |
| Design | `cdb-design-review` | 海报、PPT、界面做出来了，不知道行不行？这个 skill 按功能、效率、情感三个维度打分，列出一份改什么、为什么改、改完怎么验证的清单 |
| Design | `cdb-color` | 配色越用越乱，或者压根不知道怎么下手？这个 skill 从颜色该干的活出发帮你定主色、辅助色、强调色，再查对比度和含义一致性 |
| Design | `cdb-image-shape` | 纠结用位图还是矢量图，图标风格怎么统一？这个 skill 帮你判断图片和形状该承担什么，再查分辨率、裁剪、风格一致性，给出具体改法 |
| Design | `cdb-layout` | 信息全堆在页面上，读者不知道先看哪？这个 skill 帮你排阅读顺序、把相关内容归组，再用对比、重复、对齐、亲密性四项过一遍版式 |
| Design | `cdb-typography` | 字体换来换去还是觉得别扭？这个 skill 帮你选字体、定字号层级、调字重，中英文混排怎么处理也有一套方法 |
| Design | `cdb-storyboarding-slides` | 要做 PPT 但不知道先讲什么？这个 skill 教你 storyboarding——先定每页要干的事，再排转场，盯着观众注意力别走丢 |
| Writing | `natural-chinese-writing` | 写出来的中文总像 AI 翻译的？这个 skill 帮你把译文感、顾问腔、套话过渡全洗掉，改成自然、直接、像真人写的中文 |
| Coding | `macos-command-launcher` | 想在 Mac 上做个一键启动命令的小工具（比如一键开服务、一键跑脚本）？这个 skill 帮你搭出来 |
| Coding | `storage-analyzer` | 电脑硬盘满了，不知道什么东西在占空间？这个 skill 只读扫描整块磁盘，找出占空间大户，把每项分成能自动清理、需人工判断、谨慎清理三级，生成一份能折叠、命令可一键复制的 HTML 报告，还能起本地服务在网页上一键删除 |
| Coding | `website-to-hyperframes` | 想用一个网址做条视频？这个 skill 把网页录下来，用 HyperFrames 做成产品介绍、社交广告或演示视频 |
| Agent | `neat-freak` | 项目告一段落，文档和 agent 记忆还停在老版本？这个 skill 把 CLAUDE.md、README 这些文档跟实际代码逐项对一遍，烂掉的同步掉，洁癖级不留死角 |

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
