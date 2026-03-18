# Unity 集成项目设置指南

!!! note "指南信息"
    **预计耗时**: 约 60 分钟 | **难度**: 适合初学者 | **重要度**: 必须（VRChat 实用化）

**本页目标**: 在 Unity 中集成使用 Marvelous Designer 制作的服装，并搭建可作为 VRChat 模型使用的基础环境。

!!! success "本指南将实现的内容"
    - ✅ 让制作好的服装真正可以在 VRChat 中穿着
    - ✅ 获得 Unity + VRChat SDK3 的实战操作体验
    - ✅ 理解完整的模型制作工作流
    - ✅ 完成属于自己的自定义模型

!!! info "事前准备"
    - [Unity・VRChat SDK 设置](../setup/unity-vrchat-setup.md)已完成
    - 已在 Marvelous Designer 中制作好服装（例如 T 恤）
    - 服装已导出为 FBX 格式
    - 可以登录 VRChat 账号

## 🎯 集成全貌

### 工作流概览

!!! info "Marvelous Designer → Unity → VRChat 的流程"

    **1. Marvelous Designer 阶段**（已完成）
    - 导入模型
    - 制作并适配服装
    - 导出为 FBX 格式

    **2. Unity 集成阶段**（本次执行）
    - 项目设置
    - 集成模型与服装
    - 配置 VRChat SDK3

    **3. VRChat 发布阶段**（下一步）
    - 构建与测试
    - 上传与发布
    - 在 VRChat 内确认

## 🚀 步骤 1: 准备 Unity 项目

### 确认 VCC 项目

!!! example "步骤 1-1: 确认项目状态"

    **确认现有项目**:
    1. 启动 **VRChat Creator Companion**
    2. 确认之前创建的项目“VRChat 服装制作项目”
    3. 点击 **“Open Project”** 用 Unity 打开

    **如果需要新建项目**:
    1. 在 VCC 中选择 **“Create New Project”** → **“Avatar”**
    2. 项目名: `VRChat_Garment_Integration`
    3. 保存位置: “VRChat衣装制作/UnityProjects/” 文件夹

!!! example "步骤 1-2: 整理项目结构"

    **创建文件夹结构**:

    在 Project 窗口中创建以下文件夹：
    ```
    Assets/
    ├── Avatars/           (原始模型 FBX)
    ├── Garments/          (MD 制作的服装 FBX)
    ├── Materials/         (材质)
    ├── Textures/          (纹理)
    ├── Scenes/            (工作场景)
    └── Prefabs/           (完成模型 Prefab)
    ```

    **创建文件夹的方法**:
    1. 在 Project 窗口中右键
    2. 选择 **“Create”** → **“Folder”**
    3. 输入各文件夹名称

## 📁 步骤 2: 导入文件

### 导入模型文件

!!! example "步骤 2-1: 导入原始模型"

    **导入原始模型（FBX）**:
    1. 在资源管理器中选择原始模型 FBX 文件
    2. 拖放到 Unity 的 **“Assets/Avatars/”** 文件夹中
    3. 等待导入完成（约 30 秒到 1 分钟）

    **确认导入设置**:
    1. 选择导入后的 FBX 文件
    2. 在 **Inspector** 中确认导入设置：
       - **“Rig”** 标签页: Animation Type 为 **“Humanoid”**
       - **“Materials”** 标签页: Extract Materials 设置正确

!!! example "步骤 2-2: 导入服装文件"

    **导入 Marvelous Designer 制作的服装**:
    1. 选择在 MD 中导出的服装 FBX 文件
    2. 拖放到 Unity 的 **“Assets/Garments/”** 文件夹中
    3. 在导入设置中确认以下内容：
       - **Scale Factor**: 1
       - **Convert Units**: 勾选
       - **Import Materials**: 勾选

!!! warning "文件路径注意事项"
    请避免使用包含日文或空格的路径，否则可能导致错误。

### 处理纹理与材质

!!! example "步骤 2-3: 整理纹理"

    **确认纹理文件**:
    1. 确认导入时自动生成的 **“Materials”** 与 **“Textures”**
    2. 将自动生成的文件移动到合适的文件夹
    3. 删除不需要的纹理并整理结构

    **基础调整材质设置**:
    1. 选择 **“Assets/Materials/”** 中的材质文件
    2. 在 Inspector 中确认并调整以下项目：
       - **Shader**: Standard 或支持 VRChat 的 Shader
       - **Albedo**: 基础颜色设置
       - **Rendering Mode**: 通常以 Opaque（不透明）为主

## 🎭 步骤 3: 在场景中进行集成

### 准备场景

!!! example "步骤 3-1: 设置工作场景"

    **创建新场景**:
    1. **“File”** → **“New Scene”** → **“Basic (Built-in)”**
    2. **“File”** → **“Save As”**，命名为 “AvatarSetup”
    3. 保存位置: **“Assets/Scenes/”**

    **场景内设置**:
    1. 删除不需要的默认对象（保留 Main Camera）
    2. 调整 **Main Camera** 位置，让模型更容易查看
    3. 通过 **“Window”** → **“Lighting”** → **“Settings”** 调整灯光

### 放置并集成模型

!!! example "步骤 3-2: 放置模型"

    **放置原始模型**:
    1. 从 **“Assets/Avatars/”** 将模型 FBX 拖放到场景中
    2. 通过 Transform 将位置设置为原点（0, 0, 0）
    3. 确认模型显示正常

    **放置服装**:
    1. 从 **“Assets/Garments/”** 将服装 FBX 拖放到场景中
    2. 将其放置在与模型相同的位置（0, 0, 0）
    3. 确认服装与模型重叠显示

!!! example "步骤 3-3: 构建对象层级"

    **设置正确的父子关系**:
    1. 在 **Hierarchy** 中选择模型的根对象
    2. 将服装对象作为模型的子对象放置：
       - 把服装拖动到模型对象下方
    3. 层级结构示例：
    ```
    Avatar_Root
    ├── Armature (骨骼结构)
    ├── Body (原始身体网格)
    └── Tshirt (新增服装)
        ├── Mesh
        └── Materials
    ```

## ⚙️ 步骤 4: 配置 VRChat SDK3

### 配置 Avatar Descriptor

!!! example "步骤 4-1: 添加 VRChat Avatar Descriptor"

    **添加 Avatar Descriptor 组件**:
    1. 在 Hierarchy 中选择模型的根对象
    2. 在 **Inspector** 中点击 **“Add Component”**
    3. 搜索并添加 **“VRC Avatar Descriptor”**

    **输入基础设置**:
    1. 设置 **View Position**：
       - 将 View 球（绿色球）移动到模型眼睛位置
       - 一般可设为 X: 0, Y: 1.6～1.8, Z: 0
    2. 设置 **Lip Sync**：
       - 指定 **“Jaw Bone”**（通常是头部骨骼）

!!! example "步骤 4-2: 设置模型层"

    **Playable Layers 的基础设置**:
    1. **“VRChat SDK”** → **“Show Control Panel”**
    2. 在 Control Panel 中选择 **“Builder”** 标签页
    3. 基本上保持默认设置即可

    **Expression Parameters 与 Menu（可选）**:
    - 如果不需要服装切换功能，可以保持默认
    - 高级功能可以之后再学

### 集成骨骼结构与绑定骨架

!!! example "步骤 4-3: 集成服装与模型骨骼"

    **确认骨骼权重**:
    1. 选择服装对象
    2. 在 **Inspector** 中确认 **“Skinned Mesh Renderer”** 组件
    3. 确认 **Root Bone** 引用了模型的根骨骼

    **手动设置骨骼引用**（必要时）:
    1. 选择服装的 **“Skinned Mesh Renderer”**
    2. 在 **“Root Bone”** 中指定模型的 Root Bone
    3. 确认 **“Bones”** 数组设置正确

!!! info "Marvelous Designer 2025 的绑定骨架功能"
    **通过 Avatar Rigger 自动设置权重**:
    - 在 MD2025 中，可通过 **“Avatar Rigger”** 功能将身体骨骼权重自动复制到服装
    - 使用 **“EveryWear Toolkit”** 可执行自动重拓扑与绑定骨架
    - Unity 最多支持 8 个 Joint，MD 中可指定影响的 Joint 数量

    **IK Joint 映射**:
    - 支持 Daz 3D、Mixamo、Character Creator、MetaHumans
    - 可自动识别肩、肘、腕、骨盆、膝、踝等主要关节
    - 让动作更加自然流畅

!!! warning "传递权重时的注意点"
    - 腋下或胯部有时会被映射到不合适的骨骼
    - 如果模型不是标准 A-Pose，需要特别注意
    - 必要时可先用紧身版本处理，再替换成最终版本

## 🧪 步骤 5: 测试与质量确认

### 在 Scene View 中测试

!!! example "步骤 5-1: 在 Unity 内测试"

    **确认外观**:
    1. 在 **Scene View** 中从多个角度查看模型
    2. 确认服装是否正确贴合模型
    3. 检查是否存在不自然的穿插或悬空

    **使用 Animation Controller 测试动作**（可选）:
    1. **“Window”** → **“Animation”** → **“Animator”**
    2. 确认模型在基础动作下是否正常运动

### VRChat SDK Build & Test

!!! example "步骤 5-2: 使用 SDK 内置测试功能"

    **执行 Build & Test**:
    1. 打开 VRChat SDK Control Panel 的 **“Builder”** 标签页
    2. 点击 **“Build & Test”**
    3. 构建流程会开始运行

    **确认错误并处理**:
    - 如果出现错误，先确认内容
    - 常见错误：多边形数量过多、材质设置不当
    - 在 **Console Window** 中查看详细错误

!!! success "测试成功的确认"
    如果 VRChat 启动，并在本地测试世界中显示穿着服装的模型，就说明成功了。

## 🎨 步骤 6: 最终调整与优化

### 微调外观

!!! example "步骤 6-1: 调整材质与纹理"

    **调整颜色与质感**:
    1. 选择 **“Assets/Materials/”** 中的材质
    2. 在 **Inspector** 中调整以下项目：
       - **Albedo Color**: 微调基础颜色
       - **Metallic**: 金属感（通常为 0）
       - **Smoothness**: 表面平滑度
       - **Normal Map**: 凹凸感（高级设置）

    **面向 VRChat 的优化**:
    1. 删除不必要的高分辨率纹理
    2. 尽量减少材质数量
    3. 考虑使用 VRChat 推荐的 Shader

### 性能优化

!!! example "步骤 6-2: 评估 VRChat 性能"

    **确认 Performance 评估**:
    1. 在 VRChat SDK Control Panel 中选择模型
    2. 查看 **“Performance”** 信息：
       - **Triangle Count**: PC 低于 20,000，Quest 低于 7,500
       - **Material Count**: 尽量少
       - **Mesh Count**: 可以合并时尽量合并

    **执行优化**:
    - 视情况减少多边形数量
    - 调整纹理尺寸
    - 删除不必要的骨骼

## 💾 步骤 7: 制作 Prefab 并保存

### 为完成的模型创建 Prefab

!!! example "步骤 7-1: 保存为 Prefab"

    **创建 Prefab**:
    1. 在 Hierarchy 中选择整个模型
    2. 拖放到 **“Assets/Prefabs/”** 文件夹
    3. Prefab 名称建议使用 “MyAvatar_withGarments” 这类易懂名称

    **版本管理**:
    1. 为不同变体分别创建 Prefab
    2. 命名规则示例：
       - `MyAvatar_Tshirt_v1`
       - `MyAvatar_Casual_v1`
       - `MyAvatar_Formal_v1`

### 保存项目文件

!!! example "步骤 7-2: 保存 Unity 项目"

    **保存场景与项目**:
    1. **“File”** → **“Save Scene”** 保存当前工作
    2. **“File”** → **“Save Project”** 保存整个项目
    3. 建议定期备份

## ✅ 集成完成检查

!!! note "Unity 集成完成检查清单"

    **文件集成**:
    - [ ] 原始模型 FBX 已正常导入
    - [ ] 服装 FBX 已正常导入
    - [ ] 纹理与材质已正确设置
    - [ ] 文件夹结构已整理好

    **Unity 设置**:
    - [ ] 模型与服装在场景中正确显示
    - [ ] VRChat Avatar Descriptor 已设置
    - [ ] View Position 已正确设置
    - [ ] 骨骼结构已正确集成

    **质量确认**:
    - [ ] Build & Test 无错误
    - [ ] VRChat Performance 评估处于合理范围
    - [ ] 服装贴合效果良好
    - [ ] 已保存为 Prefab

## 🔧 故障排查

### 常见集成问题

??? question "“服装不显示”"
    **处理方法**:

    1. **确认材质设置**:
       - 确认材质是否显示为 “Missing”
       - 确认 Shader 设置是否正确

    2. **缩放问题**:
       - 确认模型与服装的缩放一致
       - 查看 Transform 的 Scale 值

    3. **导入设置**:
       - 重新确认 FBX 导入时的设置
       - 必要时重新导入

??? question "“服装不会跟着模型一起动”"
    **处理方法**:

    1. **确认骨骼设置**:
       - 确认 Skinned Mesh Renderer 的 Root Bone 是否设置正确
       - 确认 Bones 数组是否引用了模型骨骼结构

    2. **确认父子关系**:
       - 确认服装对象是否是模型的子对象
       - 确认层级结构是否正确

??? question "“Build & Test 出错”"
    **处理方法**:

    1. **查看 Console**:
       - 通过 Window → General → Console 查看错误详情
       - 按照错误信息处理

    2. **更新 VRChat SDK**:
       - 在 VCC 中确认 SDK 是否为最新版本
       - 必要时更新

    3. **确认模型设置**:
       - 重新检查 Avatar Descriptor 设置
       - 确认所有必填项都已设置

## 🌟 下一步

Unity 集成已经完成。

你制作的服装现在已经能在 Unity 中正确显示，VRChat SDK3 的设置也已完成。

**下一项重要步骤**:

[从 FBX 到 VRChat 的完整工作流 →](fbx-to-vrchat-complete-guide.md){ .md-button .md-button--primary }

如果还想进一步提升质量：

[服装物理与动态设置 →](../physics/fabric-properties.md){ .md-button }

## 📚 学习成果确认

### 本指南中掌握的技能

**🔄 集成工作流**
- 理解 Marvelous Designer → Unity 的联动
- 正确处理 FBX 文件
- 管理 Unity 项目结构

**⚙️ 技术技能**
- VRChat SDK3 的基础设置
- Avatar Descriptor 的配置方法
- 理解骨骼结构与 Skinned Mesh

**🎨 质量管理**
- 材质与纹理优化
- 理解 VRChat Performance 标准
- Prefab 管理与版本管理

**🧪 测试技能**
- 在 Unity Scene View 中测试的方法
- 使用 VRChat SDK Build & Test
- 错误处理与调试方法

!!! success "Unity 集成完成！"
    这是很扎实的成果。你制作的服装现在已经成为可在 VRChat 中使用的实用模型。下一步就是在 VRChat 中实际测试并上传。

## 💡 应用与进阶

### 集成技术的应用

**管理多套服装**:
- 为不同服装样式创建 Prefab
- 实现服装切换功能（高级）
- 构建分层穿搭系统

**提升质量的技巧**:
- 设置 LOD（Level of Detail）
- 使用 Animation Override
- 应用自定义 Shader

这些高级技术建议在掌握基础之后再继续挑战。
