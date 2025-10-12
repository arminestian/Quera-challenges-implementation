# Comparing Drug Effectiveness Between Two Countries

**Time limit:** 1 second
**Memory limit:** 256 MB

Two countries, **Shekarestan** and **Namakestan**, both with roughly equal populations, have used different medicines to treat COVID-19 patients.
Each country has reported the number of infected and deceased individuals.

We want to determine **which country’s medicine is more effective**.
The country with a **greater number of recovered patients** is considered to have used **more effective medicine**.

The number of recovered patients in each country is calculated as:

[
\text{Recovered} = \text{Infected} - \text{Deaths}
]

---

## Input

The input consists of **four lines**:

* Line 1: An integer `n` — number of infected in **Shekarestan**
* Line 2: An integer `k` — number of deaths in **Shekarestan**
* Line 3: An integer `p` — number of infected in **Namakestan**
* Line 4: An integer `q` — number of deaths in **Namakestan**

### Constraints

```
1 ≤ k ≤ n ≤ 1000
1 ≤ q ≤ p ≤ 1000
```

---

## Output

Print one of the following strings in a single line:

* `Shekarestan` — if Shekarestan’s medicines are more effective
* `Namakestan` — if Namakestan’s medicines are more effective
* `Equal` — if both countries have the same number of recovered patients

---

## Examples

### Sample Input 1

```
2
1
4
1
```

### Sample Output 1

```
Namakestan
```

---

### Sample Input 2

```
3
1
4
2
```

### Sample Output 2

```
Equal
```

---

### Sample Input 3

```
5
1
4
2
```

### Sample Output 3

```
Shekarestan
```

---

## Explanation

* Recovered in **Shekarestan** = `n - k`
* Recovered in **Namakestan** = `p - q`

Compare the two numbers:

* If `n - k > p - q`, print **Shekarestan**
* If `n - k < p - q`, print **Namakestan**
* Otherwise, print **Equal**

---

## نسخهٔ فارسی (متن اصلی)

محدودیت زمان: ۱ ثانیه
محدودیت حافظه: ۲۵۶ مگابایت

دو کشور **شکرستان** و **نمکستان** با داروهای متفاوت بیماران کرونایی خود را درمان می‌کنند.
هر کشوری که تعداد **بهبودیافتگان بیشتری** داشته باشد، از **داروی موثرتری** استفاده کرده است.
تعداد بهبودیافتگان برابر است با تعداد مبتلایان منهای تعداد فوتی‌ها.

**ورودی:**
در چهار خط، به‌ترتیب:

1. `n`: مبتلایان شکرستان
2. `k`: فوتی‌های شکرستان
3. `p`: مبتلایان نمکستان
4. `q`: فوتی‌های نمکستان

**خروجی:**
اگر داروی شکرستان مؤثرتر بود، `Shekarestan`
اگر داروی نمکستان مؤثرتر بود، `Namakestan`
و اگر برابر بودند، `Equal` را چاپ کنید.