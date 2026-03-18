# 术语库分片

本目录按领域拆分术语库，避免多个 agent 改同一个文件。

建议分片：

- `brands.yml`
- `marvelous-designer.yml`
- `vrchat.yml`
- `unity.yml`
- `modeling.yml`
- `workflow.yml`

字段约定：

- `source_term`: 日文源术语
- `canonical_zh_cn`: 固定中文译法
- `domain`: 术语领域
- `preferred`: 是否主译法
- `source_type`: `official_zh` / `official_en` / `repo_glossary` / `repo_context`
- `source_refs`: 事实来源列表
- `notes`: 使用说明，可为空
- `aliases`: 可接受别名列表，可为空
