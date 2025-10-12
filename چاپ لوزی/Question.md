# Solid Diamond Pattern

**Time limit:** 2 seconds
**Memory limit:** 256 MB

Write a program that reads a positive integer `n` and prints a **solid diamond** made of `*` characters with a diameter of `2n + 1`.

---

## Input

A single integer `n`.

### Constraints

```
1 ≤ n ≤ 10
```

---

## Output

Print the solid diamond with diameter `2n + 1` using the `*` character.

---

## Example

### Sample Input

```
3
```

### Sample Output

```
   *
  ***
 *****
*******
 *****
  ***
   *
```

---

## Explanation

* The diamond’s **height** and **width** are both equal to `2n + 1`.
* The pattern starts with one `*` at the top, increases until the middle line (which has `2n + 1` stars), and then decreases symmetrically.

---

## نسخهٔ فارسی (متن اصلی)

محدودیت زمان: ۲ ثانیه
محدودیت حافظه: ۲۵۶ مگابایت

برنامه‌ای بنویسید که عدد صحیح مثبت `n` را از کاربر بگیرد و یک **لوزی توپر** به قطر `2n + 1` چاپ کند.

**ورودی:**
در تنها خط ورودی عدد `n` آمده است.

**خروجی:**
در خروجی لوزی خواسته شده را چاپ کنید.