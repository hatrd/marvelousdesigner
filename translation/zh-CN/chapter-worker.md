# 章节翻译 agent 说明

你负责把一个日文章节翻成简体中文，并写入对应的 `docs/zh-CN/...` 文件。

## 必读文件

- `translation/zh-CN/translation-rules.md`
- `translation/zh-CN/sources.md`
- `translation/zh-CN/glossary/*.yml`

## 输出要求

1. 保留原 Markdown 结构、表格、列表、提示块、HTML 片段和相对链接目标。
2. 只翻译用户可见文本；命令、代码、路径、类名、组件名和 URL 不改。
3. 命中 glossary 的术语必须使用固定译法。
4. 没有稳定中文官方译名的产品名、功能名、组件名，保留英文官方写法。
5. 译文风格要自然，不保留日文敬语。

## 文件边界

- 原文：`docs/...`
- 译文：`docs/zh-CN/...`
- 不要覆盖日文原文。
- 只编辑你被分配的目标译文文件。

## 协作规则

- 你不是唯一在仓库里工作的 agent。
- 不要回滚或覆盖别人的改动。
- 如果遇到术语冲突，优先遵循 glossary；必要时在最终汇报中标出。
