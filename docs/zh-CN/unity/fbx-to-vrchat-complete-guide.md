# 从 FBX 到 VRChat 的完整工作流指南

!!! note "指南信息"
    **预计耗时**: 约 2-3 小时 | **难度**: 面向中级用户 | **重要度**: 必须（技术理解）

**本页目标**: 提供一套完整的技术工作流，帮助你将从 Marvelous Designer 导出的 FBX 文件打造成可在 VRChat 中以高质量运行的模型。

!!! success "通过本指南将掌握的内容"
    - ✅ 完整掌握 FBX 导入设置
    - ✅ 选择并设置适用于 VRChat 的优化 Shader
    - ✅ 实践高质量材质设置
    - ✅ 深入理解模型设置
    - ✅ 掌握实用的性能优化技巧
    - ✅ 提升故障排查能力

!!! info "事前准备"
    - 已完成 [Unity・VRChat SDK 设置](../setup/unity-vrchat-setup.md)
    - 已在 Marvelous Designer 中完成模型与服装制作
    - 已执行 FBX 导出
    - 理解 Unity 的基础操作

## 🎯 完整工作流概览

### 技术流程全貌

!!! info "5 个主要阶段"

    **Stage 1: 导入优化**
    - 细调 FBX 设置
    - 统一缩放与坐标系
    - 优化动画设置

    **Stage 2: 材质与 Shader 设置**
    - 选择支持 VRChat 的 Shader
    - 考虑 Quest 兼容性
    - 优化纹理

    **Stage 3: 模型设置与验证**
    - 细致设置 Humanoid 绑定骨架
    - 优化骨骼映射
    - 集成物理设置

    **Stage 4: SDK 集成与性能优化**
    - 高级配置 Avatar Descriptor
    - 优化 Performance Ranking
    - 解决验证错误

    **Stage 5: 最终质量保证**
    - 跨平台适配
    - 细致测试与性能分析
    - 建立持续改进机制

## 📁 Stage 1: 优化 FBX 导入

### 深入理解导入设置

!!! example "步骤 1-1: 优化 FBX 导入设置"

    **Model 标签页的关键设置**:

    ```
    Scale Factor: 1.0
    ├── Marvelous Designer 标准输出通常适合 1.0
    ├── 若设置为 0.01，会出现缩放 100 倍的问题
    └── 自定义值容易导致坐标系不一致

    Convert Units: ✓ 勾选
    ├── 自动转换不同单位制
    ├── 正确实现 MD(cm) → Unity(m) 的转换
    └── 关闭后容易出现模型过大/过小问题

    Import BlendShapes: ✓ 勾选
    ├── 用于表情与面部动画
    ├── 对应 MD2025 的 AI 表情功能
    └── 注意会增加文件体积

    Import Visibility: ✓ 勾选
    └── 正确处理被隐藏的部件
    ```

    **Rig 标签页的详细设置**:

    ```
    Animation Type: Humanoid
    ├── VRChat 必须设置
    ├── 使用 Generic 更适合高级用户
    └── 不推荐使用 Legacy

    Avatar Definition: Create From This Model
    ├── 为各个模型生成专属设置
    ├── Copy From Other 更适合有经验的用户
    └── 仅在自动生成有问题时才手动调整

    Optimize Game Objects: × 不勾选
    ├── 容易导致 VRChat 中骨骼引用问题
    ├── 对性能提升有限
    └── 会增加调试难度
    ```

!!! warning "常见导入失败模式"
    - **缩放设置错误**: 模型过大或过小
    - **坐标系不一致**: 出现旋转或镜像问题
    - **Material 提取失败**: 纹理无法正确应用
    - **骨骼结构损坏**: 动画无法正常运行

!!! example "步骤 1-2: 设置 Animation 标签页"

    **Import Animation 设置**:
    ```
    Import Animation: ✓ 勾选（仅在需要时）
    ├── 对 MD 制作的服装通常不需要
    ├── 只有在包含自定义动画时才需要
    └── 会影响文件大小与构建时间

    Anim. Compression: Off
    ├── 质量优先时推荐
    ├── Optimal: 注重平衡
    └── Keyframe Reduction: 轻量化优先
    ```

### 精细控制材质提取

!!! example "步骤 1-3: 优化 Materials 标签页"

    **Extract Materials 设置**:

    **指定 Location**:
    ```
    Use External Materials (Legacy): × 不使用
    ├── 属于旧方式，不推荐
    ├── 会让材质管理更复杂
    └── 新项目应避免使用

    Material Location: Assets/Materials/[ModelName]/
    ├── 按模型名分类整理
    ├── 避免多个模型之间冲突
    └── 更利于版本管理
    ```

    **命名规则设置**:
    ```
    Material Naming: By Base Texture Name
    ├── Model Name + Material Name: 适合多个模型共存
    ├── Base Texture Name: 简单直观
    └── Material Name: 继承 MD 中的名称
    ```

    **执行提取**:
    1. 点击 **Extract Materials** 按钮
    2. 确认生成的材质文件夹
    3. 确认纹理文件已自动链接
    4. 如有多余材质则删除

### 验证缩放与摆放

!!! example "步骤 1-4: 导入后的质量确认"

    **缩放验证方法**:
    ```
    期望结果:
    ├── 模型身高: 约 1.6-1.8m
    ├── 服装尺寸: 能恰当贴合模型
    └── 在 Unity Scene View 的 Grid 中确认
    ```

    **验证步骤**:
    1. 将导入的 FBX 放入 Scene View
    2. 确认 **Transform** → **Scale** 为 (1,1,1)
    3. 通过 **Bounds** 信息确认实际尺寸
    4. 如果有问题，重新检查 Import 设置

    **确认摆放与 Origin**:
    ```
    正确的摆放:
    ├── Position: (0, 0, 0)
    ├── Rotation: (0, 0, 0)
    ├── 双脚接触地面
    └── 面朝 Z 轴正方向
    ```

## 🎨 Stage 2: 进阶材质与 Shader 设置

### 理解并选择适用于 VRChat 的 Shader

!!! example "步骤 2-1: 选择 Shader 的判断标准"

    **Standard (Built-in)**:
    ```
    适用场景:
    ├── 基础布料表现
    ├── 需要 Quest 兼容性
    ├── 性能优先
    └── 面向初学者的稳妥选择

    特点:
    ├── Unity 标准方案，稳定性高
    ├── 灯光支持较好
    ├── 复杂表现有限
    └── 兼容 VRChat 全平台
    ```

    **Toon Lit (面向 VRChat/Mobile)**:
    ```
    适用场景:
    ├── 动漫风、漫画风表现
    ├── 明亮轻快的服装
    ├── 必须支持 Quest 时
    └── 重视移动端稳定性

    特点:
    ├── Toon 渲染
    ├── 轻量且适合移动端
    ├── 阴影表现较平
    └── 可定制性有限
    ```

    **lilToon (高功能 Toon Shader)**:
    ```
    适用场景:
    ├── 高质量动漫风表现
    ├── 细致的灯光控制
    ├── 描边表现
    └── 面向中高级用户

    注意事项:
    ├── 属于第三方 Shader
    ├── 需要安装与设置
    ├── 需要考虑对性能的影响
    └── Quest 支持有限
    ```

!!! example "步骤 2-2: 细化设置 Standard Shader"

    **选择 Rendering Mode**:
    ```
    Opaque: 不透明材质
    ├── 普通布料、皮革、金属
    ├── 性能最佳
    ├── 适合所有无需透明的材质
    └── 能高效使用 Z-buffer

    Cutout: 透明裁切
    ├── 蕾丝、网格、链条
    ├── 使用 Alpha Test
    ├── 完全透明/不透明的二值效果
    └── 也适用于草和头发

    Fade/Transparent: 半透明
    ├── 雪纺、薄纱、玻璃
    ├── 性能负担最高
    ├── 需要注意绘制顺序
    └── 应避免滥用
    ```

    **主要材质参数**:
    ```
    Albedo:
    ├── 基础颜色与纹理
    ├── 在 γ 色彩空间中调整
    ├── 避免使用 HDR 颜色
    └── 对比度调整很重要

    Metallic:
    ├── 0.0: 绝缘体（布料、皮革、木材）
    ├── 1.0: 金属（金、银、铁）
    ├── 0.5: 半金属通常不真实
    └── 以物理正确性为优先

    Smoothness:
    ├── 0.0: 完全粗糙表面
    ├── 1.0: 镜面反射
    ├── 布料: 0.0-0.3
    └── 皮革: 0.2-0.6
    ```

### 优化纹理与 UV 映射

!!! example "步骤 2-3: 优化纹理导入"

    **Texture Import 设置**:
    ```
    合适的 Max Size:
    ├── 主纹理: 1024x1024
    ├── 细节纹理: 512x512
    ├── 配件: 256x256
    └── Decal: 128x128

    Compression:
    ├── DXT1: 不需要 Alpha，高压缩
    ├── DXT5: 需要 Alpha，标准方案
    ├── Uncompressed: 仅在质量优先时使用
    └── ASTC: 面向移动端优化（高级）
    ```

    **VRChat 特有的限制**:
    ```
    推荐分辨率上限:
    ├── PC: 2048x2048（仅限特殊情况）
    ├── Quest: 1024x1024
    ├── 需考虑整个模型的总量
    └── 注意 VRAM 占用
    ```

!!! example "步骤 2-4: 检查并修正 UV 坐标系"

    **诊断 UV 问题**:
    1. 选择 **Mesh Renderer**
    2. 在 **Inspector** 中确认材质
    3. 在 **Scene View** 中切换到 **Shaded Wireframe**
    4. 检查 UV 接缝与拉伸

    **常见 UV 问题**:
    ```
    问题模式:
    ├── UV 坐标超出 0-1 范围
    ├── 纹理旋转或镜像
    ├── UV 接缝过于明显
    └── 分辨率不足导致质量下降
    ```

    **修正方式**:
    1. 最优先在 **Marvelous Designer 端**调整
    2. 在 **Unity 内**调整 Tiling/Offset
    3. 对 **Texture** 进行旋转或翻转
    4. 最后手段: 使用 **UV 编辑工具**

### 确保 Quest 兼容性

!!! example "步骤 2-5: 面向 Quest 的材质设置"

    **理解 Quest 限制**:
    ```
    Shader 限制:
    ├── Standard: 完全支持
    ├── Toon Lit: 推荐
    ├── Unlit: 轻量且安全
    └── 自定义 Shader: 很多都不支持

    材质限制:
    ├── 推荐最多 10 个
    ├── 透明材质尽量少
    ├── 避免复杂节点结构
    └── 注意实时灯光负载
    ```

    **Quest 优化实践**:
    ```
    优化方法:
    1. 合并材质:
       ├── 合并设置相近的材质
       ├── 生成纹理图集
       └── 减少 Draw Call

    2. 简化 Shader:
       ├── Standard → Unlit
       ├── 删除不需要的贴图
       └── 尽量少用 Alpha Test

    3. 轻量化纹理:
       ├── 统一为 512x512 以下
       ├── 最大化压缩率
       └── 减少色板规模
    ```

## ⚙️ Stage 3: 模型设置与细致验证

### 细化设置 Humanoid 绑定骨架

!!! example "步骤 3-1: 详细确认 Rig 设置"

    **Avatar Definition 详情**:
    1. 选择导入后的 FBX
    2. **Inspector** → **Rig** → 点击 **Configure**
    3. 打开 **Avatar Configuration** 界面

    **确认 Body 定义**:
    ```
    必须骨骼:
    ├── Root: 身体根部
    ├── Hips: 髋部，重要基准点
    ├── Spine: 脊柱基部
    ├── Chest: 胸部
    ├── Neck: 颈部
    ├── Head: 头部
    ├── Left/Right Shoulder: 肩部
    ├── Left/Right UpperArm: 上臂
    ├── Left/Right LowerArm: 前臂
    ├── Left/Right Hand: 手
    ├── Left/Right UpperLeg: 大腿
    ├── Left/Right LowerLeg: 小腿
    └── Left/Right Foot: 脚
    ```

    **设置可选骨骼**:
    ```
    推荐设置的骨骼:
    ├── Jaw: 用于张嘴动画
    ├── Left/Right Eye: 视线追踪
    ├── LeftToeBase/RightToeBase: 脚趾根部
    └── Upper Chest: 让上半身动作更自然

    手指骨骼设置:
    ├── Thumb(拇指): Proximal, Intermediate, Distal
    ├── Index(食指): 同上
    ├── Middle(中指): 同上
    ├── Ring(无名指): 同上
    └── Little(小指): 同上
    ```

!!! example "步骤 3-2: 优化骨骼映射"

    **验证自动映射**:
    ```
    检查要点:
    1. 各骨骼是否指向正确部位
    2. 左右是否识别正确
    3. 关节朝向是否自然
    4. 是否包含多余骨骼
    ```

    **需要手动修正时**:
    ```
    常见问题:
    ├── 左右混淆
    ├── Upper Chest 被误识别为 Spine
    ├── ToeBase 未设置
    └── Finger 骨骼顺序错误
    ```

    **修正步骤**:
    1. 点击有问题的骨骼名称
    2. 在 **Scene View** 中选择正确骨骼
    3. 确认 **Mapping** 栏从 “○” 变为 “✓”
    4. 全部确认后点击 **Apply**

### 集成物理设置（PhysBone/Dynamic Bone）

!!! example "步骤 3-3: 为服装添加物理设置"

    **设置 VRChat SDK3 PhysBone**:

    **基础设置步骤**:
    1. 选择服装对象
    2. **Add Component** → **VRC PhysBone**
    3. 在 **Root Transform** 中设置服装的根骨骼

    **关键参数设置**:
    ```
    Pull (拉力): 0.2-0.6
    ├── 0.2: 更自然地下垂
    ├── 0.4: 恢复力平衡
    └── 0.6: 恢复力较强，略显不自然

    Spring (弹性): 0.1-0.3
    ├── 0.1: 动作较柔和
    ├── 0.2: 标准服装动作
    └── 0.3: 动作更快，较硬

    Damping (阻尼): 0.1-0.4
    ├── 0.1: 摇摆持续时间长
    ├── 0.2: 阻尼适中
    └── 0.4: 很快停止
    ```

    **Collision 设置**:
    ```
    Colliders 设置:
    ├── Chest: 处理胸部碰撞
    ├── Hips: 处理腰部与裙子
    ├── UpperLeg: 处理裤子与紧身裙
    └── Arms: 处理袖子与身体碰撞

    Radius 调整:
    ├── 按体型分别调整
    ├── 设为不穿模的最小值
    └── 平衡性能与效果
    ```

!!! example "步骤 3-4: 优化 Constraint 设置"

    **Position/Rotation Constraint**:
    ```
    使用场景:
    ├── 固定配件
    ├── 联动多个部件
    ├── 特殊动作控制
    └── 固定分层服装

    设置注意点:
    ├── 约束过多会显得不自然
    ├── 会影响性能
    ├── 必须在 VRChat 中确认效果
    └── 也可能导致掉帧
    ```

### 验证并调整骨骼权重

!!! example "步骤 3-5: 确认权重质量"

    **确认 Skinned Mesh Renderer**:
    1. 选择服装网格
    2. 在 **Inspector** 中确认 **Skinned Mesh Renderer**
    3. 确认 **Root Bone** 指向模型根骨骼
    4. 确认 **Bones** 数组设置正确

    **诊断权重问题**:
    ```
    常见问题:
    ├── 权重错误地分配给不合适的骨骼
    ├── 影响骨骼数过多（超过 8 根）
    ├── 权重值异常（负值或极端值）
    └── 残留未使用骨骼
    ```

    **在 Unity 中可做的基础调整**:
    ```
    可调整内容:
    ├── 重新设置 Root Bone
    ├── 调整 Bone 数组顺序
    ├── 修改 Quality 设置
    └── 设置 Update When Offscreen

    限制:
    ├── 很难进行细致权重编辑
    ├── 在 MD 中重新调整更高效
    └── 复杂问题需要专用工具
    ```

## 🛠️ Stage 4: VRChat SDK 集成与性能优化

### Avatar Descriptor 的高级设置

!!! example "步骤 4-1: 细化设置 Avatar Descriptor"

    **精确调整 View Position**:
    ```
    设置方法:
    1. 选择模型的根对象
    2. 确认 Avatar Descriptor 组件
    3. 查看 View Position 的绿色球

    合适位置的标准:
    ├── 高度: 真实眼睛高度
    ├── 前后: 位于头部中央略前
    ├── 左右: 中央（0.0）
    └── 也要考虑坐下时的视角
    ```

    **用数值精确设置**:
    ```
    常见参考值:
    ├── 成年女性模型: Y = 1.62-1.68
    ├── 成年男性模型: Y = 1.68-1.75
    ├── 儿童模型: Y = 1.2-1.4
    └── Z = 0.05-0.1（略微向前）
    ```

!!! example "步骤 4-2: 理解并设置 Playable Layers"

    **各层的作用**:
    ```
    Base Layer:
    ├── 基础全身动画
    ├── 步行、跳舞、手势
    ├── 大多数情况下默认设置足够
    └── 自定义更适合高级用户

    Additive Layer:
    ├── 叠加动画
    ├── 表情与手指动作
    ├── 叠加到基础层之上
    └── 用于轻量附加表现

    Gesture Layer:
    ├── 手势动作
    ├── Peace、Fist、Gun 等
    ├── 与 VR 控制器联动
    └── 基础设置通常已足够

    Action Layer:
    ├── AFK、Sitting、Proxy
    ├── 按场景切换的专用动画
    ├── 自动执行的动作
    └── 通常不需要修改

    FX Layer:
    ├── 表情与服装切换
    ├── 粒子与灯光控制
    ├── 自定义程度最高
    └── 与 Expression Menu 联动
    ```

!!! example "步骤 4-3: 理解 Expression Parameters/Menu 的基础"

    **基础 Parameter 示例**:
    ```
    常用 Parameters:
    ├── ClothingToggle: 切换服装显示
    ├── ColorChange: 切换颜色
    ├── AccessoryToggle: 配件开关
    └── EmoteSelect: 表情选择

    Parameter 类型:
    ├── Bool: true/false 切换
    ├── Int: 整数值（多项选择）
    ├── Float: 浮点数（滑杆）
    └── Trigger: 一次性触发
    ```

    **理解内存限制**:
    ```
    VRChat Expression Memory:
    ├── 总计最多 256 bit
    ├── Bool: 1 bit
    ├── Int: 8 bit
    ├── Float: 8 bit
    └── 需要规划使用
    ```

### 优化 Performance Rating 的策略

!!! example "步骤 4-4: 详细理解 Performance 指标"

    **各项评估指标详情**:

    **Polygon Count（多边形数量）**:
    ```
    PC 版标准:
    ├── Excellent: 0-20,000
    ├── Good: 20,001-32,000
    ├── Medium: 32,001-50,000
    └── Poor: 50,001+

    Quest 版标准:
    ├── Excellent: 0-7,500
    ├── Good: 7,501-10,000
    ├── Medium: 10,001-15,000
    └── Poor: 15,001+

    优化方式:
    ├── 利用 LOD 按距离优化
    ├── 删除看不见的面
    ├── 必要时进行重拓扑
    └── 在 Marvelous Designer 中减少多边形
    ```

    **VRAM Usage（显存使用量）**:
    ```
    纹理内存计算:
    ├── 1024x1024 RGB: 3MB
    ├── 1024x1024 RGBA: 4MB
    ├── 512x512 RGB: 0.75MB
    └── 256x256 RGB: 0.19MB

    优化策略:
    ├── 合并为纹理图集
    ├── 逐级降低分辨率
    ├── 删除不必要的 Alpha 通道
    └── 选择合适的压缩格式
    ```

    **Material Count（材质数量）**:
    ```
    推荐标准:
    ├── Excellent: 1 个
    ├── Good: 2-4 个
    ├── Medium: 5-8 个
    └── Poor: 9 个以上

    减少技巧:
    ├── 合并设置相近的材质
    ├── 制作多材质纹理
    ├── 删除多余材质槽
    └── 统一 Shader
    ```

!!! example "步骤 4-5: 实践优化步骤"

    **分阶段优化方法**:

    **Phase 1: 基础优化**
    ```
    1. 删除多余材质:
       ├── 删除未使用的材质槽
       ├── 合并相同设置的材质
       └── 替换默认材质

    2. 调整纹理尺寸:
       ├── 逐步从 1024 降到 512
       ├── 每次确认对质量的影响
       └── 配件可进一步降到 256

    3. 删除多余组件:
       ├── 未使用的 Collider
       ├── 不需要的 Constraint
       └── 测试用对象
    ```

    **Phase 2: 高级优化**
    ```
    1. 设置 LOD (Level of Detail):
       ├── 按距离调整质量
       ├── 设置 3 个层级的 LOD
       └── 优化剔除距离

    2. 优化 Draw Call:
       ├── 利用 Static Batching
       ├── 适配 GPU Instancing
       └── 提高 Z-buffer 效率

    3. 优化动画:
       ├── 删除多余关键帧
       ├── 调整压缩设置
       └── 优化 Loop 设置
    ```

## 🔍 Stage 5: 最终质量保证与持续改进

### 系统化测试策略

!!! example "步骤 5-1: 系统化 Unity 内测试"

    **在 Scene View 中确认质量**:
    ```
    按视角检查:
    ├── 正面: 整体平衡
    ├── 侧面: 轮廓线
    ├── 背面: 容易遗漏的部分
    ├── 顶部: 头顶与肩部周围
    └── 底部: 脚底与裙子内侧

    按灯光条件检查:
    ├── 标准照明
    ├── 强光（假设明亮世界）
    ├── 暗光（假设俱乐部世界）
    └── 彩色灯光（RGB 照明环境）
    ```

    **利用 Animation Window**:
    ```
    动画测试:
    1. Window → Animation → Animation
    2. 确认基础动作:
       ├── Idle 状态
       ├── Walking animation
       ├── 手部上下动作
       └── 坐下与站起动作

    确认物理行为:
    ├── 重力效果是否自然
    ├── 风造成的动作
    ├── 惯性表现
    └── 碰撞判定是否合适
    ```

!!! example "步骤 5-2: 使用 VRChat SDK Build & Test"

    **详细的预检查**:
    ```
    Validation 检查项:
    ├── Missing Scripts: 无
    ├── Missing Components: 无
    ├── Performance Rating: Good 以上
    ├── Required Components: 全部已设置
    └── Bone Limits: 在限制范围内

    Build 前最后确认:
    ├── Scene 已保存
    ├── 删除了无关对象
    ├── 完成 Light Bake
    └── 材质错误为零
    ```

    **执行 Build & Test**:
    ```
    执行步骤:
    1. VRChat SDK Control Panel → Builder
    2. 选择 Build & Test for Windows
    3. 查看构建日志
    4. 处理错误与警告
    5. 确认 VRChat 本地启动
    ```

### 错误处理与调试技术

!!! example "步骤 5-3: 常见错误模式与解决方式"

    **Missing Scripts 错误**:
    ```
    原因与处理:
    ├── 未安装 VRChat SDK
       └── 通过 VCC 重新安装 SDK
    ├── 脚本引用断开
       └── 在 Project 视图中删除相关组件
    ├── Unity 版本不一致
       └── 改用推荐的 Unity 版本
    └── 自定义脚本有问题
       └── 删除不需要的组件
    ```

    **Performance Rating Poor**:
    ```
    分阶段改进方法:
    1. 先处理最关键项目:
       ├── Polygon Count → Mesh Decimation
       ├── Material Count → Material Merge
       ├── VRAM Usage → Texture Resize
       └── Skinned Renderers → Mesh Combine

    2. 测量效果:
       ├── 每次改动后确认 Rating
       ├── 判断可接受的质量损失
       └── 找到性能与质量平衡点
    ```

    **Bone/Rig Errors**:
    ```
    Humanoid 设置问题:
    ├── Required Bone Missing
       └── 在 Rig 设置中重新映射骨骼
    ├── Bone Limit Exceeded
       └── 删除或合并不必要的骨骼
    ├── Invalid Bone Hierarchy
       └── 重新整理骨骼层级结构
    └── IK Target Missing
       └── 修正或删除 IK 设置
    ```

!!! example "步骤 5-4: 建立持续质量管理机制"

    **版本管理系统**:
    ```
    文件命名规则:
    ├── Avatar_ClothingType_v1.0
    ├── Material_ClothingName_v1.2
    ├── Texture_PartName_1024_v1.1
    └── Scene_TestSetup_YYYYMMDD

    备份策略:
    ├── 保存作业前状态
    ├── 在重大改动前保存项目
    ├── 定期备份到外部存储
    └── 使用 Git 或 Perforce 等 VCS（高级）
    ```

    **跟踪质量指标**:
    ```
    建议记录的数据:
    ├── Polygon Count
    ├── VRAM Usage (MB)
    ├── Material Count
    ├── Build Time (seconds)
    ├── Performance Rating
    └── Upload Success Rate

    记录改进历史:
    ├── 问题内容与发生时机
    ├── 采取的处理方法
    ├── 定量测量改进效果
    └── 后续预防措施
    ```

## 🚀 按平台划分的优化策略

### 同时支持 PC 版与 Quest 版

!!! example "步骤 6-1: 跨平台设计"

    **PC 优先的思路**:
    ```
    设计理念:
    ├── 在 PC 版上实现理想质量
    ├── Quest 版逐步做减法
    ├── 两个平台统一基础功能
    └── Quest 专属功能尽量少

    实现策略:
    1. 先做 PC 优化版作为主版本
    2. 为 Quest 设置 LOD
    3. 自动切换材质与纹理
    4. 通过条件分支限制功能
    ```

    **应对 Quest 限制**:
    ```
    技术限制:
    ├── Polygon Count: 7,500 以下
    ├── 纹理: 推荐 512x512
    ├── 材质: 5 个以下
    ├── Shader: 必须支持 Mobile
    └── PhysBone: 限制较大

    对应方式:
    ├── 自动生成 LOD
    ├── 制作纹理图集
    ├── 自动替换 Shader
    ├── 简化物理模拟
    └── 删除或替换特效
    ```

!!! example "步骤 6-2: 高级优化技巧"

    **优化 Shader Variants**:
    ```
    删除不需要的 Variant:
    ├── 删除未使用关键字
    ├── 按平台排除
    ├── 按质量等级设置
    └── 大幅减少构建体积

    实现方法:
    ├── 设置 Shader Stripping
    ├── 调整 GraphicsSettings
    ├── 优化 Quality Settings
    └── 微调 Player Settings
    ```

    **Advanced Rendering Features**:
    ```
    PC 版高质量功能:
    ├── Real-time Reflection
    ├── Advanced Lighting
    ├── High-quality Shadows
    ├── Post-processing Effects
    └── Anti-aliasing

    Quest 版替代方案:
    ├── Baked Lightmaps
    ├── Simple Lighting Model
    ├── 减少 Shadow Cascades
    ├── 关闭 Post-processing
    └── 仅使用 FXAA
    ```

## 📊 性能分析与 Profiling

### 使用 Unity Profiler

!!! example "步骤 7-1: 用 Profiler 分析性能"

    **Profiler 基础设置**:
    ```
    1. Window → Analysis → Profiler
    2. 以 Development Build 运行
    3. 启用 Deep Profiling 选项
    4. 启用 GPU Profiling
    ```

    **关键测量项目**:
    ```
    CPU Performance:
    ├── Rendering: 绘制处理负载
    ├── Animation: 动画计算
    ├── Physics: 物理模拟
    └── Scripts: 自定义脚本负载

    GPU Performance:
    ├── Draw Calls: 绘制指令数量
    ├── SetPass Calls: Shader 切换次数
    ├── Triangles: 处理的多边形数量
    └── VRAM: 显存使用量
    ```

    **定位瓶颈的方法**:
    ```
    分析步骤:
    1. 先测量基准性能（默认模型）
    2. 添加服装后再次测量
    3. 通过差异计算影响程度
    4. 找出最需要优先改进的项目
    5. 测量改进后的效果
    ```

!!! example "步骤 7-2: VRChat 特有的性能注意事项"

    **VRChat 环境下的性能**:
    ```
    特殊负载因素:
    ├── 同时显示多个模型
    ├── 网络同步处理
    ├── 语音聊天处理
    ├── 世界本身的负载
    └── VR 双眼渲染

    优化优先级:
    ├── 绘制负载 > 其他所有内容
    ├── VRAM 使用量 > CPU 负载
    ├── 材质数量 > 多边形数量
    └── 透明绘制 > 不透明绘制
    ```

## ✅ 完整工作流达成检查清单

!!! note "FBX → VRChat 完整掌握检查"

    **Stage 1: 导入优化**
    - [ ] FBX 导入设置正确（Scale 1.0，启用 Convert Units）
    - [ ] Humanoid 绑定骨架识别正常
    - [ ] 材质提取完成并整理到合适的文件夹
    - [ ] Scale 与 Origin 设置准确

    **Stage 2: 材质与 Shader 设置**
    - [ ] 已按用途选择合适的 Shader
    - [ ] Standard Shader 参数设置正确
    - [ ] 纹理导入设置已优化
    - [ ] 已确认 Quest 兼容性
    - [ ] UV 映射没有问题

    **Stage 3: 模型设置与细致验证**
    - [ ] Humanoid 绑定骨架设置完整（所有必需骨骼均已设置）
    - [ ] 骨骼映射的左右与前后方向准确
    - [ ] PhysBone 设置合适（已调整物理参数）
    - [ ] Collider 设置与体型匹配
    - [ ] Skinned Mesh Renderer 运行正常

    **Stage 4: VRChat SDK 集成与性能优化**
    - [ ] Avatar Descriptor 设置完成（已精确调整 View Position）
    - [ ] Performance Rating 达到 Good 以上
    - [ ] 各项 Performance 指标均在推荐范围内
    - [ ] 已理解 Expression Parameters/Menu 的基础
    - [ ] Validation Check 中的错误已全部解决

    **Stage 5: 最终质量保证**
    - [ ] 已在 Unity 中完成全角度、全动作测试
    - [ ] Build & Test 成功（零错误、零警告）
    - [ ] 已在 VRChat 本地测试中确认动作
    - [ ] 已建立持续改进机制
    - [ ] 已执行备份与版本管理

## 🎯 已掌握技术技能总览

### 达到大师级的技术理解

!!! success "你已经达到的技术水平"

    **🔧 技术基础技能**
    - 高级使用 Unity Editor
    - 深入理解 FBX 格式与 3D 管线
    - 完整理解 Humanoid 绑定骨架系统
    - 实战运用材质与 Shader 系统

    **⚡ 性能优化技能**
    - 针对 VRChat Performance Ranking 进行策略化优化
    - 实现跨平台兼容
    - 使用 Unity Profiler 做科学化性能分析
    - 找出瓶颈并实施有效改进

    **🎨 质量管理技能**
    - 建立分阶段质量提升流程
    - 实践系统化测试方法
    - 进行错误诊断与调试
    - 运作持续改进循环

    **🌐 VRChat 平台专门能力**
    - 高级使用 VRChat SDK3
    - 细致设置 Avatar Descriptor
    - 优化 PhysBone/Dynamic Bone
    - 按社区标准实现高质量作品

## 🎯 下一步

完成这份综合指南后，你已经获得了从中级迈向高级的 VRChat 服装制作技术基础。

**下一项必做步骤**:

[VRChat 模型上传与测试 →](avatar-upload.md){ .md-button .md-button--primary }

把制作好的模型实际上传到 VRChat，并在社区中展示出来。

## 🚀 进一步学习

既然技术基础已经建立，就可以挑战更高阶的内容。

**推荐继续挑战的方向**:

### 学习高级技术
[Expression Menu 与动画系统 →](../advanced/expression-systems.md){ .md-button .md-button--primary }

[自定义 Shader 开发入门 →](../advanced/shader-development.md){ .md-button }

### 提升实战技能
[挑战复杂服装制作（连衣裙、荷叶边） →](../garments/dress.md){ .md-button }

[学习高级物理模拟设置 →](../physics/advanced-physics.md){ .md-button }

### 参与社区
[公开作品并收集反馈 →](../resources/community.md){ .md-button }

[与其他创作者进行技术交流 →](../resources/advanced-resources.md){ .md-button }

!!! tip "持续学习建议"
    达到这个技术层级后，你已经不再是“初学者”。接下来更重要的是通过实际制作积累经验，并通过社区交流持续提升。

    **重要**: 技术每天都在进步。持续关注 VRChat SDK、Unity、Marvelous Designer 的最新信息，并积极学习新功能，才是长期成功的关键。

希望你的创作能为 VRChat 社区带来新的价值与惊喜！ 🎨✨
