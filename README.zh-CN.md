# Worldwave Radio 2077 中文说明

<p align="center">
  <strong>一个赛博复古风格的全球网络收音机体验页面。</strong>
</p>

<p align="center">
  <a href="./README.md">English README</a>
  ·
  <a href="https://dreaminmaster.github.io/Worldwave-Radio-2077/">在线演示</a>
</p>

<p align="center">
  <img src="./assets/preview.gif" alt="Worldwave Radio 2077 动态预览" width="600">
</p>

<p align="center">
  <img src="./assets/preview.svg" alt="Worldwave Radio 2077 页面预览" width="900">
</p>

---

## 在线演示

GitHub Pages 地址：

**https://dreaminmaster.github.io/Worldwave-Radio-2077/**

---

## 项目简介

**Worldwave Radio 2077** 不只是一个普通的收音机播放器。

它把全球网络电台包装成了一个带有仪式感的赛博复古控制台：开机界面、国家切换、电台列表、调频滑块、预设按钮、机械点击音、白噪声、CRT 扫描线和示波器视觉效果，共同组成了一个更像“未来旧机器”的网页体验。

这个项目的重点不是做一个工具型电台网站，而是展示一种有氛围、有交互、有个人风格的网页界面设计。

---

## 主要功能

- 支持 **27 个国家**的网络电台：中国、美国、日本、英国、俄罗斯、澳大利亚、新西兰、韩国、加拿大、法国、朝鲜、西班牙、瑞士、希腊、德国、意大利、荷兰、瑞典、挪威、丹麦、芬兰、奥地利、比利时、爱尔兰、葡萄牙、卢森堡、冰岛
- 按国家切换网络电台（可滚动选择）
- 电台列表展示
- 模拟调频滑块
- 预设电台按钮
- **音量旋钮** — 拖拽旋转控制音量
- **微调旋钮** — 拖拽旋转调节播放速率（模拟收音机微调变调效果）
- 开机遮罩动画
- 机械点击音效
- 白噪声模拟
- Canvas 示波器视觉效果（本地模式：真实音频驱动 / 在线模式：逼真模拟）
- CRT 扫描线效果
- 移动端适配基础布局
- PWA manifest 基础结构

---

## 运行方式

克隆仓库：

```bash
git clone https://github.com/Dreaminmaster/Worldwave-Radio-2077.git
cd Worldwave-Radio-2077
```

**推荐启动（真实声波示波器）：**

```bash
python3 serve.py
```

然后打开 `http://localhost:8080`。内置 CORS 代理，示波器会显示真实的音频波形。

**普通启动（模拟声波）：**

```bash
python3 -m http.server 8080
```

然后打开：

```text
http://localhost:8080
```

---

## 使用说明

部分电台可能因为源地址失效、地区限制、HTTPS限制或跨域问题无法播放。这是公共网络电台源常见情况，不一定是页面代码本身的问题。

当前版本主要保留原型逻辑，重点放在作品展示、视觉氛围和 GitHub 项目包装上。

---

## 使用限制

本项目仅允许用于：

- 个人观看
- 学习参考
- 作品集展示
- 非商业演示

未经 Dreaminmaster 书面许可，不允许用于商业用途、付费转售、二次包装销售、客户项目、商业网站、广告或任何变现服务。

详细限制请查看 [LICENSE](./LICENSE)。

---

## 作者

Created by **Dreaminmaster**.

Copyright © 2026 Dreaminmaster. All rights reserved.
