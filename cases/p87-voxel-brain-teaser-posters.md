# P87. Voxel Brain Teaser Posters

## 👀 Preview

[<img src="../assets/p87-voxel-brain-teaser-posters/source-example-01.jpg" width="320" height="400" alt="Voxel Brain Teaser Posters — source example 1">](../assets/p87-voxel-brain-teaser-posters/source-example-01.jpg)

[<img src="../assets/p87-voxel-brain-teaser-posters/source-example-02.jpg" width="320" height="400" alt="Voxel Brain Teaser Posters — source example 2">](../assets/p87-voxel-brain-teaser-posters/source-example-02.jpg)

[<img src="../assets/p87-voxel-brain-teaser-posters/source-example-03.jpg" width="320" height="400" alt="Voxel Brain Teaser Posters — source example 3">](../assets/p87-voxel-brain-teaser-posters/source-example-03.jpg)

## 👇 Workflow

`Topic variable → voxel puzzle posters`

## 🔖 Full Prompt

```text
4 images, 4:5, mindboggling hard math, science, logic, riddle questions that would make IQ 150 people cry. INPUT: $ TOPIC # Build a difficulty field D over the topic. D = infer_conceptual_depth($ TOPIC) # Sample 4 questions at increasing thresholds of D. Q1 = generate_question($ TOPIC, difficulty='easy') Q2 = generate_question($ TOPIC, difficulty='medium') Q3 = generate_question($ TOPIC, difficulty='hard') Q4 = generate_question($ TOPIC, difficulty='brutal') # Render voxel poster with Q1–Q4.
```

<sub>(by [@Gdgtify](https://x.com/Gdgtify/status/2101753259325063485)) · [Source: X](https://x.com/Gdgtify/status/2101753259325063485)</sub>
