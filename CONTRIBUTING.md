# 贡献指南

感谢你考虑为OpenCode Skills Collection贡献！这个仓库旨在收集和分享高质量的OpenCode Skills，让更多人受益。

## 🎯 贡献理念

我们遵循"善及万物"的理念：
- **实用性**：每个skill都应该解决真实问题
- **质量**：代码清晰、文档完整、易于使用
- **分享**：好的工具应该被更多人使用
- **持续改进**：随着反馈不断优化

## 📝 如何贡献

### 1. 报告问题
如果你发现任何问题或有改进建议：
- 查看是否已有相关issue
- 创建新的issue，详细描述问题
- 提供复现步骤和期望结果

### 2. 提交新Skill
如果你想贡献新的skill：

#### 步骤1：准备skill
- 确保skill是你原创或获得授权的
- 遵循现有的skill结构
- 包含完整的SKILL.md文档
- 经过实际测试验证

#### 步骤2：创建Pull Request
1. Fork本仓库
2. 创建新的分支：`git checkout -b feature/new-skill-name`
3. 添加你的skill文件夹
4. 提交更改：`git commit -m "feat: add new-skill-name skill"`
5. 推送到你的fork：`git push origin feature/new-skill-name`
6. 创建Pull Request

### 3. 改进现有Skill
- 修复bug
- 改进文档
- 优化代码
- 添加测试用例
- 提供更好的示例

## 🏗️ Skill质量标准

### 必须包含：
1. **SKILL.md文件**：包含完整的元数据和说明
2. **清晰的触发条件**：明确何时使用该skill
3. **使用示例**：展示如何在实际中使用
4. **工作流程**：详细的操作步骤
5. **注意事项**：潜在问题和限制

### 建议包含：
1. **参考文档**：在references/目录中
2. **辅助脚本**：在scripts/目录中
3. **测试用例**：验证skill功能
4. **兼容性信息**：支持的格式和工具

### 代码质量：
- 使用清晰的命名
- 添加必要的注释
- 遵循一致的代码风格
- 避免硬编码路径和配置

## 📁 项目结构

```
opencode-skills/
├── skill-name/          # skill主目录
│   ├── SKILL.md        # 主技能文件（必须）
│   ├── references/     # 参考文档（可选）
│   ├── scripts/       # 辅助脚本（可选）
│   └── examples/      # 使用示例（可选）
├── README.md          # 项目说明
├── CONTRIBUTING.md    # 贡献指南
├── LICENSE           # 许可证
└── .gitignore        # Git忽略文件
```

## 📄 SKILL.md格式要求

### 元数据部分（YAML frontmatter）：
```yaml
---
name: skill-name
description: 简洁的技能描述
compatibility: [pdf, spreadsheet, markdown] # 可选
user-invocable: true # 可选
---
```

### 内容部分：
1. **技能介绍**：这是什么skill，解决什么问题
2. **触发条件**：何时使用这个skill
3. **工作流程**：详细的操作步骤
4. **使用示例**：具体的代码示例
5. **注意事项**：限制和潜在问题
6. **相关资源**：参考链接和文档

## 🧪 测试要求

在提交前，请确保：
1. skill在实际OpenCode环境中工作正常
2. 文档中的示例可以正确运行
3. 没有破坏性更改
4. 兼容性声明准确

## 💬 沟通准则

- 使用友好、尊重的语言
- 提供具体的反馈和建议
- 保持讨论专注于技术问题
- 尊重不同的观点和经验

## 📜 许可证

所有贡献都将采用MIT许可证。提交贡献即表示你同意你的代码将在此许可证下发布。

## 🙏 致谢

感谢所有贡献者的时间和努力！每一个贡献都让这个项目变得更好。

---

**善及万物，分享智慧** - 让我们一起构建更好的AI工具生态系统！