# Isaac's Skills Collection

> 善及万物 - Isaac 的部分自用 Skills

## 项目简介

这个仓库收集了一批可直接落地的 Skill 模块，目标是让 AI 助手在学习辅导、决策分析、技能治理和工作流自动化中更稳定、更好用。

每个 Skill 都围绕一个明确问题设计，包含触发条件、使用边界和执行流程，便于你按需组合。

## 当前收录 Skills

> 已同步为仓库实际存在的目录（共 10 个）

| 分类 | Skill | 说明 |
| --- | --- | --- |
| Learning | `paogen-wendi` | 通过"刨根问底"方式定位并补齐前置知识 |
| Learning | `article-easier-reader` | 将英文文章转为易读版学习文档 |
| Writing / Analysing | `option-enumerator` | 系统枚举方案并比较取舍与风险 |
| Writing / Analysing | `curate-skills` | 审查并重构 Skill 库结构与质量 |
| Coding | `macos-command-launcher` | 构建可启动本地命令的 macOS 启动器 |
| Coding | `opensource-release-guard` | 开源仓库发布前检查与流程辅助 |
| Agent | `agent-config-audit` | 审计本地 Agent 配置但不做任何修改 |
| Agent | `repo-harness-minimal` | 为编码 Agent 项目提供最小可重启工作流 |
| General | `normally` | 用自然、低 AI 痕迹的方式解释简单概念 |
| Agent | `personal-harness` | 个人 Agent 工作的顶层路由与任务分配 |

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
