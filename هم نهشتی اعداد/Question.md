# Common Moduli Finder

**Time limit:** 2 seconds
**Memory limit:** 256 MB

In this problem, you must find all positive integers `m` such that two given numbers `a` and `b` are **congruent modulo m**.

This means that the difference between the two numbers (`|a - b|`) must be divisible by `m`.
You must print **all such values of `m`** in **ascending order**.

---

## Input

Two integers `a` and `b`, separated by a space.

### Constraints

```
1 ≤ a, b ≤ 10⁵
```

---

## Output

Print all integers `m` (in ascending order) such that `a ≡ b (mod m)`.

---

## Example

### Sample Input

```
1 25
```

### Sample Output

```
2 3 4 6 8 12 24
```

---

## Explanation

For two numbers `a` and `b` to be congruent modulo `m`,
the condition `(a - b) % m == 0` must hold true.

Let:
[
d = |a - b|
]

Then all **positive divisors of `d`** are valid values for `m`.
Since `a = 1` and `b = 25`, we have:

[
d = |1 - 25| = 24
]

The positive divisors of 24 are:

```
1, 2, 3, 4, 6, 8, 12, 24
```

However, `m = 1` is excluded since modulo 1 makes all numbers congruent.
Thus, the valid moduli are:

```
2 3 4 6 8 12 24
```

---

## نسخهٔ فارسی (متن اصلی)

محدودیت زمان: ۲ ثانیه
محدودیت حافظه: ۲۵۶ مگابایت

برنامه‌ای بنویسید که دو عدد `a` و `b` را از ورودی بگیرد و تمام عددهایی را که این دو عدد می‌توانند **نسبت به آن هم‌نهشت باشند** بیابد.
اعداد خروجی باید **به صورت صعودی** چاپ شوند.

**ورودی:**
دو عدد `a` و `b` در یک خط با فاصله از هم داده می‌شود.

**خروجی:**
اعداد خروجی را به ترتیب صعودی چاپ کنید.

**توضیح:**
اعداد هم‌نهشت‌اند اگر اختلاف آن‌ها بر عدد مورد نظر بخش‌پذیر باشد.