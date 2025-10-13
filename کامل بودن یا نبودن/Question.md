# Perfect Number Check

**Time limit:** 2 seconds
**Memory limit:** 256 MB

Write a program that reads an integer `n` and determines whether it is a **perfect number**.
If it is perfect, print `YES`; otherwise, print `NO`.


## Definition

A **positive integer** `n` is called **perfect** if and only if the **sum of its positive divisors**, excluding itself, is **equal to `n`**.

For example:

* 6 is perfect because its divisors (excluding itself) are `1`, `2`, and `3`, and `1 + 2 + 3 = 6`.
* 27 is **not** perfect because its divisors (excluding itself) are `1`, `3`, and `9`, and `1 + 3 + 9 = 13 ≠ 27`.


## Input

A single line containing an integer `n`.

### Constraints

```
2 ≤ n ≤ 200000
```


## Output

Print:

* `YES` — if `n` is a perfect number
* `NO` — otherwise

## Examples

### Sample Input 1

```
27
```

### Sample Output 1

```
NO
```

**Explanation:**
The divisors of 27 less than itself are `1`, `3`, and `9`.
Their sum is `1 + 3 + 9 = 13 ≠ 27`.
Therefore, 27 is not perfect.


### Sample Input 2

```
6
```

### Sample Output 2

```
YES
```

**Explanation:**
The divisors of 6 less than itself are `1`, `2`, and `3`.
Their sum is `1 + 2 + 3 = 6`.
Therefore, 6 is a perfect number.


## نسخهٔ فارسی (متن اصلی)

محدودیت زمان: ۲ ثانیه
محدودیت حافظه: ۲۵۶ مگابایت

برنامه‌ای بنویسید که عددی مانند `n` را از ورودی گرفته و بررسی کند آیا خاصیت **کامل بودن** دارد یا خیر.

عددی **کامل** است اگر مجموع تمام مقسوم‌علیه‌های مثبت آن (به جز خودش) برابر خود عدد باشد.

**ورودی:**
در یک خط عدد `n` داده می‌شود.

**خروجی:**
اگر عدد کامل بود `YES`
در غیر این صورت `NO` را چاپ کنید.