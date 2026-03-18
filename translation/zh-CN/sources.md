# 术语来源层级

更新时间：2026-03-18

中文翻译统一按以下来源优先级决策：

1. 官方中文文档或官方中文界面
2. 官方英文文档中的产品名、功能名、组件名
3. 仓库内的日文术语定义与章节上下文
4. 行业通用译法

## 核心官方来源

### Unity

- Unity User Manual 2022.3: https://docs.unity3d.com/cn/2022.3/Manual/
- 变换组件: https://docs.unity3d.com/cn/2022.3/Manual/class-Transform.html
- 材质简介: https://docs.unity3d.com/cn/2022.3/Manual/materials-introduction.html
- Shader 类: https://docs.unity3d.com/cn/2022.3/Manual/shader-objects.html
- Skinned Mesh Renderer component: https://docs.unity3d.com/cn/2021.3/Manual/class-SkinnedMeshRenderer.html
- Meshes introduction: https://docs.unity3d.com/cn/2022.3/Manual/mesh-introduction.html

### VRChat

- VRChat Creation: https://creators.vrchat.com/
- PhysBones: https://creators.vrchat.com/common-components/physbones
- Performance Ranks: https://creators.vrchat.com/avatars/avatar-performance-ranking-system

### Marvelous Designer

- Marvelous Designer Support: https://support.marvelousdesigner.com/
- Particle Distance Setting: https://support.marvelousdesigner.com/hc/en-us/articles/360037022752-Particle-Distance-Setting
- Marvelous Designer File Format: https://support.marvelousdesigner.com/hc/en-us/articles/47358169252633-Marvelous-Designer-File-Format
- Compatible File Format: https://support.marvelousdesigner.com/hc/en-us/articles/47358199862553-Compatible-File-Format
- Remeshing: https://support.marvelousdesigner.com/hc/en-us/articles/47358347315481-Remeshing
- Avatar Skin Offset Setting: https://support.marvelousdesigner.com/hc/en-us/articles/47358339835929-Avatar-Skin-Offset-Setting

## 仓库内来源

- 总术语页：`docs/basics/terminology.md`
- 章节标题与导航：`mkdocs.yml`、`docs/**/*.md`
- 链接结构与文件路径：`docs/**/*.md`

## 固定规则

- `Unity`、`VRChat`、`Marvelous Designer`、`PhysBone`、`EveryWear`、`CLO-SET Connect` 等产品/功能名默认保留官方写法。
- Unity 已有官方中文译名的通用术语，优先采用 Unity 中文手册写法。
- VRChat 没有稳定官方中文译名的功能名，默认保留英文名，正文首次出现时可补充中文解释。
- Marvelous Designer 的文件格式和参数名优先保留官方英文项名，再给出中文说明。
