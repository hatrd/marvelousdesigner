# 软件确认指南

<span class="time-estimate">预计耗时: 约 15 分钟</span> <span class="difficulty-beginner">适合初学者</span>

**本页目标**: 确认 VRChat 服装制作所需的软件都已正确安装。

!!! info "开始之前"
    本指南默认你已经安装好 Marvelous Designer、Unity 和 Blender。如果还没有安装，请先前往各软件的官网下载安装。

## 📋 确认检查清单

### ✅ Marvelous Designer（最重要）

<div class="step-container">
<div class="step-number">步骤 1: 确认版本</div>

1. 请先启动 **Marvelous Designer**
2. 如果无法启动，请查看[故障排查](#marvelous-designer启动故障)
3. 点击顶部菜单中的 **「帮助」** → **「关于 Marvelous Designer」**
4. 确认版本信息

**推荐版本**:

- <span class="software-version">2025.x</span>（最新版）
- <span class="software-version">2024.2</span> 及以上（已验证可用）

!!! warning "如果你正在使用较旧版本"
    如果版本早于 2024.0，本指南中的部分功能可能无法使用。可以的话，建议更新到最新版。
</div>

<div class="step-container">
<div class="step-number">步骤 2: 确认许可证</div>

1. 确认 Marvelous Designer 可以正常运行
2. 如果你使用的是试用版，请确认剩余天数
3. 通过 **「File」** → **「New Project」** 确认可以创建新建项目

**许可证状态**:
- ✅ **正式许可证**: 可无功能限制使用
- ⚠️ **试用版**: 有 30 天期限限制，但足够用于学习
- ❌ **已过期**: 需要续订或更新许可证
</div>

### ✅ Unity Hub 和 Unity Editor

<div class="step-container">
<div class="step-number">步骤 3: 确认 Unity Hub</div>

1. 请启动 **Unity Hub**
2. 在左侧菜单中选择 **「Installs」**
3. 确认当前已安装的 Unity 版本

**所需版本**:

- <span class="software-version">Unity 2022.3.22f1</span>（**VRChat 推荐版本**）
- 或 <span class="software-version">Unity 2022.3.x</span> 系列中的较新版本

!!! tip "如果没有 Unity 2022.3.22f1"
    1. 点击 Unity Hub 顶部的 **「Install」**
    2. 选择 **「Install Editor」**
    3. 在 **「Recommended Release」** 中找到 2022.3.22f1 并安装
    4. 安装时建议一并安装 **「Android Build Support」** 和 **「iOS Build Support」**，方便以后继续做面向 VRChat 的扩展开发
</div>

### ✅ VRChat Creator Companion（VCC）

<div class="step-container">
<div class="step-number">步骤 4: 确认 VCC</div>

1. 请启动 **VRChat Creator Companion**
   - 如果尚未安装，请前往 [VCC 官网](https://vcc.docs.vrchat.com/) 下载
2. 确认顶部显示的版本信息
3. 在 **「Settings」** → **「Unity Editors」** 中确认 Unity 2022.3.22f1 已被识别

**确认要点**:
- ✅ VCC 能正常启动
- ✅ Unity 2022.3.22f1 已被识别
- ✅ 网络连接正常（后续需要更新 SDK）
</div>

### ✅ 辅助软件

<div class="step-container">
<div class="step-number">步骤 5: 其他确认项</div>

**Blender**:
1. 启动 Blender 并确认版本
2. 推荐 <span class="software-version">Blender 3.0</span> 及以上
3. 这份指南不会直接用到 Blender，但在更进阶的编辑阶段可能会需要

**文本编辑器（推荐）**:
- 记事本、VS Code 或其他可以编辑配置文件的工具
</div>

## 📁 准备文件和文件夹

<div class="step-container">
<div class="step-number">步骤 6: 创建工作文件夹</div>

1. 在桌面或文档目录下创建 **「VRChat衣装制作」** 文件夹
2. 在其中继续创建以下子文件夹:

```
VRChat衣装制作/
├── Avatars/          (用于存放 FBX 文件)
├── Garments/         (用于存放 PZIP 文件)
├── UnityProjects/    (用于存放 Unity 项目)
├── Exports/          (用于存放导出成品)
└── References/       (用于存放参考图片和资料)
```
</div>

<div class="step-container">
<div class="step-number">步骤 7: 确认你手头的文件</div>

请检查你已经准备好的文件:

**头像文件**（.fbx）:
- ✅ 文件大小合理（通常在 1MB 到 50MB 之间）
- ✅ 扩展名确认为 `.fbx`
- ✅ 文件未损坏（可先双击尝试打开）

**服装文件**（.pzip）:
- ✅ 扩展名确认为 `.pzip` 或 `.zip`
- ✅ 确认它是 Marvelous Designer 使用的文件

!!! tip "关于文件准备"
    先把手头的文件复制到刚创建的文件夹中，后续操作会顺很多。
</div>

## 🔧 故障排查

### Marvelous Designer 启动故障 {#marvelous-designer启动故障}

??? question "“Marvelous Designer 无法启动”"
    **可能原因与处理方法**:

    1. **许可证问题**
       - 确认许可证仍然有效
       - 检查网络连接
       - 确认试用版是否已到期

    2. **系统要求不足**
       - 需要 Windows 10/11（64bit）
       - 建议内存至少 8GB，理想情况是 16GB 以上
       - 必须具备支持 DirectX 11 的显卡

    3. **安装问题**
       - 尝试以管理员身份运行
       - 检查杀毒软件的排除设置
       - 必要时重新安装

??? question "“画面一片空白”"
    **处理方法**:

    1. 更新显卡驱动
    2. 重置配置文件
    3. 尝试以兼容模式启动

### Unity 相关故障

??? question "“找不到 Unity 2022.3.22f1”"
    **处理方法**:

    1. 通过 Unity Hub 安装准确版本
    2. 从 [Unity Archive](https://unity.com/releases/editor/archive) 直接下载
    3. 安装时务必同时安装 **「Visual Studio Community」**

??? question "“VCC 识别不到 Unity”"
    **处理方法**:

    1. 重启 VCC
    2. 以管理员身份运行 Unity Hub
    3. 先启动一次 Unity Editor，再回到 VCC 中确认

## ✅ 确认完成检查清单

全部确认完成后，请在这里打勾:

<div class="progress-checklist">
<h4>软件确认完成</h4>

- [ ] Marvelous Designer 2024.2 以上版本可正常启动
- [ ] Unity 2022.3.22f1 已安装
- [ ] VRChat Creator Companion 可正常运行
- [ ] 已创建工作目录结构
- [ ] 已确认 FBX 文件（头像）的状态
- [ ] 已确认 PZIP 文件（服装）的状态
- [ ] Blender 可正常运行（补充确认）
</div>

---

## 🚀 下一步

完成以上确认后，就可以正式开始使用 Marvelous Designer 了。

[前往 Marvelous Designer 首次启动指南 →](md-first-launch.md){ .md-button .md-button--primary }

!!! success "辛苦了"
    基础环境确认已经完成。如果之后遇到问题，也可以查看[常见问题与处理方法](../workflows/common-issues.md)。
