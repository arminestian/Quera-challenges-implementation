# Greatest Common Divisor (GCD) and Least Common Multiple (LCM)

**Time limit:** 1 second
**Memory limit:** 128 MB

Write a program that reads two integers `n` and `m` and prints their **Greatest Common Divisor (GCD)** and **Least Common Multiple (LCM)**.

---

## Input

Two integers `n` and `m` are given in one line, separated by a space.

### Constraints

```
1 ≤ n, m ≤ 10⁹
```

---

## Output

Print the **GCD** and **LCM** of `n` and `m`, separated by a space.

---

## Example

### Sample Input

```
8 20
```

### Sample Output

```
4 40
```

---

## Explanation

* The **GCD** of 8 and 20 is 4.
* The **LCM** of 8 and 20 is 40.
* Formula used:
  [
  \text{LCM}(n, m) = \frac{n \times m}{\text{GCD}(n, m)}
  ]

---

## نسخهٔ فارسی (متن اصلی)

محدودیت زمان: ۱ ثانیه
محدودیت حافظه: ۱۲۸ مگابایت

برنامه‌ای بنویسید که دو عدد `n` و `m` را دریافت کرده و **ب.م.م** (بزرگ‌ترین مقسوم‌علیه مشترک) و **ک.م.م** (کوچک‌ترین مضرب مشترک) آن‌ها را چاپ کند.

**ورودی:**
در یک خط ابتدا عدد `n` و سپس عدد `m` داده می‌شود.
**خروجی:**
ابتدا ب.م.م و سپس ک.م.م را با فاصله از هم چاپ کنید.