# Solving a ‘Word Wheel’ with Python

[Blog Post](http://ollie.work/2016/10/13/Solving-a-Word-Wheel-with-Python)

### Question
> By using any of the letters in the ‘Word Wheel’ - How many different words can you make? Each word must always include the centre letter, and each letter can only be used as many times as it is on the wheel (In the example below - 'a' and 'e' are on the wheel twice).

![Image of a Word Wheel](http://d33wubrfki0l68.cloudfront.net/9fa6f80fffdbe63b16fe900b3fb82adf8ded6414/3f1e9/images/word-wheel.png)

#### Example Valid Words
- Calm
- Ale
- Bale

#### Example Invalid Words
- Hello (Invalid Letters)
- Cane (Middle letter not used)
- Mama ('M' used twice, despite only appearing in the wheel once)

This is by no means the optimal way of solving the problem - and could probably be made a lot more ‘pythonic’ - but it’s a good way of pretending to be better at the word puzzles than you actually are (which is good enough for me).

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
```
