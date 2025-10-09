# Separate year and month (توابع: جدا کردن سال و ماه)

**Time limit:** 1 second
**Memory limit:** 50 MB

Write a program that reads your birth year and month concatenated together, separates the month from the year, and prints both.

## Problem statement

You are given a 4-character string that contains the year and month of birth concatenated (year first, then month). Split the input into the year (first two characters) and the month (last two characters) and print them in the required format.

## Input

A single line containing a string of length **4** representing the year and month of birth (YYMM).

## Output

Print two lines:

```
saal:YY
maah:MM
```

Where `YY` is the two-digit year (first two characters of the input) and `MM` is the two-digit month (last two characters of the input).

## Examples

**Sample Input 1**

```
7106
```

**Sample Output 1**

```
saal:71
maah:06
```

**Sample Input 2**

```
7011
```

**Sample Output 2**

```
saal:70
maah:11
```

**Sample Input 3**

```
0012
```

**Sample Output 3**

```
saal:00
maah:12
```

---

### Notes

* The input is always exactly 4 characters long.
* Do not add extra spaces or lines; follow the exact output format shown above.

---

### نسخهٔ فارسی (اصل مسأله)

محدودیت زمان: ۱ ثانیه
محدودیت حافظه: ۵۰ مگابایت

برنامه‌ای بنویسید که سال و ماه تولد شما را پشت سر هم دریافت کند، سپس ماه را از سال جدا کرده و هر دو را چاپ کند.

**ورودی:** در خط اول ورودی یک رشته به طول ۴ شامل ماه و سال تولد آمده است.
**خروجی:** در خروجی موارد خواسته شده را چاپ کنید.

(نمونه‌ها همان‌طور که در متن بالا آمده‌اند.)
