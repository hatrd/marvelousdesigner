# 常见问题与处理方法（FAQ）

!!! note "指南信息"
    **对象**: 全部级别 | **更新**: 持续更新 | **重要度**: 解决故障的必备资源

**本页目标**: 提供在 VRChat 服装制作中遇到的常见问题解决方法，帮助你更顺利地学习和制作。

!!! success "本页可以解决的问题"
    - ✅ 处理制作过程中出现的各种故障
    - ✅ 理解并应对错误信息
    - ✅ 诊断并解决性能问题
    - ✅ 改善工作流的提示
    - ✅ 落实预防性措施

## 🚨 按紧急程度分类的问题

### 🔴 级别 1: 紧急（制作中断）

**无法继续制作的严重问题**

### 🟡 级别 2: 重要（影响质量与效率）

**虽然可以继续制作，但需要处理**

### 🟢 级别 3: 信息（改进与优化）

**为了获得更好结果的改进建议**

---

## 🔴 紧急问题（制作中断）

### Marvelous Designer 启动与运行问题

??? question "🔴“Marvelous Designer 无法启动”"
    **症状**: 应用程序完全无法启动，或报错后崩溃

    **原因与处理方法**:

    **1. 许可证问题**:
    ```
    症状: 许可证认证错误
    处理:
    - 确认网络连接
    - 重新输入许可证密钥
    - 确认试用版期限
    - 联系 MD 官方支持
    ```

    **2. 系统要求不足**:
    ```
    症状: 运行异常卡顿、冻结
    检查项目:
    - 必须为 Windows 10/11 (64bit)
    - 建议内存 16GB 以上
    - 必须为支持 DirectX 11 的 GPU
    - 可用磁盘空间需大于 10GB
    ```

    **3. 安装损坏**:
    ```
    处理方法:
    1. 以管理员权限运行 MD
    2. 添加杀毒软件例外设置
    3. 完全卸载后重新安装
    4. 应用 Windows Update
    ```

??? question "🔴“项目文件无法打开或已损坏”"
    **症状**: `.zprj` 文件打不开，出现“文件已损坏”错误

    **紧急处理方法**:
    ```
    Step 1: 检查备份文件
    - 查找“项目名_backup.zprj”
    - 确认自动保存文件“AutoSave_XXXX.zprj”

    Step 2: 尝试恢复
    1. 将文件复制到其他位置后再打开
    2. 将扩展名改为 .zip 并尝试解压
    3. 尝试用其他版本的 MD 打开

    Step 3: 部分恢复
    - 从已导出的 FBX 文件重新构建
    - 如果单独保存过版型，则重新导入
    ```

    **预防措施**:
    ```
    - 在每个工作节点执行“Save As”
    - 定期以不同名称保存
    - 用云存储做自动备份
    - 在重要阶段额外保存导出的 FBX
    ```

### VRChat 模型与服装集成的严重错误

??? question "🔴“无法将布置点与模型对齐。仅在 A pose 或 T pose 下可正常运行”"
    **症状**: 在 Marvelous Designer 2025 中，模型布置点自动生成失败，无法创建适配套装

    **原因分析与处理方法**:

    **1. T-pose/A-pose 识别问题**:
    ```
    诊断项目:
    □ 模型是否准确处于 T-pose（双臂水平、手掌朝下）
    □ 肩膀角度是否完全水平（90 度）
    □ 手腕是否自然伸直
    □ 双脚是否大致与肩同宽

    处理方法（分阶段）:
    1. 尝试 A-pose：将手臂下放到 30-45 度
    2. 在 Blender 中调整到 T-pose 后再导出 FBX
    3. 在 MD 中使用 Avatar Editor 手动调整姿势
    ```

    **2. 模型尺寸与结构问题**:
    ```
    确认事项:
    - 模型高度低于 2 米
    - 与内置模型（Feifei）比较尺寸
    - 骨骼命名规则符合 MD 标准

    修复步骤:
    1. 导入时勾选“Automatically Add Arrangement Points”
    2. 尝试不同文件格式（FBX → OBJ → Collada）
    3. 分别测试带 Armature / 不带 Armature 的情况
    ```

    **3. 手动设置布置点（绕行方案）**:
    ```
    步骤:
    1. Avatar Editor → IK Mapping Tab
    2. “Auto Mapping”失败时，手动连接关节
    3. Display → 2D Pattern → Show Garment Fitting Suite 中确认
    4. 需要时手动添加 Arrangement Point
    ```

    **MD 2025 特有注意点**:
    ```
    - 自 2024.0.149 之后的版本起，有自定义模型布置点问题的报告
    - FBX 文件内若存在重复关节名，会导致 IK Mapping 功能异常
    - DAZ Genesis 8/9、Mixamo、Metahuman 等可自动对应
    ```

??? question "🔴“EveryWear 无法将模型的绑定骨架信息传输到服装”"
    **症状**: EveryWear 的骨骼权重传输失败，服装无法跟随模型动作

    **原因与分阶段处理方法**:

    **Level 1: 确认前提条件**:
    ```
    必要条件检查:
    □ 已正常创建适配套装
    □ 模型保留了合适的 Humanoid 绑定骨架
    □ 服装网格已正确放置到模型上
    □ MD 中的物理模拟运行稳定

    EveryWear 要求:
    - 仅支持基于 2D 版型系统的服装
    - 自定义服装必须使用 “Garment Fitting Suite”
    ```

    **Level 2: 确认绑定质量**:
    ```
    模型骨架诊断:
    1. 确认存在必需骨骼（Head、Hand、Foot）
    2. 确认骨骼层级结构（Shoulder 直接位于 Chest 下）
    3. 确认 Neck 直接位于 Chest 下
    4. 确认未分配 Upper Chest 骨骼（面向 VRChat）

    服装网格质量:
    - 拓扑与模型网格匹配
    - 没有极端变形或拉伸区域
    - 没有 Self-collision 问题
    ```

    **Level 3: 替代绑定方法**:
    ```
    手动绑定步骤:
    1. 以 OBJ 文件导出（不带绑定）
    2. 在 Blender/Maya 等软件中传输模型骨架
    3. 手动执行权重绘制
    4. 以 FBX 重新导入 Unity

    注意事项:
    - MD 的物理特性会丢失
    - 建议在 Blender 中重新设置布料物理
    ```

    **故障排查**:
    ```
    常见问题:
    - “EveryWear refuses to open” → 多数情况下重启 MD 可解决
    - 骨骼重复错误 → 检查 FBX 文件中的骨骼名称
    - 局部传输失败 → 重置对应版型的物理设置
    ```

??? question "🔴“在 Unity 中服装不跟随骨架（使用 Modular Avatar 时）”"
    **症状**: 在 Unity + Modular Avatar 中，服装网格不响应动画、不会变形

    **按原因分类的处理方法**:

    **1. Skinned Mesh Renderer 设置问题**:
    ```
    诊断检查:
    □ 存在 Skinned Mesh Renderer 组件
    □ Root Bone 正确引用模型骨骼
    □ Bones 列表已设置模型骨骼组
    □ Mesh 包含合适的 Bone Weights

    修复步骤:
    1. Inspector → Skinned Mesh Renderer
    2. Root Bone → 设置为模型的 Hips/Pelvis
    3. Bounds → 正确调整 Center and Extents
    4. Update When Offscreen → 勾选后临时测试
    ```

    **2. Modular Avatar Armature Link 问题**:
    ```
    设置确认:
    - 服装的 Armature 骨骼名称与模型完全一致
    - Armature Link → Merge Type 设置正确
    - Advanced Options → Align Rotation 的勾选状态

    常见解决方法:
    1. 取消勾选 Align Rotation（保留现有骨骼旋转）
    2. 复制模型骨骼供服装专用使用
    3. 改用 VRCFury 的 Linking Clothes 功能
    ```

    **3. Bone Weight / Mesh 优化问题**:
    ```
    Unity 优化设置:
    问题: 优化后的网格按骨骼名称而不是骨骼顺序工作
    处理: 取消勾选 Optimize Game Objects 进行验证

    手动修正权重:
    1. 在 Blender 等软件中重新执行权重绘制
    2. 手动调整问题区域的骨骼影响度
    3. 重新导出 FBX 时确认权重被保留
    ```

    **4. MD → Unity 管线优化**:
    ```
    推荐工作流:
    1. 在 MD 中导出 OBJ（不带绑定）
    2. 在 Blender 中传输模型骨架结构
    3. 执行权重绘制
    4. 为 Modular Avatar 导出 FBX
    5. 在 Unity 中设置 Armature Link

    质量保证:
    - 确认 VRChat Performance Rating
    - 用 Animation Playback 测试验证运行情况
    - 确认多个姿势下的变形
    ```

### Unity 与 VRChat SDK 严重错误

??? question "🔴“无法识别 VRChat SDK3，或菜单不显示”"
    **症状**: 在 Unity 中看不到 VRChat 菜单，无法使用 SDK 功能

    **分阶段处理方法**:
    ```
    Level 1: 基础确认
    1. 确认 Unity 版本 (2022.3.22f1)
    2. 确认通过 VCC 创建项目
    3. 在 Package Manager 中确认 SDK

    Level 2: 重新安装
    1. 在 VCC 中确认 SDK 更新
    2. 删除项目的“Packages”文件夹
    3. 重启 Unity 以重新解析包

    Level 3: 重新创建项目
    1. 用 VCC 创建新项目
    2. 仅迁移 Asset
    3. 重建 Scene
    ```

??? question "🔴“Build & Test 时发生错误”"
    **症状**: 构建时报错，VRChat 无法启动

    **按错误分类的处理方法**:
    ```
    “DLL not found” 错误:
    - 重新安装 Visual Studio Redistributable
    - 更新 .NET Framework
    - 执行 Unity Hub 修复

    “Avatar Descriptor” 错误:
    - 确认 View Position 设置
    - 确认 Animator Controller
    - 添加必需组件

    “Performance” 错误:
    - 减少 Triangle Count
    - 减少 Material 数量
    - 执行 Texture 压缩
    ```

---

## 🟡 重要问题（影响质量与效率）

### 服装适配问题

??? question "🟡“服装无法贴合模型”"
    **症状**: 尺寸不合适、形状崩坏、出现不自然的悬浮

    **诊断与处理**:
    ```
    问题诊断检查清单:
    □ 模型尺寸是否标准？
    □ 服装版型尺寸是否合适？
    □ Particle Distance 是否合适？
    □ 物理设置是否适合该服装类型？

    处理方法（优先顺序）:
    1. 调整整体缩放 (Transform→Scale)
    2. 调整各个版型尺寸
    3. 重新检查物理设置 (Bend/Stretch)
    4. 调整模型姿势
    ```

    **具体调整示例**:
    ```
    过紧时:
    - 将整体版型缩放到 110-120%
    - 将 Stretch 值调整为 0.1-0.2
    - 降低 Particle Distance 以提升质量

    过松时:
    - 将整体版型缩放到 80-90%
    - 提高 Density 以增强重力效果
    - 提高 Bend 值以加强形状保持
    ```

??? question "🟡“物理模拟不稳定或发生爆炸”"
    **症状**: 服装异常运动、飞出画面、形状崩溃

    **分阶段稳定方法**:
    ```
    紧急稳定化:
    1. 停止 Simulation（Space 键）
    2. 执行 Reset 3D Arrangement
    3. 将 Particle Distance 提高到 12-15
    4. 再逐步恢复质量设置

    根本原因处理:
    - 将极端物理值恢复为默认值
    - 临时禁用 Self Collision
    - 确认 Time Step 设置（Preferences）
    - 检查版型重叠或交叉区域
    ```

### Unity 集成问题

??? question "🟡“导入 FBX 后网格不显示”"
    **症状**: 导入成功，但看不到 3D 模型

    **检查项目与处理方法**:
    ```
    显示确认:
    1. 在 Scene View 中选择对象→按 F key
    2. 确认 Material 是否为“Missing”
    3. 确认 Mesh Renderer 组件

    导入设置确认:
    - Scale Factor: 1.0
    - Convert Units: 勾选
    - Generate Materials: 勾选
    - Import Materials: 勾选

    修复步骤:
    1. 执行 Reimport Assets
    2. 手动重新连接 Materials
    3. 必要时在 MD 侧重新导出
    ```

??? question "🟡“VRChat Performance Rating 很差”"
    **症状**: 被评为 Medium/Poor，可能导致其他用户看不到

    **分阶段优化**:
    ```
    Phase 1: 基础优化
    1. 确认并减少 Triangle Count
       - MD: 提高 Particle Distance
       - Unity: 执行 Mesh 合并
    2. 减少 Material 数量（目标 8 个以下）
    3. 压缩 Texture 并缩小尺寸

    Phase 2: 高级优化
    1. 实装 LOD 设置
    2. 删除不需要的组件
    3. 优化 Shader
    4. 优化 Animation

    评价改善目标:
    PC: Good 以上, Quest: 推荐 Excellent
    ```

---

## 🟢 信息问题（改进与优化）

### 工作流改进

??? question "🟢“想提高工作效率”"
    **改进建议**:

    **善用快捷键**:
    ```
    Marvelous Designer:
    Space: 开始/停止 Simulation
    F: 适配显示
    A: Arrow tool
    R: Rectangle tool
    C: Circle tool
    Ctrl+S: 保存
    Ctrl+Z: Undo

    Unity:
    F: 聚焦到所选对象
    W/E/R: 移动/旋转/缩放
    Ctrl+D: 复制
    ```

    **善用模板**:
    ```
    1. 将常用物理设置保存为 Preset
    2. 保存基础模型布置 Scene
    3. 创建材质设置模板
    4. 统一项目文件夹结构
    ```

??? question "🟢“想进一步提高质量”"
    **质量提升技巧**:

    **视觉质量**:
    ```
    1. 准备 Reference 图片并进行对比
    2. 在不同光照条件下测试
    3. 彻底检查各个角度
    4. 对比研究其他作品
    ```

    **技术质量**:
    ```
    1. 逐步提高 Simulation 质量
    2. 提升细节版型精度
    3. 提升材质真实感
    4. 强化动画适配能力
    ```

### 学习与技能提升

??? question "🟢“下一步应该学习什么技术？”"
    **按级别推荐的学习路径**:

    **初学者→中级者**:
    ```
    1. 扩展基础服装的变体
    2. 颜色与纹理的表现技术
    3. 简单装饰技术
    4. 多套服装的组合
    ```

    **中级者→高级者**:
    ```
    1. 制作复杂立体版型
    2. 控制高级物理设置
    3. 自定义 Unity Shader
    4. Animation Override 技术
    ```

    **高级者→专业级**:
    ```
    1. 实现商业级完成度
    2. 构建高效量产体系
    3. 掌握教学与指导能力
    4. 社区领导力
    ```

---

## 🛠️ 预防问题的最佳实践

### 制作前的准备

!!! example "预防故障的习惯"

    **项目开始时**:
    ```
    1. 明确需求（服装规格与目标质量）
    2. 收集参考资料（参考图片、资料）
    3. 确认工作环境（软件版本、设置）
    4. 制定备份计划
    ```

    **制作中的习惯**:
    ```
    1. 定期保存（建议每 30 分钟一次）
    2. 分阶段确认（每道工序完成时）
    3. 记录问题日志（附带解决方法）
    4. 记录设置值（保存成功模式）
    ```

### 应对故障的心态

!!! info "高效应对故障"

    **解决问题的步骤**:
    ```
    1. 冷静整理当前情况
    2. 准确记录错误信息
    3. 梳理最近的改动点
    4. 分阶段恢复到原始状态
    5. 逐项定位原因
    6. 记录并分享解决方法
    ```

    **善用支持资源**:
    ```
    1. 查阅官方文档
    2. 搜索社区论坛
    3. 在 Discord 等平台提问
    4. 通过截图和视频共享信息
    ```

---

## 📞 额外支持与资源

### 官方支持

**Marvelous Designer**:
- 官方支持: [support@marvelousdesigner.com](mailto:support@marvelousdesigner.com)
- 文档: [https://support.marvelousdesigner.com](https://support.marvelousdesigner.com)
- YouTube 频道: 官方教程

**Unity**:
- Unity Learn: [https://learn.unity.com](https://learn.unity.com)
- Unity Forum: [https://forum.unity.com](https://forum.unity.com)
- Unity Documentation: [https://docs.unity3d.com](https://docs.unity3d.com)

**VRChat**:
- Creator Docs: [https://creators.vrchat.com](https://creators.vrchat.com)
- VRChat Discord: 官方 Discord 服务器
- VRChat Feedback: [https://feedback.vrchat.com](https://feedback.vrchat.com)

### 社区支持

[日语社区信息 →](../resources/community.md){ .md-button .md-button--primary }

[技术资源集合 →](../resources/useful-links.md){ .md-button }

### 紧急情况联系

!!! warning "遇到严重问题时"

    **存在数据丢失风险时**:
    1. 立即停止作业
    2. 创建项目文件备份
    3. 详细记录问题情况
    4. 谨慎评估多种解决方法

    **感觉已触及技术极限时**:
    1. 不要勉强自己硬解决
    2. 向社区或专业人士咨询
    3. 将其视为学习机会
    4. 研究替代方法

---

## 🔄 关于本页更新

!!! info "持续改进"

    本 FAQ 将持续更新：

    - 新增新的问题与解决方法
    - 随软件更新修正信息
    - 反映来自社区的反馈
    - 提出更有效的解决方法

    **欢迎反馈**:
    - 报告新的问题
    - 提出改进解决方法的建议
    - 改进说明易读性的方案
    - 希望补充的内容需求

!!! success "故障也是学习的一部分"
    在 VRChat 服装制作的学习过程中，遇到问题是很自然的事。只要掌握合适的处理方法，就能更稳定、更高效地进行制作。

    遇到困难时，不要一个人闷头处理，积极利用这份指南和社区。

---

*最后更新: 2025-08-08*
*下次更新计划: 有新问题出现时 / 软件更新时*
