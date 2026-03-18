# 中文翻译工作区

本目录用于管理仓库的简体中文翻译资产，而不是直接混入现有日文文档源。

当前约定：

- 原文：`docs/**/*.md`
- 中文译文：`docs/zh-CN/**/*.md`
- 术语源：`translation/zh-CN/glossary/*.yml`
- 术语索引：`translation/zh-CN/index_terms.csv`
- 译法规则：`translation/zh-CN/translation-rules.md`

工作原则：

1. 先固定术语，再批量翻译章节。
2. 品牌名、组件名、功能名优先遵循官方文档或官方产品命名。
3. 没有官方中文译法时，保留官方英文名，并在需要时补充中文说明。
4. 译文保持 Markdown 结构、相对链接和代码/路径不变。
5. 一切新的固定译法都必须回写到术语库，而不是只存在于某个 agent 的上下文里。
