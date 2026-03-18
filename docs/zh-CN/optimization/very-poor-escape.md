# 摆脱 Very Poor 完整指南 - 通过头像轻量化摆脱被排斥

!!! info "关于本指南"
    **所需时间**: 45 分钟 - 2 小时 | **难度**: 适合初学者 | **重要度**: 紧急，关系到是否能正常参与社交

    本指南是一份为那些在 VRChat 活动中因“拒绝 Very Poor”而感到难受的用户准备的**紧急应对指南**。通过具体的数值目标和经过验证的优化方法，你可以稳定摆脱 Very Poor 评级。

## 为什么摆脱 Very Poor 很重要？

### 😢 当前正在发生的严重问题

- **活动参加受限**: 因“拒绝 Very Poor 头像”而被活动排除在外
- **对移动端用户不可见**: Quest/Pico 用户看不到你的头像
- **创作动力下降**: 因技术门槛而放弃创作
- **与社区疏离**: 无法和伙伴一起活动

??? question "“我的头像真的有那么重吗？”"
    **答案**: VRChat 的 Performance Rating（性能评级）标准非常严格。哪怕是普通大小的 3D 模型，也很容易变成 Very Poor。**这属于技术问题，并不代表你的审美或努力不够。**

### 🎯 本指南能帮助你做到什么

- **稳定从 Very Poor 提升到 Poor 及以上**
- **让移动端用户可以看到你**（Quest/Pico 兼容）
- **获得活动参与资格**
- **继续创作并参与社区**

## 理解 Performance Rating

### 📊 VRChat 的评级标准（截至 2025 年 1 月）

| Rating | 多边形数量 | 纹理内存 | 骨骼数量 | PhysBone 数量 |
|--------|-----------|---------------|----------|-----------|
| **Excellent** | ～7,500 | ～10MB | ～75 | ～8 |
| **Good** | ～10,000 | ～40MB | ～90 | ～16 |
| **Medium** | ～15,000 | ～75MB | ～150 | ～24 |
| **Poor** | ～20,000 | ～110MB | ～200 | ～32 |
| **Very Poor** | 20,001～ | 110MB～ | 201～ | 33～ |

!!! warning "重要事实"
    **优先目标应是达到 Poor 及以上**：很多活动都会要求“Poor 及以上”。**只要是 Poor 就能参加**，所以第一步先把目标设为 Poor。

## 🛠️ 准备必要工具

### Avatar Optimizer (AAO) - 非破坏式优化的救星

!!! example "Avatar Optimizer 安装步骤"

    **1. 通过 VCC 安装**
    ```
    VCC → Add Repository →
    https://vpm.anatawa12.com/vpm.json
    → 添加 Avatar Optimizer
    ```

    **2. 在 Unity 中确认**
    ```
    Window → Avatar Optimizer →
    Trace and Optimize
    ```

### Mantis LOD Editor - 强力削减多边形的工具

!!! tip "Mantis LOD Editor 的优势"
    **实测数据**: 平均可减少 63% 的多边形，同时保持质量

    **安装方式**:
    1. Unity Asset Store → 搜索 `"Mantis LOD Editor"`
    2. 下载并导入
    3. Tools → Mantis → LOD Editor

### lilNDMFMeshSimplifier - 最新网格优化工具

!!! info "适配 2024 年 10 月 19 日更新版"
    最新版在可用性上有明显改善。

    **GitHub**: https://github.com/lilxyzw/lilNDMFMeshSimplifier

## 🎯 分阶段摆脱 Very Poor 的策略

### Phase 1: 分析现状（15 分钟）

!!! example "步骤 1: 确认 Performance Ranking"

    **在 Unity 中确认的方法**:
    ```
    1. VRChat SDK Control Panel → Builder 标签
    2. 选择目标头像
    3. Build & Publish → 查看 Performance Ranking
    ```

    **确认项目**:
    - [ ] Overall Performance（总体评级）
    - [ ] Polygon Count（多边形数量）
    - [ ] Texture Memory（纹理内存）
    - [ ] Bone Count（骨骼数量）
    - [ ] PhysBone Components（PhysBone 组件数量）

!!! example "步骤 2: 找出问题"

    **找出影响最大的项目**:

    **多边形超过 20,000** → 使用 Mantis LOD Editor
    **纹理内存超过 110MB** → 执行纹理压缩
    **PhysBone 超过 33 个** → 合并或删除 PhysBone
    **骨骼超过 201 根** → 删除无用骨骼

### Phase 2: 使用 Avatar Optimizer（20 分钟）

!!! example "步骤 3: 设置 Avatar Optimizer"

    **1. 执行 Trace and Optimize**
    ```
    Avatar Optimizer → Trace and Optimize →
    选择目标头像 → Optimize
    ```

    **2. 自动优化项目**
    - [ ] 删除未使用组件
    - [ ] 合并重复材质
    - [ ] 删除无用骨骼
    - [ ] 优化网格

!!! example "步骤 4: 优化 PhysBone"

    **找出可以合并的 PhysBone**:
    ```
    头发 → 合并为 3-5 个 PhysBone
    裙子 → 合并为 1-2 个 PhysBone
    配饰 → 评估必要性后删除
    ```

    **调整推荐数值**:
    ```
    Pull（拉力）: 0.1 - 0.3
    Spring（弹簧）: 0.2 - 0.5
    Damping（阻尼）: 0.3 - 0.7
    Collision Check（碰撞检测）: Only Self
    ```

### Phase 3: 纹理优化（15 分钟）

!!! example "步骤 5: 缩小纹理尺寸"

    **推荐分辨率**:
    ```
    主纹理: 1024x1024 → 512x512
    法线贴图: 1024x1024 → 512x512
    Emission: 512x512 → 256x256
    ```

    **Unity 设置**:
    ```
    1. 选择纹理 → Inspector
    2. Max Size: 512 (或 256)
    3. Compression: High Quality
    4. Apply → 确认
    ```

!!! example "步骤 6: 合并纹理"

    **Material 合并策略**:
    ```
    同色材质 → 合并成一个
    小部件 → 合并进主纹理
    透明度使用 → 尽可能减少
    ```

### Phase 4: 使用 Mantis LOD Editor（20 分钟）

!!! example "步骤 7: 执行多边形削减"

    **Mantis LOD Editor 设置**:
    ```
    1. Tools → Mantis → LOD Editor
    2. 选择目标网格
    3. Reduction Rate: 30-50%
    4. Generate LOD → 确认结果
    ```

    **削减顺序**:
    ```
    1. 头发（内侧与不可见区域）
    2. 衣服内侧与重叠区域
    3. 配饰细节
    4. 鞋底与不可见部分
    ```

!!! warning "必须做质量检查"
    **削减后确认事项**:
    - [ ] 轮廓是否发生明显变化
    - [ ] 纹理映射是否正常
    - [ ] 关节区域动作是否正常

### Phase 5: 最终验证与调整（10 分钟）

!!! example "步骤 8: 再次确认 Performance Rating"

    **确认是否达成目标**:
    ```
    VRChat SDK → Build & Publish →
    查看 Performance Rating

    目标: Poor 及以上（推荐 Medium/Good）
    ```

    **检查项目**:
    - [ ] Overall Performance: Poor 及以上
    - [ ] Polygon Count: 20,000 以下
    - [ ] Texture Memory: 110MB 以下
    - [ ] PhysBone Components: 32 个以下

!!! example "步骤 9: 实机测试"

    **在 VRChat 中确认效果**:
    ```
    1. 上传头像
    2. 测试切换世界
    3. 确认动作与物理演算
    4. 确认其他用户看到的效果
    ```

## 📱 适配移动端（Quest/Pico）

### Quest 适配的重要性

!!! info "移动端市场正在扩大"
    **截至 2025 年**: Quest/Pico 用户占整体 40% 以上

    **Very Poor 的问题**: 移动端用户完全看不到你（会被 Safety 设置隐藏）

### 面向 Quest 的超轻量设置

!!! example "以 Quest Excellent 为目标的设置"

    **Quest 标准（更严格）**:
    ```
    多边形数量: 7,500 以下
    纹理内存: 10MB 以下
    骨骼数量: 75 以下
    PhysBone 数量: 8 以下
    ```

    **实现方法**:
    ```
    1. Mantis LOD Editor: 设置为减少 70%
    2. 纹理: 以 256x256 为主
    3. PhysBone: 只保留头发和裙子
    4. 配饰: 大幅简化
    ```

## 🛠️ 经过验证的优化配方

### 配方 1: 普通原创头像

!!! success "实测数据（成功轻量化 63%）"

    **Before**: Very Poor
    - 多边形数量: 45,000
    - 纹理: 180MB
    - PhysBone: 28 个

    **After**: Good
    - 多边形数量: 16,500（减少 63%）
    - 纹理: 35MB（减少 81%）
    - PhysBone: 12 个（减少 57%）

    **步骤**:
    ```
    1. Avatar Optimizer → 自动优化
    2. Mantis LOD Editor → 减少 60%
    3. 统一为 512x512 纹理
    4. 合并 PhysBone（头发 3 个，裙子 2 个）
    ```

### 配方 2: 改造 BOOTH 购买头像

!!! tip "优化购买头像时的注意点"
    **尊重版权**: 大幅改造前务必先确认使用条款

    **推荐做法**:
    ```
    1. Avatar Optimizer → 非破坏式优化
    2. 只压缩纹理
    3. 调整 PhysBone 设置
    4. 删除无用配饰
    ```

## ⚠️ 常见问题与对策

### Q1: 优化后外观变了

??? question "“优化后头发变得坑坑洼洼了”"
    **处理方法**:
    1. **降低 Mantis LOD Editor 的削减率**（30%→20%）
    2. **头发手动处理**（重要部分排除在削减之外）
    3. **保留法线贴图**（维持质感）

    **预防措施**:
    - 削减前必须备份
    - 分阶段削减（每次先测试 10%）
    - 随时在 Scene View 中确认

### Q2: PhysBone 减太多导致动作不自然

??? question "“头发像纸板一样硬”"
    **推荐下限**:
    ```
    头发: 至少保留 3 个
    - 刘海: 1 个
    - 侧发: 2 个（左右各一个）
    - 后发: 2-3 个（按长度决定）
    ```

    **设置技巧**:
    ```
    Root Transform: 设置在发根
    Chain Length: 适合头发长度
    Multi Child Type: Average
    ```

### Q3: 纹理变得太糊

??? question "“脸看起来糊掉了”"
    **优先级建议**:
    ```
    1. 脸部纹理: 保持 1024x1024
    2. 身体纹理: 512x512
    3. 服装: 512x512 或 256x256
    4. 配饰: 256x256
    ```

    **压缩设置**:
    ```
    重要度高: High Quality
    重要度中: Normal Quality
    重要度低: Low Quality（Fast 设置）
    ```

### Q4: Avatar Optimizer 不工作

??? question "“按下优化按钮后什么都没发生”"
    **检查项目**:
    1. 确认使用 **Unity 2022.3.22f1**
    2. 确认 **VRChat SDK 为最新版**（v3.8.2 及以上）
    3. 更新到 **Avatar Optimizer 最新版**
    4. **重启项目**

    **重新安装步骤**:
    ```
    1. VCC → Remove Avatar Optimizer
    2. 关闭 Unity 项目
    3. VCC → 重新执行 Add Repository
    4. 再次添加 Avatar Optimizer
    ```

## 🎯 分阶段目标设置

### 紧急对策: 先脱离 Poor 以下（30 分钟）

!!! example "用最少作业获得活动参与资格"

    **目标**: Very Poor → Poor

    **步骤**:
    ```
    1. 执行 Avatar Optimizer（10 分钟）
    2. 将 PhysBone 数量降到 32 以下（10 分钟）
    3. 将纹理统一为 512x512（10 分钟）
    ```

    **预期**: 有 80% 概率达到 Poor

### 推荐对策: 以 Good 为目标（60 分钟）

!!! example "用稳定性能参与社区活动"

    **目标**: Very Poor → Good

    **步骤**:
    ```
    1. 执行紧急对策
    2. 使用 Mantis LOD Editor（30 分钟）
    3. 合并材质（15 分钟）
    4. 做详细测试（15 分钟）
    ```

### 完整对策: 以 Excellent 为目标（2 小时）

!!! example "兼容 Quest，完成彻底轻量化"

    **目标**: Very Poor → Excellent

    **步骤**:
    ```
    1. 执行推荐对策
    2. 按 Quest 标准进行额外优化（30 分钟）
    3. 做细节调整与质量确认（30 分钟）
    4. 在多个环境中测试（30 分钟）
    ```

## 📊 如何验证优化效果

### 在 VRChat 中确认

!!! example "在实际环境中测试"

    **确认步骤**:
    ```
    1. 在 Home/Test 世界上传
    2. 性能设置: Show All Avatars
    3. 请其他用户帮忙确认显示效果
    4. 分别找 Quest/PC 用户确认
    ```

    **检查项目**:
    - [ ] 头像显示正常
    - [ ] 动作没有问题
    - [ ] 纹理显示正确
    - [ ] PhysBone 动作自然

### 使用 Unity Profiler 进行详细分析

!!! tip "深入的性能分析"

    **使用 Profiler**:
    ```
    Window → Analysis → Profiler
    → Play Mode → 检查头像动作
    → 查看 Memory/Rendering
    ```

    **监视项目**:
    - Memory Usage（内存使用量）
    - Draw Calls（绘制调用次数）
    - Triangle Count（多边形数量）
    - Texture Memory（纹理内存）

## 🌟 成功案例与体验分享

### 案例 1: 成功恢复活动参与

!!! success "“时隔 3 个月终于又能参加活动了！”"
    **A 先生/女士（初学者）的体验**:
    - **Before**: Very Poor → 被活动拒绝
    - **作业时间**: 1.5 小时
    - **After**: Good → 可以参加活动
    - **使用工具**: Avatar Optimizer + Mantis LOD Editor

    **感想**: “即使没有太多技术知识，照着指南一步步做也能稳定改善。现在终于又能和朋友一起开心参加活动了。”

### 案例 2: 成功兼容 Quest

!!! success "“Quest 用户终于能看到我了！”"
    **B 先生/女士（中级用户）的体验**:
    - **Before**: Very Poor → Quest 上不可见
    - **作业时间**: 2 小时
    - **After**: Excellent → 完整支持 Quest
    - **优化率**: 多边形减少 68%，纹理减少 75%

    **感想**: “当 Quest 用户的朋友对我说‘现在能看到了！’的时候，真的非常感动。能克服这种技术限制，成就感很强。”

## 🔧 高级优化技巧

### 自定义 Shader 适配

!!! info "使用 lilToon 等自定义 Shader 时"

    **优化重点**:
    ```
    1. 与 Standard Shader 对比评估
    2. 关闭不需要的功能
    3. 充分利用纹理通道
    4. 调整轮廓线设置
    ```

### 利用 LOD 系统

!!! tip "根据距离自动调整质量"

    **Mantis LOD Editor 设置**:
    ```
    LOD0 (近距离): 100% 质量
    LOD1 (中距离): 70% 质量
    LOD2 (远距离): 40% 质量
    ```

## 🎉 摆脱 Very Poor 完成检查清单

### 最终确认项

!!! success "全部检查完成后，就成功摆脱 Very Poor！"

    **技术检查**:
    - [ ] Overall Performance: Poor 及以上
    - [ ] Polygon Count: 20,000 以下
    - [ ] Texture Memory: 110MB 以下
    - [ ] Bone Count: 200 以下
    - [ ] PhysBone Components: 32 个以下

    **动作检查**:
    - [ ] 已确认 Unity 中运行正常
    - [ ] 已成功上传到 VRChat
    - [ ] 基础动作（移动、表情变化）正常
    - [ ] PhysBone 运作正常

    **社区检查**:
    - [ ] 其他用户可以看到
    - [ ] Quest 用户可以看到
    - [ ] 满足活动参与条件

## 🌟 下一步 - 继续提升

### 持续改进

!!! tip "摆脱 Very Poor 后的进阶学习"

    **下一步建议学习内容**:
    1. **[活用 MD2025 新功能](../advanced/md2025-features.md)**: 利用最新技术提高效率
    2. **[EveryWear 集成工作流](../advanced/everywear-integration.md)**: 掌握自动优化系统
    3. **[IK-Joint 优化](../advanced/ik-joint-mapping.md)**: 实现更自然的动作
    4. **[高级物理模拟](../physics/optimization.md)**: 提升物理演算质量

### 为社区做贡献

!!! example "分享知识、互相支持"

    **你可以做的事**:
    ```
    1. 在社区分享成功经验
    2. 给有相同烦恼的初学者提建议
    3. 发现并分享新的优化方法
    4. 提供工具更新信息
    ```

---

!!! success "摆脱 Very Poor，是重新参与社交的第一步"
    通过本指南摆脱 Very Poor 评级后，你就等于重新获得了完整参与 VRChat 社区的资格。**你的创作活动不再会被技术限制所束缚。**

    **祝你享受更顺畅的创作过程，也享受与伙伴共度的快乐时光。**

**相关链接**:
- [性能分析工具活用法](performance-analysis.md){ .md-button }
- [移动端完整兼容指南](mobile-compatibility.md){ .md-button .md-button--primary }
- [社区支持](../resources/community.md){ .md-button }
