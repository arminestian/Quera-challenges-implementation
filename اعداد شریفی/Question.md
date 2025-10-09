# Sharifi Numbers Finder

**Time limit:** 1 second
**Memory limit:** 256 MB

Every year on **December 6 (16 Azar)**, Sharif University students participate in the *Sharifi Numbers* contest.
The challenge is as follows:

You are first given an integer `n`, and then `n` integers `a₁, a₂, a₃, …, aₙ`.
Next, you must compute the value of:

[
EndInterval = 2 \times \sum_{i=1}^{n} \sum_{j=i+1}^{n} a_i \times a_j
]

After calculating this value, print all **Sharifi numbers** in the interval **[100, EndInterval]**, inclusive.

---

## Definition — Sharifi Number

A number is called a **Sharifi number** if it is equal to the sum of its digits raised to the power of the number of digits.

For example:

[
153 = 1^3 + 5^3 + 3^3
]

So, **153** is a Sharifi number.

---

## Input

* The first line contains an integer `n`.
* The next `n` lines each contain one integer `aᵢ`.

### Constraints

```
1 ≤ n ≤ 20
1 ≤ aᵢ ≤ 100
```

---

## Output

Print all **Sharifi numbers** in the range `[100, EndInterval]` (including both endpoints),
each on a separate line.

---

## Example

### Sample Input 1

```
5
3
3
3
3
3
```

### Sample Output 1

```
153
```

---

## Notes

* The formula for `EndInterval` grows quickly with `n`, so be careful with large sums.
* You can use simple iteration or list comprehension to find the Sharifi numbers.