# 性能分析工具完整使用方法

!!! info "指南概览"
    **所需时间**: 30 分钟 - 1 小时 | **难度**: 适合初学者 | **重要度**: 摆脱 Very Poor 的基础

    想摆脱 Very Poor，首先必须准确掌握**问题到底出在哪里**。本指南将详细说明分析 VRChat 头像性能所需的工具和技巧。

## 🔍 性能分析的重要性

### 为什么必须先分析？

!!! warning "盲目优化往往适得其反"
    **常见失败示例**:
    - 纹理压得太小，导致外观明显变差
    - 削减了不重要区域的多边形，却几乎没有效果
    - PhysBone 删得太多，动作反而不自然

    **正确做法**: **基于数据进行有策略的优化**

### 分析能带来的收益

!!! success "通向高效优化的路径"
    - **找出效果最大的改进点**: 明确应该先优化哪里
    - **避免无效劳动**: 不把时间浪费在影响很小的部分
    - **保持质量**: 在维持观感的同时完成轻量化
    - **建立目标**: 用具体数值制定稳定可行的改进计划

## 🛠️ 基础分析工具

### 1. VRChat SDK Control Panel - 最基础也最重要

!!! example "在 SDK Control Panel 中做基础分析"

    **访问方式**:
    ```
    Unity 顶部菜单 → VRChat SDK →
    Show Control Panel → Builder 标签
    ```

    **分析步骤**:
    ```
    1. 选择目标头像
    2. 点击 Build & Publish
    3. 确认 Performance Ranking
    4. 查看各项详细数值
    ```

#### 详细解读 Performance Rating

!!! info "各评级项目的详细分析"

    **Overall Performance（总体评级）**:
    ```
    Excellent: 绿色 - 所有项目都很优秀
    Good: 黄绿色 - 有轻微问题
    Medium: 黄色 - 存在需要改进的项目
    Poor: 橙色 - 存在较严重问题
    Very Poor: 红色 - 需要紧急改进
    ```

    **各单项分析**:
    ```
    Polygon Count: 网格复杂度
    Bounds: 头像尺寸（通常不是问题）
    Texture Memory: 纹理占用的内存
    Bone Count: 骨骼总数
    Light Count: 灯光数量（通常为 0）
    Particle System Count: 粒子系统数量
    Dynamic Bone Components: Dynamic Bone 或 PhysBone 数量
    Dynamic Bone Colliders: 碰撞体数量
    Dynamic Bone Collider Check Count: 碰撞判定次数
    Animator Memory: Animator 占用内存
    ```

### 2. Unity Stats Window - 实时监视

!!! example "用 Unity Stats 做详细监视"

    **显示方法**:
    ```
    Unity → Window → Analysis →
    Frame Debugger 或 Stats
    → Game View 右上角的 Stats 按钮
    ```

    **重点监视项目**:
    ```
    Tris（三角面数）: 实际绘制的多边形数量
    Verts（顶点数）: 网格顶点总数
    SetPass Calls: 绘制调用次数（越少越好）
    Batches: 绘制批次数
    ```

### 3. Unity Profiler - 专业级分析工具

!!! tip "用 Profiler 进行高级分析"

    **启动方法**:
    ```
    Unity → Window → Analysis → Profiler
    → 点击 Play → 检查头像动作
    ```

    **分析项目**:
    ```
    CPU Usage: 处理器占用率
    Memory: 内存使用情况
    Rendering: 渲染性能
    Animation: 动画负载
    Physics: 物理演算负载
    ```

## 📊 实战分析工作流

### Step 1: 记录初始状态

!!! example "记录当前状态"

    **记录模板**:
    ```
    头像名称: ________________
    分析时间: ________________

    === VRChat SDK Analysis ===
    Overall Performance: ________
    Polygon Count: ________ / 20,000
    Texture Memory: _______ MB / 110 MB
    Bone Count: ________ / 200
    PhysBone Components: ________ / 32

    === Unity Stats ===
    Tris: ________
    Verts: ________
    SetPass Calls: ________
    Batches: ________
    ```

    **保存截图**: 用于对比优化前后变化

### Step 2: 给问题项目排优先级

!!! example "按收益高低安排分析顺序"

    **Priority 1: 收益最大的项目**
    ```
    1. Polygon Count 为 Very Poor
       → 优先做网格优化

    2. Texture Memory 为 Very Poor
       → 压缩纹理并缩小尺寸

    3. PhysBone Components 为 Very Poor
       → 合并或减少 PhysBone
    ```

    **Priority 2: 中等收益项目**
    ```
    4. Bone Count 为 Very Poor
       → 删除无用骨骼

    5. SetPass Calls 偏高
       → 合并材质
    ```

### Step 3: 执行详细分析

#### 多边形数量分析

!!! example "分析多边形构成"

    **按网格统计多边形数量**:
    ```
    1. 在 Hierarchy 中选择各个网格
    2. Inspector → Mesh Filter → 查看 Mesh 信息
    3. 记录各部位的多边形数量
    ```

    **常见分布示例**:
    ```
    头发: 8,000-15,000 多边形 (35-40%)
    脸部: 2,000-4,000 多边形 (10-15%)
    身体: 3,000-6,000 多边形 (15-20%)
    服装: 5,000-12,000 多边形 (25-35%)
    配饰: 1,000-3,000 多边形 (5-10%)
    ```

    **预估削减效果**:
    ```
    头发减少 50% → 可减少 4,000-7,500 多边形
    服装减少 30% → 可减少 1,500-3,600 多边形
    删除配饰 → 可减少 1,000-3,000 多边形
    ```

#### 纹理内存分析

!!! example "详细分析纹理占用"

    **调查纹理尺寸**:
    ```
    1. Project View → Filter: Texture2D
    2. 选择每一张纹理
    3. Inspector → 查看 Import Settings
    4. 确认 Max Size 与 Compression
    ```

    **计算内存占用**:
    ```
    RGBA32 (未压缩): Width × Height × 4 bytes
    DXT1 (压缩): Width × Height × 0.5 bytes
    DXT5 (压缩): Width × Height × 1 bytes

    例: 1024×1024 RGBA32 = 4MB
        1024×1024 DXT5 = 1MB
        512×512 DXT5 = 0.25MB
    ```

    **预估削减效果**:
    ```
    1024→512 缩小尺寸: 内存变为 1/4
    未压缩→DXT5: 内存变为 1/4
    合并重复纹理: 按数量减少
    ```

#### PhysBone 分析

!!! example "详细分析 PhysBone 结构"

    **清点 PhysBone**:
    ```
    1. Hierarchy → 搜索 PhysBone
    2. 查看每个 PhysBone 的设置
    3. 评估影响范围和必要性
    ```

    **分类与优先级**:
    ```
    必需（保留）:
    - 头发主体: 3-5 个
    - 裙子/礼服: 1-2 个

    可商议（可合并）:
    - 次要头发部件: 可合并
    - 配饰摆动: 可删除

    不需要（删除）:
    - 装饰物细碎摆动
    - 不可见部分上的 PhysBone
    ```

## 📋 如何利用分析结果

### 根据分析结果制定优化计划

!!! example "基于数据的优化路线图"

    **改进效果模拟**:
    ```
    当前状态: Very Poor (45,000 多边形, 180MB)

    Phase 1: 优化头发
    → 预测: 30,000 多边形 (-15,000)

    Phase 2: 压缩纹理
    → 预测: 45MB (-135MB)

    Phase 3: 合并 PhysBone
    → 预测: 15 个 PhysBone (-13)

    最终预测: Good (30,000 多边形, 45MB, 15 个)
    ```

### 进度追踪系统

!!! tip "把改进过程可视化"

    **进度记录模板**:
    ```
    日期: ________
    作业内容: ________

    改进前: Overall ______
    改进后: Overall ______

    多边形数: _____ → _____
    纹理: _____ → _____
    PhysBone: _____ → _____

    下次作业: ________
    ```

## 🔧 高级分析技巧

### 自定义分析脚本

!!! info "高效批量分析"

    **用 Unity Editor 扩展实现自动化**:
    ```csharp
    // 简单的分析信息显示示例
    [MenuItem("Tools/Avatar Analysis")]
    static void AnalyzeAvatar()
    {
        GameObject avatar = Selection.activeGameObject;

        // 收集网格信息
        MeshRenderer[] renderers = avatar.GetComponentsInChildren<MeshRenderer>();
        int totalTris = 0;

        foreach(MeshRenderer renderer in renderers)
        {
            MeshFilter filter = renderer.GetComponent<MeshFilter>();
            if(filter && filter.sharedMesh)
                totalTris += filter.sharedMesh.triangles.Length / 3;
        }

        Debug.Log($"Total Triangles: {totalTris}");
    }
    ```

### 联动外部分析工具

!!! tip "需要更详细分析时"

    **集成 VRCAvatar Optimizer**:
    ```
    1. GitHub: anatawa12/AvatarOptimizer
    2. 用 Analysis 功能生成详细报告
    3. 自动对比优化前后结果
    ```

    **与 Blender 联动分析**:
    ```
    1. 导出 FBX
    2. 在 Blender 中分析网格
    3. 查看详细多边形分布
    4. 模拟优化方案
    ```

## ⚠️ 分析时的注意点与故障排查

### 常见分析失误

??? question "“数值看起来还行，为什么还是 Very Poor？”"
    **排查隐藏问题**:

    **检查项**:
    ```
    1. Dynamic Bone Collider Check Count
       → 碰撞判定次数异常偏高

    2. Particle System Count
       → 是否藏有粒子系统

    3. Light Count
       → 头像上是否挂了灯光

    4. Bounds Size
       → 头像尺寸是否异常过大
    ```

### Unity 显示与实际结果不同

??? warning "“Unity 里没问题，但进 VRChat 还是 Very Poor”"
    **VRChat 特有的计算方式**:

    **处理方法**:
    ```
    1. 使用最新版 VRChat SDK
    2. 使用指定版本 Unity 2022.3.22f1
    3. 通过 Build & Test 在 VRChat 中测试
    4. 再次确认 Statistics Window
    ```

## 📊 把分析结果做成数据库

### 记录改进历史

!!! example "为持续改进积累数据"

    **改进数据库示例**:
    ```
    头像: Sample Avatar v1.0

    === 2025-01-15 分析结果 ===
    Overall: Very Poor
    Polygon: 45,000 (Very Poor)
    Texture: 180MB (Very Poor)
    PhysBone: 28 (Poor)

    === 改进行动 ===
    1. 用 Mantis LOD Editor 执行 50% 削减
    2. 统一为 512×512 纹理
    3. 合并头发部分的 PhysBone

    === 2025-01-16 结果 ===
    Overall: Good
    Polygon: 22,500 (Good)
    Texture: 35MB (Good)
    PhysBone: 12 (Excellent)

    改进效果: 成功轻量化 50%
    ```

## 🎯 提高分析精度的技巧

### 统一环境的重要性

!!! warning "保持一致的分析环境"

    **推荐环境设置**:
    ```
    Unity: 2022.3.22f1 (VRChat 推荐版本)
    VRChat SDK: 最新版 (v3.8.2 及以上)
    项目设置: Linear Color Space
    Quality Settings: Ultra
    ```

### 在多种条件下验证

!!! tip "在不同场景中做分析"

    **分析模式**:
    ```
    1. 静止状态分析
    2. 动画播放中分析
    3. 表情变化时分析
    4. PhysBone 动作时分析
    ```

## 🌟 下一步

### 根据分析结果继续优化

!!! success "完成分析后的具体行动"

    **推荐学习顺序**:
    1. **[摆脱 Very Poor 的实践](very-poor-escape.md)**: 根据分析结果执行优化
    2. **[移动端适配优化](mobile-compatibility.md)**: 面向 Quest/Pico 的详细分析
    3. **[面向专业用户的分析技术](../advanced/professional-techniques.md)**: 更高级的分析方法

### 提升分析能力

!!! example "持续提升技能"

    **进阶学习内容**:
    - 开发自定义分析工具
    - 编写自动化脚本
    - 在社区分享经验
    - 研究新的分析方法

---

!!! success "实现数据驱动的优化"
    通过本指南掌握的分析方法，你将能够进行**不依赖感觉的、基于数据的科学头像优化**。从准确掌握现状开始，以高效改进稳定摆脱 Very Poor。

**相关链接**:
- [摆脱 Very Poor 实践指南](very-poor-escape.md){ .md-button .md-button--primary }
- [移动端完整适配](mobile-compatibility.md){ .md-button }
- [活用最新优化工具](../tools/avatar-optimizer.md){ .md-button }
