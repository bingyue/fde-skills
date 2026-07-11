# PPTX 生成代码模板

> 主文件 SKILL.md 中引用这些模板。按需加载。

---

## 目录

- [基础设置](#基础设置)
- [通用辅助函数](#通用辅助函数)
- [每页代码结构模板](#每页代码结构模板)
- [文字换行规则](#文字换行规则)
- [颜色规范](#颜色规范)
- [形状类型](#形状类型)
- [保存文件](#保存文件)

---

## 基础设置

```javascript
const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";  // 10 x 5.625 英寸
```

---

## 通用辅助函数

### 顶部标题条

```javascript
function addEliteHeader(slide, pres, titleCN, titleEN = "", theme = themeA) {
  // 顶部底色条
  slide.addShape("rect", {
    x: 0, y: 0, w: 10, h: 0.55,
    fill: { color: "FFFFFF" },
    line: { color: theme.border, width: 0.5 }
  });
  // 左侧强调竖条
  slide.addShape("rect", {
    x: 0, y: 0, w: 0.06, h: 0.55,
    fill: { color: theme.accent }, line: { color: theme.accent }
  });
  // 主标题（结论性语句）
  slide.addText(titleCN, {
    x: 0.15, y: 0.06, w: 8.3, h: 0.28,
    fontSize: 10, fontFace: "Microsoft YaHei",
    color: theme.primary, bold: true, wrap: true
  });
  // 英文副标题（可选）
  if (titleEN) {
    slide.addText(titleEN, {
      x: 0.15, y: 0.32, w: 7, h: 0.18,
      fontSize: 7.5, fontFace: "Arial",
      color: theme.midText, wrap: true
    });
  }
  // 右上角来源标注区
  slide.addText("Elite PPT Pro", {
    x: 8.5, y: 0.08, w: 1.4, h: 0.35,
    fontSize: 6, fontFace: "Arial",
    color: theme.midText, align: "right"
  });
}
```

### 数据来源引用

```javascript
function addDataSource(slide, pres, sourceText, theme = themeA) {
  slide.addShape("line", {
    x: 0.2, y: 5.38, w: 9.6, h: 0,
    line: { color: theme.border, width: 0.5 }
  });
  slide.addText("Source: " + sourceText, {
    x: 0.2, y: 5.42, w: 8.5, h: 0.15,
    fontSize: 7.5, fontFace: "Arial",
    color: theme.midText, wrap: false
  });
}
```

### 页码徽章

```javascript
function addPageBadge(slide, pres, pageNum, theme = themeA) {
  slide.addShape("rect", {
    x: 9.55, y: 5.2, w: 0.35, h: 0.25,
    fill: { color: theme.accent }, line: { color: theme.accent }
  });
  slide.addText(String(pageNum).padStart(2, "0"), {
    x: 9.55, y: 5.2, w: 0.35, h: 0.25,
    fontSize: 9, fontFace: "Arial",
    color: "FFFFFF", bold: true,
    align: "center", valign: "middle"
  });
}
```

### 关键指标卡片

```javascript
function addKPICard(slide, x, y, w, h, value, label, delta, theme = themeA) {
  // 卡片底色
  slide.addShape("rect", {
    x, y, w, h,
    fill: { color: theme.light }, line: { color: theme.border, width: 1 }
  });
  // 大数字
  slide.addText(value, {
    x: x + 0.1, y: y + 0.12, w: w - 0.2, h: 0.45,
    fontSize: 28, fontFace: "Arial", bold: true,
    color: theme.accent, align: "center"
  });
  // 指标标签
  slide.addText(label, {
    x: x + 0.1, y: y + 0.6, w: w - 0.2, h: 0.22,
    fontSize: 9, fontFace: "Microsoft YaHei",
    color: theme.darkText, align: "center", wrap: true
  });
  // 变化率（可选）
  if (delta) {
    const isPositive = delta.startsWith("+");
    slide.addText(delta, {
      x: x + 0.1, y: y + 0.82, w: w - 0.2, h: 0.18,
      fontSize: 9, fontFace: "Arial",
      color: isPositive ? "2D8A6A" : "C41E3A",
      align: "center", bold: true
    });
  }
}
```

### 分析要点列表

```javascript
function addBulletPoints(slide, x, y, w, h, title, points, theme = themeA) {
  // 标题
  slide.addText(title, {
    x, y, w, h: 0.28,
    fontSize: 10, fontFace: "Microsoft YaHei",
    color: theme.primary, bold: true
  });
  // 要点
  const bulletText = points.map(p => "▸ " + p).join("\n");
  slide.addText(bulletText, {
    x, y: y + 0.32, w, h: h - 0.32,
    fontSize: 10, fontFace: "Microsoft YaHei",
    color: theme.darkText, wrap: true, valign: "top",
    lineSpacingMultiple: 1.4
  });
}
```

### 数据卡片（带来源）

```javascript
function addDataCard(slide, x, y, w, h, title, content, source, borderColor, theme = themeA) {
  slide.addShape("rect", {
    x, y, w, h,
    fill: { color: "F8F9FA" }, line: { color: borderColor, width: 1.5 }
  });
  // 顶部色条
  slide.addShape("rect", {
    x, y, w, h: 0.06,
    fill: { color: borderColor }, line: { color: borderColor }
  });
  slide.addText(title, {
    x: x + 0.12, y: y + 0.1, w: w - 0.24, h: 0.26,
    fontSize: 11, fontFace: "Microsoft YaHei",
    color: borderColor, bold: true
  });
  slide.addText(content, {
    x: x + 0.12, y: y + 0.42, w: w - 0.24, h: h - 0.58,
    fontSize: 10, fontFace: "Microsoft YaHei",
    color: theme.darkText, wrap: true, valign: "top"
  });
  if (source) {
    slide.addText(source, {
      x: x + 0.12, y: y + h - 0.2, w: w - 0.24, h: 0.16,
      fontSize: 7, fontFace: "Arial",
      color: theme.midText, wrap: false
    });
  }
}
```

---

## 每页代码结构模板

```javascript
function createSlide_N(pres, theme, data) {
  // data = 从研究阶段收集的实际数据对象
  const slide = pres.addSlide();
  slide.background = { color: "FFFFFF" };

  // 1. 顶部标题条（必须）
  addEliteHeader(slide, pres, "结论性标题，直接写出洞察", "Conclusion as Title");

  // 2. 内容区域（至少4个区域）
  // 区域1：关键指标/数字
  // 区域2：图表（柱状/折线/散点）
  // 区域3：分析要点（3-5条）
  // 区域4：背景/对比数据

  // 3. 数据来源引用（必须）
  addDataSource(slide, pres, "Source: [机构], [机构] | [时间段]");

  // 4. 页码徽章（非封面页必须）
  addPageBadge(slide, pres, N);

  return slide;
}
```

---

## 文字换行规则

```javascript
// ❌ 错误：文字会重叠
slide.addText('第一行\n第二行', { x:0.5, y:1, w:4, h:1 });

// ✅ 正确：必须加 wrap: true
slide.addText('第一行\n第二行', {
  x: 0.5, y: 1, w: 4, h: 1,
  wrap: true,
  valign: "top"
});
```

---

## 颜色规范

```javascript
// ✅ 正确：6字符hex，无#前缀
color: "00A69C"

// ❌ 错误
color: "#00A69C"   // 带#
color: "00A69C33"  // 带透明度（pptxgenjs不支持）
```

---

## 形状类型

```javascript
// ✅ 使用字符串
slide.addShape("rect", { ... })
slide.addShape("oval", { ... })
slide.addShape("line", { ... })
slide.addShape("roundRect", { ... })

// ❌ 不要用 pres.ShapeType.xxx（可能不存在）
```

---

## 保存文件

```javascript
pres.writeFile({ fileName: "output.pptx" })
    .then(() => console.log("✅ 生成成功！"))
    .catch(err => console.error("❌ 错误：", err));
```
