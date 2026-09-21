# P87. 体素风烧脑题海报

[English](../p87-voxel-brain-teaser-posters.md) | [简体中文](p87-voxel-brain-teaser-posters.md)

## 👀 预览

[<img src="../../assets/p87-voxel-brain-teaser-posters/source-example-01.jpg" width="320" height="400" alt="体素风烧脑题海报——来源示例 1">](../../assets/p87-voxel-brain-teaser-posters/source-example-01.jpg)

[<img src="../../assets/p87-voxel-brain-teaser-posters/source-example-02.jpg" width="320" height="400" alt="体素风烧脑题海报——来源示例 2">](../../assets/p87-voxel-brain-teaser-posters/source-example-02.jpg)

[<img src="../../assets/p87-voxel-brain-teaser-posters/source-example-03.jpg" width="320" height="400" alt="体素风烧脑题海报——来源示例 3">](../../assets/p87-voxel-brain-teaser-posters/source-example-03.jpg)

## 👇 工作流

`主题变量 → 体素风谜题海报`

## 🔖 完整提示词

```text
4 张图，4:5，围绕数学、科学、逻辑和谜语生成难到连智商 150 的人都会抓狂的烧脑题。输入：$ TOPIC。# 在该主题上建立难度场 D。D = infer_conceptual_depth($ TOPIC) # 按 D 的递增阈值抽取 4 道题。Q1 = generate_question($ TOPIC, difficulty='easy') Q2 = generate_question($ TOPIC, difficulty='medium') Q3 = generate_question($ TOPIC, difficulty='hard') Q4 = generate_question($ TOPIC, difficulty='brutal') # 将 Q1–Q4 渲染为体素风海报。
```

<sub>(by [@Gdgtify](https://x.com/Gdgtify/status/2101753259325063485)) · [来源平台： X](https://x.com/Gdgtify/status/2101753259325063485)</sub>
