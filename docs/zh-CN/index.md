# VRChat 服装制作完整指南

## 欢迎，你也能做出好看的 VRChat 服装

**“我真的能做到吗……”** 你是不是也有这种不安？

没问题。这份指南就是为**完全零基础的读者**准备的。你不需要会编程，也不需要有 3D 建模经验。只要按步骤慢慢来，最终一定能做出自己理想中的服装。

<div class="step-container">
<div class="step-number">✨ 你将学会制作的内容</div>

<ul>
<li><strong>礼服</strong>: 从优雅的正式礼服到可爱的日常连衣裙</li>
<li><strong>T 恤</strong>: 从基础款到个性化设计</li>
<li><strong>裙子</strong>: 从伞裙、百褶裙到短裙和长裙</li>
<li><strong>休闲服</strong>: 覆盖日常穿搭到更讲究的风格</li>
<li><strong>连衣裙</strong>: 一体式的优美轮廓</li>
<li><strong>泳装</strong>: 贴身、特殊材质的服装类型</li>
</ul>

<p>更重要的是，你可以做出<strong>能在 VRChat 中自然运动的服装</strong>。</p>
</div>

## 这份指南的特点

### 🎯 面向完全初学者
- **可以从零开始**: 不需要任何前置知识
- **术语解释清晰**: 专有名词也会逐步说明
- **不怕出错**: 会同时告诉你如何回退和修正

### ⏰ 现实可行的学习节奏
- **第一次完整体验**: 2 到 3 小时（把现成服装适配到你的头像上）
- **制作一件 T 恤**: 4 到 6 小时（基础原创服装）
- **制作一件礼服**: 8 到 12 小时（更复杂的服装）

### 🛠 支持较新的软件版本
- **Marvelous Designer 2025**: <span class="software-version">支持最新版</span>
- **Unity 2022.3.22f1**: <span class="software-version">VRChat 推荐版本</span>
- **VRChat SDK3**: <span class="software-version">支持 v3.8.2</span>

## 建议的学习顺序

### 📚 推荐学习路径

=== "初学者路线（推荐）"

    **阶段 1: 基础准备（第 1 天）**

    1. [软件确认](setup/software-check.md) <span class="time-estimate">15 分钟</span>
    2. [Marvelous Designer 首次启动](setup/md-first-launch.md) <span class="time-estimate">30 分钟</span>
    3. [理解基础界面](basics/md-interface.md) <span class="time-estimate">45 分钟</span>

    **阶段 2: 第一次成功体验（第 2 天）**

    4. [导入头像](workflows/avatar-import.md) <span class="time-estimate">30 分钟</span>
    5. [适配现有服装](workflows/garment-fitting.md) <span class="time-estimate">2 小时</span>

    **阶段 3: 开始原创制作（第 3 到 4 天）**

    6. [制作 T 恤](garments/t-shirt.md) <span class="difficulty-beginner">初学者</span> <span class="time-estimate">4 到 6 小时</span>
    7. [基础物理设置](physics/fabric-properties.md) <span class="time-estimate">1 小时</span>

    **阶段 4: 发布到 VRChat（第 5 天）**

    8. [Unity 集成](unity/project-setup.md) <span class="time-estimate">1 小时</span>
    9. [上传到 VRChat](unity/avatar-upload.md) <span class="time-estimate">1 小时</span>

=== "想尽快跑通的人"

    **最短路径（1 到 2 天）**

    1. [软件确认](setup/software-check.md) ✅
    2. [适配现有服装](workflows/garment-fitting.md) ✅
    3. [Unity 集成和上传](unity/project-setup.md) ✅

    *建议先用现成服装跑通一次完整流程，再挑战原创制作。*

## 常见顾虑与回答

??? question "“我真的能做到吗……”"
    **当然可以。** 这份指南就是和零基础读者一起打磨出来的。只要一个阶段一个阶段完成，你就一定能做出来。

??? question "“大概要花多久？”"
    **第一次完成一套流程（适配现有服装）**: 2 到 3 小时
    **原创 T 恤**: 4 到 6 小时
    **复杂礼服**: 8 到 12 小时

    熟练之后，你完成同样的工作通常只需要一半时间。

??? question "“如果失败了怎么办……”"
    **失败本来就是学习的一部分。** 这份指南会尽量告诉你“哪里容易出错”“出错后怎么回退”，所以可以放心尝试。

??? question "“软件看起来很难……”"
    **一开始大家都会这样觉得。** 所以本指南会先从最少必须掌握的功能开始，再逐步扩展你的操作范围。

??? question "“在 VRChat 里被别人看到会不会很尴尬……”"
    **你可以先在私人世界里测试。** 先在不会被别人看到的环境里练习，等有把握后再公开使用。

## 需要准备的东西

### ✅ 必备软件（部分带试用期）
- [Marvelous Designer](https://www.marvelousdesigner.com/) - 服装制作主软件
- [Unity Hub](https://unity.com/download) - 用于 VRChat 集成
- [VRChat Creator Companion](https://vcc.docs.vrchat.com/) - 用于管理 SDK

### 📁 必要文件
- **VRChat 头像的 FBX 文件** ← 你已经持有
- **服装的 PZIP 文件** ← 你已经持有

!!! info "关于文件"
    既然你已经有 FBX 文件和 PZIP 文件，就不需要另外再准备新的素材了。

### 💻 推荐电脑配置
- **操作系统**: Windows 10/11（64bit）
- **内存**: 建议 16GB 以上
- **显卡**: 支持 DirectX 11
- **存储空间**: 至少预留 10GB

## 社区与支持

### 🌟 日语社区
- [VRChat 服装制作 Discord](resources/community.md#discord)
- [Marvelous Designer 日语论坛](resources/community.md#forum)
- [YouTube 教程合集](resources/useful-links.md#youtube)

### 📚 额外资源
- [实用链接集](resources/useful-links.md)
- [常见问题 FAQ](workflows/common-issues.md)
- [进阶资源](resources/advanced-resources.md)

---

## 开始吧

<div class="step-container">
<div class="step-number">🚀 第一步</div>

<p><strong>准备好了吗？</strong> 先从<a href="setup/software-check/">软件确认</a>开始，正式开启你的 VRChat 服装制作之旅。</p>

<p><strong>有不安和疑问也没关系。</strong> 我们就按顺序，一步一步往前走。</p>

<p><a href="setup/software-check/" class="md-button md-button--primary">前往软件确认 →</a></p>
</div>

---

<div class="progress-checklist">
<h4>📋 学习进度检查清单</h4>

- [ ] 已完成软件确认
- [ ] 已成功启动 Marvelous Designer
- [ ] 已成功导入头像
- [ ] 已完成现有服装适配
- [ ] 已完成第一次 Unity 集成
- [ ] 已成功上传到 VRChat
- [ ] 已完成原创 T 恤
- [ ] 已理解物理设置
- [ ] 已开始挑战更复杂的服装

*复选框状态会自动保存。*
</div>

!!! tip "学习建议"
    **不要试图一次把所有内容都弄懂。** 一次只解决一个阶段，通常反而会学得更快。别着急，持续做下去就行。
