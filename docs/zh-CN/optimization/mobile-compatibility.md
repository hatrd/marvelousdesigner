# 移动端完整兼容指南 - 与 Quest/Pico 用户建立连接

!!! info "指南概览"
    **所需时间**: 1 小时 - 2.5 小时 | **难度**: 适合中级用户 | **重要度**: 确保社区包容性

    在 VRChat 用户中，**40% 以上是 Quest/Pico 用户**。Very Poor 头像对他们来说是完全不可见的。通过本指南，制作一个能和所有用户建立连接的头像。

## 📱 移动 VR 的现状与重要性

### 2025 年移动 VR 市场的现实

!!! warning "不能忽视的移动端用户"

    **市场份额（截至 2025 年 1 月）**:
    ```
    Quest 2/3/Pro: 35%
    Pico 4/4E: 8%
    PC VR: 57%

    合计: 43% 属于移动 VR
    ```

    **地区差异**:
    ```
    日本: Quest 系约 30%（PC VR 仍是主流）
    北美: Quest 系约 50%（移动端成为主流）
    亚洲: Pico 系约 15%（以中国市场为中心）
    ```

### 移动端用户面临的问题

!!! example "Very Poor 带来的社交隔离"

    **技术限制**:
    ```
    1. Safety Settings 会隐藏 Very Poor
    2. 因处理能力不足而崩溃
    3. 电池消耗加快
    4. 加载时间大幅延长
    ```

    **社交影响**:
    ```
    - 在活动里有一半以上的人看不到你
    - 即使是好友之间也可能无法显示
    - 失去交流机会
    - 移动端用户会感到被排斥
    ```

## 🎯 面向移动端的评级标准

### VRChat Quest 标准详解

!!! info "Quest 用 Performance Rating 标准"

    **Excellent（推荐给 Quest）**:
    ```
    Polygon Count: 7,500 以下
    Texture Memory: 10MB 以下
    Bone Count: 75 以下
    PhysBone Components: 8 以下
    Dynamic Bone Colliders: 4 以下
    ```

    **Good（Quest 可接受）**:
    ```
    Polygon Count: 10,000 以下
    Texture Memory: 40MB 以下
    Bone Count: 90 以下
    PhysBone Components: 16 以下
    Dynamic Bone Colliders: 8 以下
    ```

    **Medium（Quest 极限）**:
    ```
    Polygon Count: 15,000 以下
    Texture Memory: 75MB 以下
    Bone Count: 150 以下
    PhysBone Components: 24 以下
    Dynamic Bone Colliders: 16 以下
    ```

### 实用目标设置

!!! tip "分阶段移动端适配策略"

    **Phase 1: 确保可见（最高优先级）**
    ```
    目标: 达到 Medium
    → 可向 80% 的 Quest 用户显示

    最低标准:
    - Polygon: 15,000 以下
    - Texture: 75MB 以下
    - PhysBone: 24 个以下
    ```

    **Phase 2: 舒适显示（推荐）**
    ```
    目标: 达到 Good
    → 可向 95% 的 Quest 用户流畅显示

    推荐标准:
    - Polygon: 10,000 以下
    - Texture: 40MB 以下
    - PhysBone: 16 个以下
    ```

    **Phase 3: 完整兼容（理想）**
    ```
    目标: 达到 Excellent
    → 对所有 Quest 用户都能最佳显示

    理想标准:
    - Polygon: 7,500 以下
    - Texture: 10MB 以下
    - PhysBone: 8 个以下
    ```

## 🛠️ 移动端优化的实战步骤

### Step 1: 现状分析与 Quest 标准评估

!!! example "按 Quest 标准评估现状"

    **分析模板**:
    ```
    === Quest 兼容性分析 ===
    头像名称: _______________
    分析日期: _______________

    当前状态:
    Polygon Count: _____ / 7,500 (Quest Excellent)
    Texture Memory: _____ / 10MB (Quest Excellent)
    PhysBone Count: _____ / 8 (Quest Excellent)

    Quest 显示可能性:
    □ Excellent: 100% 可显示
    □ Good: 95% 可显示
    □ Medium: 80% 可显示
    □ Poor 以下: 难以显示
    ```

### Step 2: 超轻量纹理策略

!!! example "应对 10MB 限制"

    **面向 Quest 的纹理设置**:
    ```
    脸部纹理: 512×512 DXT5 (0.25MB)
    身体纹理: 512×512 DXT5 (0.25MB)
    头发纹理: 256×256 DXT5 (0.0625MB)
    服装主纹理: 512×512 DXT1 (0.125MB)
    服装副纹理: 256×256 DXT1 (0.03125MB)

    合计示例: 约 0.7MB（余量很大）
    ```

    **纹理整合策略**:
    ```
    1. 制作 Atlas: 把多张纹理合并成一张
    2. Channel Packing: 充分利用 RGB 通道
    3. 灰度化: 对不需要颜色的区域轻量化
    4. 分辨率优先级: 脸 > 身体 > 服装 > 饰品
    ```

### Step 3: 应对 7,500 多边形限制

!!! example "极限多边形削减技巧"

    **削减优先级**:
    ```
    1. 头发内侧: 可减少 50-70%
       常见 8,000→2,400-4,000 多边形

    2. 服装重叠区域: 可减少 40-60%
       常见 5,000→2,000-3,000 多边形

    3. 简化配饰: 可减少 70-90%
       常见 2,000→200-600 多边形

    4. 身体被遮挡部分: 可减少 30-50%
       常见 3,000→1,500-2,100 多边形
    ```

    **Mantis LOD Editor 的 Quest 设置**:
    ```
    Hair (内侧): Reduction 70%
    Clothes (重叠): Reduction 60%
    Body (遮挡部分): Reduction 40%
    Face: Reduction 10% (保持质量)
    Accessories: Reduction 80%
    ```

### Step 4: PhysBone 最小化策略

!!! example "如何应对 8 个限制"

    **PhysBone 优先级**:
    ```
    必须保留（4-6 个）:
    1. 头发主体（刘海）: 1 个
    2. 头发主体（后发）: 2 个
    3. 裙子/礼服: 1-2 个

    可酌情保留（1-2 个）:
    4. 侧发: 1 个（左右合并）
    5. 配饰摆动: 1 个（只保留最重要的）

    删除对象:
    - 装饰物的细小摆动
    - 对外观影响很小的摆动
    - 重复的摆动效果
    ```

    **PhysBone 合并技巧**:
    ```
    Before: 头发 18 个（前 3、侧 6、后 9）
    After: 头发 3 个（前 1、侧合并 1、后合并 1）

    合并方法:
    1. 将 Root Transform 调整到更上层
    2. 设置 Multi Child Type: Average
    3. 调整 Chain Length，维持自然动作
    ```

## 🔧 Quest 专用优化工具

### 面向 Quest 的 Avatar Optimizer 设置

!!! example "Quest 专用优化设置"

    **Avatar Optimizer Quest Mode**:
    ```
    1. Avatar Optimizer → Settings
    2. Target Platform: Quest
    3. Quality Mode: Performance Priority
    4. Auto Optimization: Enabled
    ```

    **Quest 专用优化项目**:
    ```
    □ Aggressive Mesh Optimization
    □ Texture Compression (Quest)
    □ PhysBone Reduction
    □ Bone Cleanup (Non-Essential)
    □ Material Merging (Aggressive)
    ```

### 利用 Quest Preview 功能

!!! tip "在 Quest 环境中预览"

    **使用 Unity Quest Simulator**:
    ```
    1. VRChat SDK → Utilities → Quest Simulator
    2. Performance Mode: 设置为 Quest 2/3
    3. 实时确认性能
    4. 查看接近真实 Quest 环境的显示效果
    ```

## 📊 Quest 优化实测数据

### 成功案例 1: 普通原创头像

!!! success "达到 Quest Excellent 的案例"

    **Before（仅 PC）**:
    ```
    Overall: Very Poor
    Polygon: 45,000
    Texture: 180MB
    PhysBone: 28 个
    Quest 显示: 不可能
    ```

    **After（Quest 兼容）**:
    ```
    Overall: Excellent (Quest 标准)
    Polygon: 6,800 (减少 85%)
    Texture: 8.2MB (减少 95%)
    PhysBone: 6 个 (减少 79%)
    Quest 显示: 完整兼容
    ```

    **优化步骤**:
    ```
    1. Mantis LOD Editor: 执行 70% 削减
    2. 统一纹理为 256×256
    3. 大幅合并 PhysBone
    4. 大幅简化配饰
    作业时间: 2.5 小时
    ```

### 成功案例 2: 改造 BOOTH 购买头像

!!! success "达到 Quest Good 的案例"

    **Before（购买时）**:
    ```
    Overall: Poor
    Polygon: 22,000
    Texture: 85MB
    PhysBone: 24 个
    Quest 显示: 可能受到限制
    ```

    **After（兼顾 Quest）**:
    ```
    Overall: Good (Quest 标准)
    Polygon: 9,500 (减少 57%)
    Texture: 35MB (减少 59%)
    PhysBone: 14 个 (减少 42%)
    Quest 显示: 95% 兼容
    ```

    **兼顾外观的优化方式**:
    ```
    1. Avatar Optimizer: 非破坏式优化
    2. 只压缩纹理（维持尺寸）
    3. 调整 PhysBone 设置（尽量少删）
    4. 以保持外观质量为优先
    作业时间: 1 小时
    ```

## 📱 按 Quest/Pico 区分的适配策略

### Quest 2/3 的专用优化

!!! example "按 Quest 世代优化"

    **适配 Quest 2**:
    ```
    CPU: Snapdragon XR2 (2020)
    RAM: 6GB/8GB 限制
    推荐设置:
    - Polygon: 6,000 以下
    - Texture: 8MB 以下
    - PhysBone: 6 个以下
    ```

    **适配 Quest 3/Pro**:
    ```
    CPU: Snapdragon XR2 Gen 2 (2023)
    RAM: 8GB/12GB/24GB
    推荐设置:
    - Polygon: 8,000 以下
    - Texture: 12MB 以下
    - PhysBone: 10 个以下
    ```

### Pico 4/4E 适配

!!! info "Pico 的特别注意事项"

    **适配 Pico 4**:
    ```
    CPU: Snapdragon XR2 Gen 1
    RAM: 8GB
    VRChat 适配: 实验性支持

    推荐设置（保守）:
    - Polygon: 5,000 以下
    - Texture: 6MB 以下
    - PhysBone: 4 个以下
    ```

    **确保兼容性**:
    ```
    1. 推荐使用 Standard Shader
    2. 避免复杂 Shader 功能
    3. 以 Quest 2 标准进行优化
    ```

## ⚠️ Quest 优化注意事项

### 避免过度优化

??? warning "“太轻了，结果没魅力了”"
    **平衡方法**:

    **保持质量的要点**:
    ```
    1. 优先保住脸部质量
    2. 绝对不要破坏轮廓
    3. 保留有辨识度的装饰
    4. 重视动作自然度
    ```

    **分阶段优化**:
    ```
    Step 1: 先以 Medium 为目标做第一次优化
    Step 2: 确认外观并评估质量
    Step 3: 没问题再冲 Good
    Step 4: 最后挑战 Excellent
    ```

### Quest 特有的显示问题

??? question "“PC 上很好看，但 Quest 上怪怪的”"
    **Quest 环境中的差异**:

    **Shader 限制**:
    ```
    PC: 支持高功能 Shader
    Quest: 仅支持移动端 Shader

    对策: 使用 Standard Shader
         避免自定义 Shader
    ```

    **灯光差异**:
    ```
    PC: 高质量灯光
    Quest: 简化灯光

    对策: 活用 Baked Lighting
         用 Emission 效果补足
    ```

## 🌍 按地区与社区区分的应对方式

### 日本社区中的 Quest 现状

!!! info "日本特有的移动 VR 状况"

    **普及情况**:
    ```
    Quest 普及率: 约 30%（亚洲最高水平）
    主要用途: VRChat、游戏
    课题: 与 PC VR 文化并存
    ```

    **社区应对**:
    ```
    1. 活动: 越来越重视 Quest 兼容
    2. 创作者: Quest 适配意识提高
    3. 工具: Quest 优化工具逐渐普及
    ```

### 与海外社区联动

!!! example "参与全球社区"

    **在 Quest 为主的地区活动**:
    ```
    北美社区: 以 Quest 为前提
    欧洲社区: Quest/PC 混合
    亚洲社区: 地区差异较大
    ```

    **应对策略**:
    ```
    1. 准备一个 Quest Excellent 头像
    2. 参与英语社区
    3. 进行文化交流与技术交流
    ```

## 🔧 高级 Quest 优化

### 利用 LOD 系统

!!! tip "根据距离动态调整质量"

    **Quest LOD 设置**:
    ```
    LOD0 (近距离): 100% 质量 - 7,500 多边形
    LOD1 (中距离): 70% 质量 - 5,250 多边形
    LOD2 (远距离): 40% 质量 - 3,000 多边形
    LOD3 (极远): 20% 质量 - 1,500 多边形
    ```

    **动态质量调整效果**:
    ```
    近处用户: 保持高质量显示
    远处用户: 通过轻量化降低负载
    结果: 整体性能提升
    ```

### 制作 Quest 专用变体

!!! example "区分 PC/Quest 进行优化"

    **双版本策略**:
    ```
    Avatar_PC.prefab:
    - 保持高质量
    - 面向 PC 优化
    - 只需摆脱 Very Poor

    Avatar_Quest.prefab:
    - 面向 Quest 的专项优化
    - 目标 Excellent/Good
    - 执行大幅轻量化
    ```

    **管理与维护**:
    ```
    1. 使用同一基础模型
    2. 只变更优化设置
    3. 更新时同步维护
    4. 按社区类型灵活使用
    ```

## 📊 测量 Quest 适配效果

### 确认显示率提升

!!! example "在真实社区中测量效果"

    **测量方法**:
    ```
    1. 参加 VRChat 活动
    2. 确认 Quest/PC 用户比例
    3. 调查自己的头像显示情况
    4. 收集好友反馈
    ```

    **效果指标**:
    ```
    显示率: 可被 ___% 的 Quest 用户看到
    流畅度: 无明显帧率下降
    稳定性: 无崩溃、无报错
    满意度: 保持外观质量
    ```

## 🎯 Quest 适配成功检查清单

### 技术检查项

!!! success "确认已完整支持 Quest"

    **Quest Excellent 标准**:
    - [ ] Polygon Count: 7,500 以下
    - [ ] Texture Memory: 10MB 以下
    - [ ] Bone Count: 75 以下
    - [ ] PhysBone Components: 8 以下
    - [ ] Dynamic Bone Colliders: 4 以下

    **显示确认**:
    - [ ] Unity Quest Simulator 正常显示
    - [ ] 已完成 VRChat Quest 环境测试
    - [ ] 动作与物理演算正常
    - [ ] Shader 与纹理显示正常

    **性能确认**:
    - [ ] 帧率稳定
    - [ ] 已确认加载时间缩短
    - [ ] 电池消耗处于可接受范围
    - [ ] 没有发热问题

### 社区融入确认

!!! example "在真实社区中验证"

    **社交效果确认**:
    - [ ] Quest 好友反馈可以看到你
    - [ ] 参加活动时不再受限
    - [ ] 与移动端用户的交流增加
    - [ ] 感受到社区包容性提升

## 🌟 完成 Quest 适配后的进阶方向

### 更进一步的优化技术

!!! tip "以 Quest 适配为基础继续提升"

    **进阶学习内容**:
    1. **[面向专业用户的优化技术](../advanced/professional-techniques.md)**: 行业标准级轻量化方法
    2. **[多平台适配](../advanced/multi-platform-optimization.md)**: 对应多种 VR 设备
    3. **[最新优化工具](../tools/advanced-optimization.md)**: 活用最新技术

### 为社区做贡献

!!! example "分享 Quest 适配经验"

    **贡献方式**:
    ```
    1. 分享成功案例
    2. 讲解优化方法
    3. 支持 Quest 初学者
    4. 提出工具开发和改进建议
    ```

---

!!! success "实现与所有用户建立连接"
    完成 Quest/Pico 适配后，你就能和 VRChat 的**完整用户社区**建立连接。跨过技术限制，享受更包容、更丰富的虚拟体验。

    **你的头像会成为连接更多人、建立新友谊的桥梁。**

**相关链接**:
- [摆脱 Very Poor 实践指南](very-poor-escape.md){ .md-button }
- [性能分析方法](performance-analysis.md){ .md-button }
- [活用最新优化工具](../tools/avatar-optimizer.md){ .md-button .md-button--primary }
