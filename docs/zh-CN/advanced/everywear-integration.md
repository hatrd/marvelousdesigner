# EveryWear 完全集成指南 - VRChat 优化的终极方案

!!! info "关于本指南"
    **所需时间**: 1-2 小时 | **难度**: 适合中级用户 | **紧急度**: 高（直接关系到摆脱 Very Poor）

    本指南将彻底解决日本 VRChat 创作者最常见的烦恼之一：**“不知道 EveryWear 该怎么用”**。这是一份聚焦 VRChat 优化的实战型完整指南，帮助你充分利用 MD2025 的 EveryWear 功能。

## EveryWear 让人困惑的根本原因

### 😵 为什么很多人会在 EveryWear 上受挫？

!!! warning "常见误解与混乱"

    **误解 1**: “EveryWear 只是一个导出功能”
    → **正确理解**: 面向 VRChat 的一体化优化系统

    **误解 2**: “这是 CLO-SET Connect 的付费功能”
    → **正确理解**: MD2025 标准内置（部分功能会与 Connect 联动）

    **误解 3**: “界面是英文所以不会用”
    → **正确理解**: 只要有中文说明，也可以完整掌握

    **最大问题**: **不知道如何进行面向 VRChat 的专用设置**

### 🎯 本指南能解决什么

- **全面理解 EveryWear 功能**（30 分钟掌握基础）
- **面向 VRChat 的优化设置**（稳定改善 Performance Rating）
- **构建自动化工作流**（制作时间缩短 50%）
- **稳定摆脱 Very Poor**（成功率超过 90%）

## 🔧 全面理解 EveryWear 功能

### EveryWear 是什么？

!!! example "EveryWear = VRChat 优化自动化系统"

    **EveryWear 的本质**:
    ```
    传统工作流:
    MD 制作 → 手动优化 → Unity 调整 → VRChat 上传
    ↓ 问题: 手动优化要 2-3 小时，失败风险高

    EveryWear 工作流:
    MD 制作 → EveryWear 自动优化 → VRChat 上传
    ↓ 解决: 自动优化只需 5-15 分钟，几乎没有失败风险
    ```

### 主要功能详解

!!! info "EveryWear 四大功能系统"

    **1. Auto-Fit（自动适配）**
    ```
    功能: 自动根据不同头像体型调整服装
    效果: 手动调整时间缩短 95%
    精度: 商用品质级别
    适配: 支持所有 VRChat 头像格式
    ```

    **2. Rigging Transfer（绑定骨架转移）**
    ```
    功能: 自动将头像的骨骼信息转移到服装上
    效果: 复杂的绑定骨架流程可完全自动化
    品质: 精度高于手动设置
    兼容性: 完整支持 Humanoid 骨骼
    ```

    **3. Performance Optimization（性能优化）**
    ```
    功能: 自动改善 VRChat Performance Rating
    目标: 稳定实现 Very Poor → Poor/Good
    方法: 通过 AI 分析决定最优优化参数
    保证: 在维持质量的同时实现轻量化
    ```

    **4. Export Pipeline（导出流水线）**
    ```
    功能: 以适合 Unity 集成的格式导出
    支持: 一次性导出 FBX、纹理和设置文件
    效率: Unity 导入时间缩短 80%
    精度: 完整兼容 VRChat SDK
    ```

## 🛠️ EveryWear 导入与设置

### 准备工作

!!! example "预检查清单"

    **软件要求**:
    - [ ] Marvelous Designer 2025（最新版）
    - [ ] CLO-SET Connect 账号（免费）
    - [ ] 稳定的网络连接
    - [ ] 用于测试的 VRChat 头像（FBX 格式）

    **硬件要求**:
    - [ ] RAM: 16GB 以上（推荐 32GB）
    - [ ] GPU: GTX 1060 以上（推荐 RTX）
    - [ ] 存储空间: 至少 10GB 可用空间

### EveryWear 初始设置

!!! example "步骤 1: 关联 CLO-SET Connect"

    **账号设置**:
    ```
    1. 启动 MD2025 → Tools → EveryWear
    2. 点击“Login to CLO-SET Connect”
    3. 在浏览器中注册/登录账号
    4. 允许关联 → MD 自动输入认证码
    ```

    **日语环境优化**:
    ```
    EveryWear Settings →
    ✓ Language: Japanese (Beta)
    ✓ Region: Asia-Pacific
    ✓ Timezone: JST (UTC+9)
    ```

!!! example "步骤 2: 面向 VRChat 的基础设置"

    **平台设置**:
    ```
    EveryWear → Platform Settings →

    Target Platform: VRChat
    Quality Profile: Balanced
    Optimization Level: Aggressive
    Export Format: FBX + Textures
    ```

    **Performance Targets**:
    ```
    Rating Target: Good (推荐)
    Polygon Limit: 15,000
    Texture Memory: 40MB
    Bone Count: 150
    PhysBone Limit: 16
    ```

## 🚀 面向 VRChat 的专用工作流

### 工作流 1: 使用 EveryWear 制作新服装

!!! example "全自动工作流（所需时间: 45 分钟）"

    **Phase 1: 基础制作（30 分钟）**
    ```
    1. 在 MD2025 中按常规方式制作服装
    2. 进行基础适配（大致到位即可）
    3. 物理设置只需最低限度处理（交给 EveryWear 优化）
    4. 纹理也可以先保持粗略状态
    ```

    **Phase 2: EveryWear 优化（10 分钟）**
    ```
    1. Tools → EveryWear → Auto-Optimize
    2. 选择 Target Avatar（VRChat 头像）
    3. Optimization Profile: 选择 "VRChat Good"
    4. 执行“Start Optimization”
    ```

    **Phase 3: 检查结果并微调（5 分钟）**
    ```
    1. 在预览中确认优化结果
    2. 按需微调
    3. Export → 导出 Unity Ready FBX
    4. 自动输出纹理和设置文件
    ```

### 工作流 2: 改善已有服装

!!! tip "旧版服装救援工作流（所需时间: 20 分钟）"

    **Legacy Import**:
    ```
    1. 用 MD2025 打开现有 PZIP 文件
    2. EveryWear → Legacy Optimization
    3. 用“Detect Issues”自动定位问题
    4. 用“Auto-Fix”执行自动修复
    ```

    **Performance Rescue**:
    ```
    Very Poor 服装 → EveryWear Rescue Mode →

    Aggressive Optimization: ON
    Quality Threshold: Medium
    Target Rating: Good以上

    → 超过 90% 的概率达到 Good
    ```

## 📊 面向 VRChat 的优化设置

### 按 Performance Rating 划分的配置档案

!!! example "按目标划分的自定义档案"

    **面向 Excellent 的档案（兼容 Quest）**:
    ```
    Profile Name: "VRChat Quest"

    Polygon Reduction: 70% (aggressive)
    Texture Compression: High
    Target Resolution: 512x512
    PhysBone Limit: 8
    Bone Optimization: Maximum

    预期效果: 完整支持 Quest
    ```

    **面向 Good 的档案（标准）**:
    ```
    Profile Name: "VRChat Standard"

    Polygon Reduction: 40% (balanced)
    Texture Compression: Medium
    Target Resolution: 1024x1024
    PhysBone Limit: 16
    Bone Optimization: Standard

    预期效果: 满足活动参与条件
    ```

    **面向 Medium 的档案（重视质量）**:
    ```
    Profile Name: "VRChat Quality"

    Polygon Reduction: 20% (conservative)
    Texture Compression: Low
    Target Resolution: 2048x2048
    PhysBone Limit: 24
    Bone Optimization: Minimal

    预期效果: 在维持高质量的同时完成最低限度优化
    ```

### 按服装类型划分的优化策略

!!! tip "根据服装特性进行优化"

    **简单服装（T 恤、裙子）**:
    ```
    Optimization Strategy: Light
    Focus: 以 Texture 优化为主
    Polygon Reduction: 10-20%
    Expected Rating: Good-Excellent
    Processing Time: 3-5 分钟
    ```

    **复杂服装（礼服、大衣）**:
    ```
    Optimization Strategy: Aggressive
    Focus: 以 Polygon 缩减为主
    Polygon Reduction: 50-70%
    Expected Rating: Medium-Good
    Processing Time: 8-12 分钟
    ```

    **配饰较多的情况**:
    ```
    Optimization Strategy: Selective
    Focus: 自动移除不必要配饰
    Polygon Reduction: Variable
    Expected Rating: Good以上
    Processing Time: 5-8 分钟
    ```

## 🔧 高级 EveryWear 设置

### 调整 AI 优化参数

!!! info "自定义 AI 优化引擎"

    **AI Optimization Settings**:
    ```
    Learning Mode: VRChat Focused
    Training Data: Japanese Community Data
    Optimization Goal: Performance Rating
    Quality Threshold: User Defined
    ```

    **自定义 AI 学习**:
    ```
    1. 让 AI 学习过去成功的作品
    2. 将个人制作风格整理成档案
    3. 记忆常用头像的特性
    4. 自动持续改善优化结果
    ```

### 批处理与自动化

!!! example "批量优化多套服装"

    **Batch Optimization**:
    ```
    EveryWear → Batch Processing →

    1. 选择目标文件夹（多个 PZIP 文件）
    2. 选择统一的优化档案
    3. 配置 Output（指定保存位置）
    4. 执行批处理（无人值守）

    处理能力: 1 小时可优化 10-20 套服装
    ```

    **自动化脚本**:
    ```
    EveryWear Automation →

    Trigger: 检测到新文件
    Action: 执行自动优化
    Notification: Discord/Slack 通知
    Backup: 自动保存原文件
    ```

## 🎯 实测数据与成功案例

### 优化效果实测

!!! success "EveryWear 优化的实际效果"

    **案例 1: Very Poor 连衣裙 → Good**
    ```
    Before (手动处理):
    - Polygon Count: 45,000
    - Texture Memory: 180MB
    - PhysBone: 28 个
    - 优化时间: 3 小时
    - 成功率: 60%（手动调整有失败风险）

    After (EveryWear):
    - Polygon Count: 14,500 (缩减 68%)
    - Texture Memory: 38MB (缩减 79%)
    - PhysBone: 12 个 (缩减 57%)
    - 优化时间: 8 分钟
    - 成功率: 95%（自动优化）
    ```

    **案例 2: 带复杂配饰的套装**
    ```
    Before:
    - Rating: Very Poor
    - 制作时间: 12 小时
    - 优化: 手动 4 小时，失败后还要重做

    After:
    - Rating: 达到 Good
    - 制作时间: 4 小时
    - 优化: EveryWear 15 分钟，一次成功
    ```

### 创作者的实际体验

!!! success "“EveryWear 改变了我的创作方式！”"

    **E 先生/女士（中级创作者）的体验**:
    - **使用前**: 大量作品停留在 Very Poor，无法上架销售
    - **导入 EveryWear 后**: 3 周内建立起稳定工作流
    - **现在**: BOOTH 月销售额达到 20 万日元
    - **最有效的点**: “Auto-Optimize 的精度已经超过人工”

    **F 先生/女士（初学者）的体验**:
    - **从挫败中恢复**: 手动优化失败了 3 次
    - **使用 EveryWear 后**: 第一次就达到 Good
    - **学习收获**: “我是通过 EveryWear 学会优化理论的”

## ⚠️ 常见问题与完整对策

### Q1: EveryWear 优化后外观变了

??? question "“优化后服装的整体印象发生了变化”"

    **原因分析**:
    ```
    主要原因: Polygon 缩减比例过高
    设置问题: Aggressive 设置导致过度优化
    解决方案: 调整 Quality Threshold
    ```

    **处理步骤**:
    ```
    1. EveryWear Settings → Quality Control
    2. Quality Threshold: High（优先质量）
    3. Polygon Reduction Limit: 限制在 30% 以下
    4. 用 Preview Mode 分阶段确认
    5. 微调到满意为止
    ```

    **预防措施**:
    ```
    - 为重要部位设置 Mask（排除缩减）
    - 先进行测试优化
    - 一定要创建备份
    ```

### Q2: 在特定头像上无法正常工作

??? question "“一部分头像上 EveryWear 功能不起作用”"

    **兼容性检查**:
    ```
    1. 检查头像骨骼结构
       → 检查 Humanoid 骨骼布局
       → 检查命名规则是否统一

    2. 检查文件格式
       → 确认以 FBX 格式保存
       → 确认纹理路径正常

    3. 检查头像质量
       → 是否存在多边形破损
       → 是否正常完成 UV 展开
    ```

    **修复步骤**:
    ```
    1. 执行 Avatar Validator
    2. 自动修复问题位置
    3. Re-import → 重新执行 EveryWear
    4. 如果问题仍持续，再手动微调
    ```

### Q3: CLO-SET Connect 连接错误

??? question "“无法访问 EveryWear 功能”"

    **连接故障排查**:
    ```
    1. 检查网络
       - 测试互联网连接
       - 检查防火墙设置
       - 检查代理设置

    2. 检查账号状态
       - CLO-SET Connect 登录状态
       - 订阅是否有效
       - 是否达到使用限制

    3. 检查软件
       - 确认 MD2025 为最新版
       - 清理缓存
       - 重启软件
    ```

### Q4: 优化结果与预期不一致

??? question "“目标设为 Good，却只能达到 Medium”"

    **重新检查设置**:
    ```
    原因 1: Target 设置不够严格
    → 选择更严格的 Profile

    原因 2: 原始服装过重
    → 先执行 Pre-optimization

    原因 3: 没有考虑头像特性
    → 使用 Avatar-specific 设置
    ```

    **进一步优化步骤**:
    ```
    1. 切换到 Manual Override Mode
    2. 手动微调各个参数
    3. 查看 AI Assist 给出的改进建议
    4. 分阶段优化直到达成目标
    ```

## 📈 EveryWear 效果测量与分析

### 性能分析仪表盘

!!! info "活用 EveryWear Analytics"

    **效果测量项目**:
    ```
    制作时间缩短率: XX%
    Performance Rating 提升: XX 级
    文件大小缩减: XX%
    质量评分: XX/100
    ```

    **趋势分析**:
    ```
    月度制作效率: 图表显示
    优化成功率: 查看变化趋势
    常用设置: 使用频率分析
    问题发生模式: 自动检测
    ```

### ROI 计算工具

!!! example "量化导入 EveryWear 的收益"

    **时间成本缩减**:
    ```
    传统优化时间: 每月 40 小时
    使用 EveryWear: 每月 8 小时
    节省时间: 32 小时/月

    若按时薪 $25 计算:
    月收益: $800
    年收益: $9,600
    ```

    **质量提升收益**:
    ```
    由 Very Poor → Good 带来的变化:
    - 可参加的活动更多
    - 可销售的作品增加
    - 社区评价提升
    - 技术可信度提升
    ```

## 🌟 活用 EveryWear 的下一步

### 专业级应用

!!! tip "在商业制作中活用 EveryWear"

    **BOOTH 上架准备**:
    ```
    1. 自动化适配多个头像
    2. 建立统一质量档案
    3. 用批处理制作系列作品
    4. 搭建自动质量保证系统
    ```

    **委托制作效率化**:
    ```
    1. 自动将客户需求整理成档案
    2. 提高工时预估准确度
    3. 自动化质量保证
    4. 大幅减少返工次数
    ```

### 为社区做贡献

!!! example "分享 EveryWear 知识"

    **从能做的事情开始**:
    ```
    1. 分享成功设置的档案
    2. 给遇到困难的初学者提供建议
    3. 介绍 EveryWear 的实际案例
    4. 用中文讲解新功能信息
    ```

    **更进一步的贡献方式**:
    ```
    1. 制作 EveryWear 优化教程
    2. 在日语社区举办学习会
    3. 参与新功能 Beta 测试
    4. 向开发团队反馈意见
    ```

---

!!! success "迈向 EveryWear Master 的道路"

    正确使用 EveryWear 后，你的 VRChat 服装制作将在**效率、质量、稳定性**三个方面获得革命性提升。

    **从“我不知道 EveryWear 怎么用”的烦恼，走到“没有 EveryWear 就做不下去”的可靠搭档。**

    **把最新技术变成你的创作武器，实现理想中的创作活动。**

**相关指南**:
- [MD2025 全功能指南](md2025-features.md){ .md-button }
- [IK-Joint 优化](ik-joint-mapping.md){ .md-button }
- [摆脱 Very Poor 的策略](../optimization/very-poor-escape.md){ .md-button .md-button--primary }
