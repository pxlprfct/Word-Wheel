# Solving a ‘Word Wheel’ with Python

[Blog post](http://ollie.work/2016/10/13/Solving-a-Word-Wheel-with-Python)

**How many different words can you make with a ‘Word Wheel’?**

## Rules
Each word must always include the centre letter, and each letter can only be used as many times as it is on the wheel (in the example below - 'a' is on the wheel twice, so it can be used twice in the same word).

![Image of a Word Wheel](http://d33wubrfki0l68.cloudfront.net/9fa6f80fffdbe63b16fe900b3fb82adf8ded6414/3f1e9/images/word-wheel.png)

##### Valid words
- Calm
- Ale
- Bale

##### Invalid words
- Hello (Invalid Letters)
- Cane (Middle letter not used)
- Mama ('M' used twice, despite only appearing in the wheel once)

#### Output
```
Optional Letters - n c m u a b e a
Required Letters - l
With that letter set, there are 117 valid words

abel
abele
able
ala
…
