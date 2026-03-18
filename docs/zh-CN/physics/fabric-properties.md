# 布料物理特性设置指南

!!! note "指南信息"
    **预计用时**：约 60 分钟 | **难度**：适合中级用户 | **重要度**：质量提升的关键

**本页目标**：理解 Marvelous Designer 中的布料物理特性，制作适合 VRChat、运动效果自然美观的服装。

!!! success "本指南将帮助你实现"
    - ✅ 理解自然且美观的布料动态
    - ✅ 在 VRChat 中兼顾轻量化与质量的最佳平衡
    - ✅ 掌握不同服装类型的推荐设置
    - ✅ 预防并解决性能问题

!!! info "事前准备"
    - 已通过 [T 恤制作指南](../garments/t-shirt.md) 等内容体验过基础服装制作
    - 已熟悉 Marvelous Designer 的基础操作
    - 已理解 VRChat 中的性能概念

## 🎯 物理设置的重要性

### 物理设置对 VRChat 的影响

!!! info "物理设置会如何影响 VRChat"

    **对性能的影响**：
    - 模拟精度 ↔️ 处理负载之间的权衡
    - 直接影响其他用户看到的效果
    - 影响帧率与稳定性

    **对外观的影响**：
    - 布料是否有自然的运动和重力感
    - 与模型动作的协调程度
    - 真实感与美观之间的平衡

    **对体验的影响**：
    - 操作模型时是否会产生违和感
    - 与他人互动时给人的印象
    - 在 VRChat 中的存在感

## 📐 物理特性参数基础理解

### 主要参数一览

!!! example "Marvelous Designer Physical Property 主要项目"

    **基础物理特性**：
    1. **Particle Distance** - 模拟精度（最重要）
    2. **Bend** - 抗弯折性（布料硬度）
    3. **Stretch** - 抗拉伸性（布料延展）
    4. **Shear** - 抗剪切性（布料扭转）

    **材质特性**：
    5. **Air Resistance** - 空气阻力
    6. **Density** - 密度（重量）
    7. **Thickness** - 厚度
    8. **Friction** - 摩擦系数

    **模拟质量**：
    9. **Self Collision** - 自碰撞检测
    10. **Collision Thickness** - 碰撞检测厚度

### VRChat 优化的基本方针

!!! warning "VRChat 优化的基本原则"

    **优先轻量化的项目**：
    - ✅ **Particle Distance**：8-12（精度与轻量化的平衡）
    - ✅ **Self Collision**：仅在必要范围内启用
    - ✅ **Simulation Quality**：推荐使用 Medium

    **优先保证质量的项目**：
    - ✅ **Bend/Stretch/Shear**：为获得自然动态进行调整
    - ✅ **Density**：为体现重力感进行合理设置
    - ✅ **Air Resistance**：通过微调提升动态美感

## 🧵 按服装类型划分的推荐设置

### T 恤与休闲上装

!!! example "T 恤最佳设置"

    **基础设置（Cotton Base）**：
    ```
    Fabric Preset: Cotton
    Particle Distance: 8-10
    Bend: 0.2-0.4
    Stretch: 0.1-0.2
    Shear: 0.1-0.2
    Air Resistance: 0.05-0.1
    Density: 0.2-0.3
    ```

    **调整要点**：
    - **宽松贴合**：Bend 0.2，Density 0.2
    - **紧身贴合**：Bend 0.4，Density 0.3
    - **轻薄材质感**：Thickness 0.5mm
    - **厚实材质感**：Thickness 1.0-1.5mm

### 裙子与连衣裙

!!! example "裙装最佳设置"

    **伞裙**：
    ```
    Fabric Preset: Silk (轻盈) / Cotton (普通)
    Particle Distance: 6-8 (优先保证动态美感)
    Bend: 0.1-0.3 (轻盈的动态)
    Stretch: 0.05-0.1
    Shear: 0.05-0.1
    Air Resistance: 0.1-0.2 (受风带动的动态)
    Density: 0.15-0.25
    ```

    **百褶裙**：
    ```
    Particle Distance: 8-10
    Bend: 0.3-0.5 (保持褶皱)
    Stretch: 0.2-0.3
    Shear: 0.2-0.3
    Air Resistance: 0.05-0.1
    Density: 0.2-0.3
    ```

### 泳装与紧身服装

!!! example "泳装与紧身衣最佳设置"

    **基础设置**：
    ```
    Fabric Preset: Custom (专用设置)
    Particle Distance: 10-12 (优先稳定性)
    Bend: 0.4-0.6 (贴合感)
    Stretch: 0.3-0.5 (弹性)
    Shear: 0.3-0.5
    Air Resistance: 0.01-0.03 (最小)
    Density: 0.3-0.4 (贴身感)
    ```

    **特殊调整**：
    - **Self Collision**：禁用（相比防穿模，更优先轻量化）
    - **Collision Thickness**：最小值
    - **Friction**：0.2-0.4（与皮肤的摩擦）

## ⚙️ 实践性的调整工作流

### 步骤 1：建立基线设置

!!! example "开始调整时的基本步骤"

    **1. 选择预设**：
    1. 选择与服装类型接近的 **Fabric Preset**
    2. **Cotton**（通用）、**Silk**（轻盈）、**Denim**（偏硬）
    3. 应用预设后，再开始单独微调

    **2. 确定 Particle Distance**：
    ```
    高质量 (6-8): 礼服、重点展示服装
    标准 (8-10): 普通休闲服装
    轻量化 (10-12): 多层服装叠穿时
    ```

    **3. 进行基础模拟测试**：
    - 让衣服穿到模型上，确认基础动作
    - 通过行走、手部动作、坐下动作进行检查

### 步骤 2：细节微调

!!! example "优化外观与动态"

    **Bend（硬度）调整**：
    ```
    0.1-0.2: 轻盈，像随风飘动一样
    0.2-0.4: 自然的布料动态（推荐范围）
    0.4-0.6: 略硬，更重视形状保持
    0.6+: 硬质布料，用于特殊服装
    ```

    **Density（重量）调整**：
    ```
    0.1-0.2: 轻质布料（雪纺、丝绸类）
    0.2-0.3: 标准布料（推荐）
    0.3-0.4: 略重的布料（牛仔布、厚棉布）
    0.4+: 重布料（大衣、特殊服装）
    ```

    **Air Resistance（空气阻力）调整**：
    ```
    0.01-0.05: 最小（泳装、紧身服装）
    0.05-0.1: 标准（普通服装）
    0.1-0.2: 略大（蓬松轻柔的动态）
    0.2+: 较大（礼服、特殊效果）
    ```

### 步骤 3：面向 VRChat 的优化

!!! example "性能优化实战"

    **Self Collision 的优化**：
    1. **基本方针**：能禁用就尽量禁用
    2. **需要启用的情况**：
       - 仅长裙、礼服的重叠区域
       - 袖子与身体的重叠区域（按需）
    3. **Collision Thickness**：最小值（0.5mm-1mm）

    **Simulation Quality 的调整**：
    ```
    Low: 用于动作确认和测试
    Medium: VRChat 推荐设置
    High: 仅用于最终微调和截图
    ```

    **优化确认项目**：
    - 检查对 Unity 中 FPS 的影响
    - 确认 VRChat SDK Performance Rating
    - 在 Build & Test 中检查实际表现

## 🎨 实用调整技巧

### 按问题分类的调整方法

!!! example "通过物理设置解决常见问题"

    **“布料太硬，不自然”**：
    ```
    降低 Bend: 0.5 → 0.2-0.3
    降低 Shear: 0.5 → 0.1-0.2
    提高 Air Resistance: 0.05 → 0.1
    ```

    **“布料太轻，像飘起来一样”**：
    ```
    提高 Density: 0.2 → 0.3-0.4
    降低 Air Resistance: 0.1 → 0.05
    将 Bend 设为适中: 0.2-0.3
    ```

    **“动作太激烈，晃动过头”**：
    ```
    提高 Particle Distance: 6 → 8-10
    提高 Bend: 0.2 → 0.3-0.4
    启用并调整 Damping
    ```

    **“穿模很多”**：
    ```
    调整 Collision Thickness: 1mm → 2-3mm
    局部启用 Self Collision
    降低 Particle Distance（提升质量）
    ```

### 按材质感区分的表现方法

!!! example "表现真实材质感的方法"

    **丝绸、缎面类**：
    ```
    Bend: 0.1-0.2 (柔顺)
    Density: 0.15-0.2 (轻盈)
    Air Resistance: 0.1-0.15 (像被风带动一样)
    Friction: 0.1-0.2 (顺滑)
    ```

    **牛仔布、厚棉布类**：
    ```
    Bend: 0.4-0.6 (偏硬)
    Density: 0.3-0.4 (偏重)
    Air Resistance: 0.05 (受风影响小)
    Friction: 0.3-0.4 (粗糙质感)
    ```

    **皮革类**：
    ```
    Bend: 0.6-0.8 (硬)
    Stretch: 0.4-0.6 (不易拉伸)
    Density: 0.4-0.5 (重)
    Air Resistance: 0.01-0.03 (最小)
    ```

## 📊 设置管理与版本管理

### 保存与复用设置

!!! example "高效管理设置"

    **创建预设**：
    1. 完成满意的设置后保存为预设
    2. **「File」** → **「Export」** → **「Physical Property」**
    3. 可按用途命名文件，例如：「VRChat_Tshirt_v1.phy」

    **预设的用法**：
    - 按服装类型创建预设
    - 在不同项目之间共享设置
    - 在团队协作中统一设置

    **推荐的设置记录格式**：
    ```
    服装名称: 休闲 T 恤
    最后更新: 2025-08-08
    Particle Distance: 8
    Bend: 0.3, Stretch: 0.15, Shear: 0.15
    Density: 0.25, Air Resistance: 0.08
    VRChat Performance: Good
    备注: 优先轻量化，Self Collision 已禁用
    ```

## ✅ 物理设置检查清单

!!! note "VRChat 优化物理设置完成检查"

    **基础设置**：
    - [ ] 已从合适的 Fabric Preset 开始
    - [ ] Particle Distance 位于 8-12 范围内
    - [ ] Bend/Stretch/Shear 处于自然范围
    - [ ] 已调好 Density 与 Air Resistance 的平衡

    **优化设置**：
    - [ ] Self Collision 已控制在最低必要范围
    - [ ] Collision Thickness 设置合适
    - [ ] Simulation Quality 为 Medium 或更低
    - [ ] 已禁用不必要的高负载设置

    **质量确认**：
    - [ ] 模型基础动作下动态自然
    - [ ] 坐下、抬手等动作无问题
    - [ ] 与其他模型的干涉降到最低
    - [ ] VRChat Build & Test 中无错误

    **性能**：
    - [ ] 对 Unity Scene View 中 FPS 的影响最小
    - [ ] VRChat SDK Performance Rating 达到 Good 或更高
    - [ ] 多件服装叠穿时也能稳定运行
    - [ ] 已记录并保存设置内容

## 🔧 故障排查

### 物理设置相关问题的解决方法

??? question "“模拟不稳定，或者会炸开”"
    **处理方法**：

    1. **提高 Particle Distance**：6 → 10-12
    2. **调整 Time Step**：Edit → Preferences → Simulation
    3. **重置极端数值**：把所有参数恢复到标准值
    4. **禁用 Self Collision**：先临时全部禁用再确认

??? question "“在 VRChat 里性能很差”"
    **处理方法**：

    1. **增大 Particle Distance**：至少设为 8 以上
    2. **最小化 Self Collision**：只在确实必要的区域启用
    3. **降低 Simulation Quality**：High → Medium → Low
    4. **简化复杂形状**：合并不必要的版型

??? question "“布料动态和预期不一样”"
    **处理方法**：

    1. **逐步调整**：每次只改一个参数并确认结果
    2. **观察参考**：参考真实布料或其他作品
    3. **重新尝试预设**：从不同的 Fabric Preset 重新开始
    4. **调整 Air Resistance**：它会明显影响动态氛围

## 🌟 下一步

你已经掌握了物理特性设置。

接下来可以学习更细致的模拟设置和优化技巧：

[性能优化指南 →](optimization.md){ .md-button .md-button--primary }

[性能优化指南 →](optimization.md){ .md-button }

或者把学到的知识用于更高级的服装制作：

[礼服制作指南 →](../garments/dress.md){ .md-button }

## 📚 深入理解的补充内容

### 物理模拟背后的原理

**布料的物理特性**：
- **张力**：布料抵抗拉扯的能力
- **剪切**：布料抵抗扭转的能力
- **弯曲**：布料抵抗折弯的能力
- **质量**：影响重力和惯性的物理量

**模拟中的近似关系**：
- Particle Distance = 分辨率（越细越准确，越细负载越高）
- Time Step = 时间步长（越细越稳定，越细负载越高）
- Iteration = 计算次数（越多越准确，越多负载越高）

### VRChat 的技术限制

**网络同步**：
- 物理运算结果由各客户端独立计算
- 精度过高会导致同步偏差
- 稳定性与可复现性比极致质量更重要

**性能限制**：
- 需要考虑其他用户电脑性能的承受能力
- 也要兼顾移动端与 Quest 适配
- 实用的“足够好”往往比追求“完美”更重要

!!! success "你已完成物理特性设置进阶掌握！"
    恭喜。你已经掌握了为 VRChat 制作优美布料动态并兼顾优化的关键方法。这些知识是所有服装制作都能复用的重要基础。

    请在实际制作中多尝试不同设置，逐步找到最适合你作品的“最佳解”。
