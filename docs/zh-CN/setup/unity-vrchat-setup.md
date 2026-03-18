# Unity・VRChat SDK 设置指南

<span class="time-estimate">预计耗时: 约 45 分钟</span> <span class="difficulty-beginner">适合初学者</span>

**本页目标**: 正确设置 Unity 和 VRChat SDK3，完成模型制作与上传前的准备工作。

!!! info "开始之前"
    - 已完成[软件确认指南](software-check.md)
    - 已安装 Unity Hub、Unity 2022.3.22f1 和 VRChat Creator Companion
    - 拥有 VRChat 账号

## 🎯 本次要达成的目标

1. ✅ 正确设置 VRChat Creator Companion
2. ✅ 使用 Unity 2022.3.22f1 创建 VRChat 项目
3. ✅ 安装 VRChat SDK3
4. ✅ 准备模型开发环境
5. ✅ 上传一个用于测试的简单模型

## 🚀 设置步骤

### 步骤 1: VRChat Creator Companion (VCC) 设置

<div class="step-container">
<div class="step-number">VCC 的初始设置</div>

**启动 VCC 并完成初始设置**:

1. 启动 **VRChat Creator Companion**
2. 按照首次启动时显示的指引继续
3. 登录 VRChat 账号

**Unity Editor 的设置**:
1. 点击 **「Settings」** 标签页
2. 确认 **「Unity Editors」** 区块
3. 确认显示了 **Unity 2022.3.22f1**

!!! tip "如果识别不到 Unity Editor"
    1. 点击 **「Add Unity Install」**
    2. 手动指定 Unity 2022.3.22f1 的安装位置
    3. 通常是 `C:\Program Files\Unity\Hub\Editor\2022.3.22f1\Editor\Unity.exe`
</div>

<div class="step-container">
<div class="step-number">创建新的 VRChat 项目</div>

**创建用于模型制作的项目**:

1. 在 VCC 主界面点击 **「Create New Project」**
2. 选择 **「Avatar」** 项目类型
3. 输入项目信息:
   - **Project Name**: `VRChat服装制作项目`
   - **Location**: 选择前面创建的 `VRChat衣装制作/UnityProjects/` 文件夹
4. 点击 **「Create Project」**

**自动执行的处理**:
- Unity Editor 会启动
- VRChat SDK3 会自动安装
- 必要的 Package 会完成设置

!!! success "项目创建完成"
    当 Unity Editor 启动并显示 VRChat 标志时，就说明项目创建完成了。
</div>

### 步骤 2: 确认并设置 Unity Editor

<div class="step-container">
<div class="step-number">Unity Editor 的初始确认</div>

**确认 Unity Editor 是否正常运行**:

**检查界面组成**:
- **Scene View** (3D 工作视图)
- **Game View** (运行时预览)
- **Hierarchy** (对象列表)
- **Project** (Asset 管理)
- **Inspector** (属性设置)

**确认 VRChat SDK3**:
1. 确认顶部菜单栏显示 **「VRChat SDK」** 菜单
2. 点击 **「VRChat SDK」** → **「Show Control Panel」**
3. 确认 VRChat SDK Control Panel 能打开

!!! warning "如果没有显示 VRChat SDK 菜单"
    1. 打开 **「Window」** → **「Package Manager」**
    2. 选择 **「In Project」** 并确认是否显示 `VRChat SDK - Avatars`
    3. 如果没有显示，请从 VCC 重新创建项目
</div>

<div class="step-container">
<div class="step-number">Unity Editor 的基础设置</div>

**调整成更便于开发的环境**:

**Layout 设置**:
1. 从右上角 **「Layout」** 下拉菜单选择 **「2 by 3」**
2. 或按自己的习惯调整

**启用 Auto Save**:
1. **「Edit」** → **「Preferences」** → **「General」**
2. 启用 **「Auto Refresh」**

**切换日文界面（可选）**:
- Unity 2022 可使用日文化 Package
- **「Window」** → **「Package Manager」** → **「Unity Registry」** → **「Localization Package」**
</div>

### 步骤 3: VRChat SDK3 的详细设置

<div class="step-container">
<div class="step-number">设置 VRChat Control Panel</div>

**打开并设置 VRChat SDK Control Panel**:

1. **「VRChat SDK」** → **「Show Control Panel」**
2. 在 **「Authentication」** 标签页中登录 VRChat 账号

**确认模型设置**:
1. 选择 **「Builder」** 标签页
2. 确认显示 **「Build & Publish for Windows」** 区块

**设置项**:
- **Publish to VRChat**: 上传到 VRChat 时使用
- **Build Only**: 仅进行测试构建
- **Test Avatar**: 用于本地测试

!!! info "关于 Trust Rank"
    想要向 VRChat 上传模型，需要拥有 **「New User」** 及以上的 Trust Rank。
</div>

### 步骤 4: 使用测试模型确认运行

<div class="step-container">
<div class="step-number">创建简单的测试模型</div>

**用基础模型测试 VRChat 集成**:

**使用默认模型**:
1. 在 Project 窗口中确认 VRChat SDK samples
2. **「VRChat SDK」** → **「Samples」** → **「Avatar Dynamics Robot Avatar」**
3. 将机器人模型拖放到场景中

**确认 VRChat Avatar Descriptor**:
1. 在 Hierarchy 中选择模型
2. 在 Inspector 中确认 VRChat Avatar Descriptor 组件
3. 确认 **View Position**（视角位置）已设置

!!! tip "如果想使用自定义模型"
    你也可以用同样的拖放方式添加自己的 FBX 文件，但建议一开始先用测试模型确认流程正常。
</div>

<div class="step-container">
<div class="step-number">使用 Build & Test 进行本地测试</div>

**在本地测试已创建的模型**:

1. 打开 VRChat SDK Control Panel 的 **「Builder」** 标签页
2. 点击 **「Build & Test」**
3. 开始构建处理

**构建完成后**:
1. VRChat 会自动启动（如果已安装）
2. 会打开用于本地测试的世界
3. 你制作的模型将可供使用

!!! success "测试成功！"
    如果能在 VRChat 中确认模型，就说明基础集成环境已经搭建完成。
</div>

### 步骤 5: 理解项目结构

<div class="step-container">
<div class="step-number">整理文件夹结构</div>

**为了高效作业，先理解项目结构**:

**推荐的文件夹结构**:
```
Assets/
├── Avatars/           (模型文件)
├── Materials/         (材质)
├── Textures/          (纹理)
├── Garments/          (来自 Marvelous Designer 的服装)
├── Prefabs/           (Prefab)
└── Scenes/            (Scene)
    └── AvatarSetup.unity
```

**创建文件夹的方法**:
1. 在 Project 窗口中右键
2. **「Create」** → **「Folder」**
3. 按照上面的名称创建文件夹

!!! tip "项目管理小技巧"
    文件一多就会难管理。建议从一开始就做好文件夹分类。
</div>

## 🔧 故障排查

### VCC 相关问题

??? question "“无法在 VCC 中创建项目”"
    **处理方法**:

    1. **权限问题**:
       - 以管理员身份运行 VCC
       - 确认杀毒软件的排除设置

    2. **路径问题**:
       - 使用不包含日文的路径
       - 确认路径没有过长

    3. **网络问题**:
       - 确认互联网连接
       - 确认防火墙设置

??? question "“无法识别 Unity Editor”"
    **处理方法**:

    1. 通过 Unity Hub 安装准确版本（2022.3.22f1）
    2. 在 VCC 的 Settings → Unity Editors 中手动添加
    3. 如果安装了多个 Unity 版本，请整理

### Unity 相关问题

??? question "“没有显示 VRChat SDK 菜单”"
    **处理方法**:

    1. **检查 Package Manager**:
       - Window → Package Manager
       - 在 In Project 中确认是否显示 VRChat SDK - Avatars

    2. **重新导入**:
       - Assets → Reimport All
       - 这会花一些时间，请等待完成

    3. **重新创建项目**:
       - 重新从 VCC 创建新项目

??? question "“构建失败”"
    **处理方法**:

    1. **检查 Console 错误**:
       - 在 Window → General → Console 中确认错误消息

    2. **常见错误与处理**:
       - Missing script: 删除损坏的组件
       - Path too long: 移到更短的路径
       - Shader error: 确认正在使用的 Shader

## ✅ 完成检查清单

全部完成后，Unity・VRChat 集成环境就准备好了：

<div class="progress-checklist">
<h4>Unity・VRChat SDK 设置完成</h4>

- [ ] VRChat Creator Companion 可以正常运行
- [ ] 已能在 Unity 2022.3.22f1 中创建 VRChat 项目
- [ ] VRChat SDK3 已正确安装
- [ ] 可以打开 VRChat SDK Control Panel
- [ ] 已能登录 VRChat 账号
- [ ] 使用测试模型的 Build & Test 已成功
- [ ] 已理解项目文件夹结构
- [ ] 已能在 VRChat 中进行本地测试
</div>

## 🌟 下一步

Unity・VRChat 集成环境已经准备好了！

接下来就开始在 Marvelous Designer 中制作服装吧:

[学习 Marvelous Designer 基础界面 →](../basics/md-interface.md){ .md-button .md-button--primary }

或者如果想直接进入实战:

[前往模型导入指南 →](../workflows/avatar-import.md){ .md-button }

## 📚 参考信息

### 对 VRChat 开发有帮助的资源

- **VRChat Creator Docs**: [https://creators.vrchat.com/](https://creators.vrchat.com/)
- **VRChat SDK Release Notes**: [https://creators.vrchat.com/releases/](https://creators.vrchat.com/releases/)
- **Unity Learn**: [https://learn.unity.com/](https://learn.unity.com/)

### 社区

- **VRChat 日语社区**: [Discord 邀请链接](../resources/community.md#discord)
- **Unity 日语论坛**: [Unity Forum Japan](https://forum.unity.com/)

!!! success "环境搭建完成！"
    辛苦了！至此，制作 VRChat 服装所需的基础环境已经全部准备就绪。下一步终于可以进入实际的服装制作了！
