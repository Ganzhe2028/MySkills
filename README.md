# OpenCode Skills Collection

> 善及万物，分享智慧 - 一个由我创建并开源的高质量OpenCode Skills集合

## 📚 项目简介

这是一个专门收集和分享我创建的OpenCode Skills的仓库。OpenCode Skills是用于增强AI助手能力的专业技能模块，每个skill都针对特定任务进行了优化和精炼。

## 🎯 项目理念

- **善及万物**：好的工具应该被更多人使用和受益
- **实用优先**：每个skill都经过实际使用验证，解决真实问题
- **质量保证**：代码清晰、文档完整、易于集成
- **持续更新**：随着使用反馈不断改进和优化

## 🛠️ 可用Skills

### 当前包含的Skills：

1. **teacher-style-review** - 教师风格复习技能
   - 模拟特定教师的教学、复习、测试和反馈风格
   - 特别适合概念+证据类课程（如积极心理学）
   - 支持范围映射、复习计划、练习题目生成、答案评分

2. **macos-command-launcher** - macOS命令启动器
   - 构建可重复使用的macOS命令启动器应用
   - 支持Spotlight启动、终端包装、后台启动器、LaunchAgent
   - 提供明确的绝对路径，无PATH依赖

3. **normally** - 自然解释技能
   - 用直接、自然、低AI痕迹的方式解释简单概念
   - 适合简短概念问题，避免过度工程化解释

4. **option-enumerator** - 选项枚举器
   - 为架构、工具、调试和工作流决策枚举具体选项
   - 比较权衡、失败模式、工作量，提供推荐顺序

## 📦 安装和使用

### 方法一：直接复制
```bash
# 复制skill文件夹到你的OpenCode skills目录
cp -r teacher-style-review ~/.config/opencode/skills/
```

### 方法二：使用skill工具
```bash
# 在OpenCode环境中使用skill工具加载
skill(name="teacher-style-review")
```

### 方法三：Git子模块
```bash
# 将整个仓库添加为子模块
git submodule add https://github.com/yourusername/opencode-skills.git skills-collection
```

## 🏗️ Skill结构

每个skill都遵循标准结构：
```
skill-name/
├── SKILL.md          # 主技能定义文件
├── references/       # 参考文档（可选）
├── scripts/         # 辅助脚本（可选）
└── examples/        # 使用示例（可选）
```

### SKILL.md文件格式
```yaml
---
name: skill-name
description: 技能描述
compatibility: [pdf, spreadsheet, markdown] # 可选
user-invocable: true # 可选
---

# 技能标题

详细的使用说明、工作流程、示例等...
```

## 🔧 开发新Skill

### 创建步骤：
1. 创建skill文件夹：`mkdir new-skill-name`
2. 编写SKILL.md文件，包含元数据和详细说明
3. 添加必要的辅助文件（scripts/, references/等）
4. 测试skill功能
5. 提交到仓库

### 最佳实践：
- **明确触发条件**：清晰定义何时使用该skill
- **完整文档**：包含使用示例、工作流程、注意事项
- **实际测试**：确保skill在实际场景中有效
- **保持简洁**：专注于解决特定问题

## 🤝 贡献指南

欢迎贡献你的skills！请遵循以下步骤：

1. Fork本仓库
2. 创建你的skill文件夹
3. 确保包含完整的SKILL.md文档
4. 提交Pull Request
5. 提供使用示例和测试说明

### 贡献要求：
- 必须是原创或获得授权的skill
- 必须有完整的文档
- 必须经过实际测试
- 遵循现有的skill结构

## 📖 使用示例

### 使用teacher-style-review：
```javascript
// 在OpenCode环境中
skill(name="teacher-style-review")

// 然后可以请求教师风格的复习帮助
// "帮我分析这个测试的风格"
// "生成一些教师风格的练习题"
// "像我的老师一样评分这个答案"
```

### 使用macos-command-launcher：
```javascript
skill(name="macos-command-launcher")

// 创建Spotlight可启动的应用
// "为我的本地服务器创建一个启动器"
// "制作一个后台同步服务的LaunchAgent"
```

## 🚀 路线图

- [ ] 添加更多实用skills
- [ ] 创建skill模板生成器
- [ ] 添加自动化测试
- [ ] 建立skill评级系统
- [ ] 创建skill市场原型

## 📄 许可证

本项目采用MIT许可证 - 详见[LICENSE](LICENSE)文件。

## 🙏 致谢

感谢所有使用和贡献这些skills的开发者。特别感谢OpenCode社区提供的灵感和支持。

---

**善及万物，分享智慧** - 让我们一起构建更好的AI工具生态系统！