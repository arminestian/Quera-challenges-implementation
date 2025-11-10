# Covid-19 Risk Color Code (Neverland)

**Time limit:** 1 second  
**Memory limit:** 256 MB

---

The ministry of health in Neverland classifies cities into three risk categories — **White**, **Yellow**, and **Red** — according to two indicators averaged over the past two weeks (per one million population):

- Let `p` be the average number of new **cases** per day (per 1,000,000).
- Let `q` be the average number of new **hospitalizations** per day (per 1,000,000).

The classification rules are:

- **White** (low risk) if and only if:
  - `p ≤ 50` **and** `q ≤ 10`.
- **Red** (high risk) if:
  - `q > 30`.
- **Yellow** (medium risk) otherwise.

Note: `q ≤ p` always holds in the input.

---

## Input
Two lines:

- First line: integer `p` (0 ≤ `p` ≤ 1000) — average new cases per day per 1,000,000.  
- Second line: integer `q` (0 ≤ `q` ≤ 500, `q` ≤ `p`) — average new hospitalizations per day per 1,000,000.

---

## Output
Print one of the strings `White`, `Yellow`, or `Red` — the color code for the city according to the rules above.

---

## Examples

### Example 1
**Input**
```

50
7

```
**Output**
```

White

```

### Example 2
**Input**
```

60
40

```
**Output**
```

Red

```

### Example 3
**Input**
```

15
12

```
**Output**
```

Yellow