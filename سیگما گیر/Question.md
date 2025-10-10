Here’s a **clean and GitHub-ready Markdown version** of your problem statement, formatted consistently with your previous ones 👇

---

# Nested Summation Calculation

**Time limit:** 1 second
**Memory limit:** 50 MB

Write a program that takes two integers, `n` and `m`, and computes the value of the following expression:

[
\sum_{i=-10}^{m} \sum_{j=1}^{n} (i + j)^3 \times j^2
]

---

## Input

* The first line contains the integer `n`.
* The second line contains the integer `m`.

### Constraints

```
0 ≤ n, m ≤ 10
```

---

## Output

Print the value of the given expression in a single line.

---

## Examples

### Sample Input 1

```
3
2
```

### Sample Output 1

```
-2349
```

---

### Sample Input 2

```
1
-10
```

### Sample Output 2

```
-729
```

---

## Explanation

The program must calculate:

[
\sum_{i=-10}^{m} \sum_{j=1}^{n} (i + j)^3 \times j^2
]

That means for each `i` from `-10` to `m`,
and for each `j` from `1` to `n`,
you add up `(i + j)^3 * j^2`.
