# Spiral Room Navigation

**Time limit:** 1 second
**Memory limit:** 256 MB

Kian is trapped inside a **square-shaped room** whose floor is tiled with `n × n` **square tiles**.
Each tile has a **unique number**, and the numbering follows a **spiral pattern** as shown below for `n = 5`:

```
13 12 11 10  9
14 23 22 21  8
15 24 25 20  7
16 17 18 19  6
 1  2  3  4  5
```

Kian knows there is a **candle** somewhere in the room.
He wants to reach it, but since the room is dark, he can’t see anything.
Your task is to help him determine **how much** and **in which directions** he needs to move to reach the candle.

---

## Input

A single line contains three integers `n`, `s`, and `d`, separated by spaces:

* `n`: the size of the room (the floor is `n × n`)
* `s`: the tile number Kian is currently standing on
* `d`: the tile number where the candle is located

### Constraints

```
2 ≤ n ≤ 2000
1 ≤ s ≠ d ≤ n²
```

---

## Output

You must print **up to two lines**:

* **First line:** horizontal movement

  ```
  <value> <direction>
  ```

  * `<direction>` is `L` if Kian must move left, `R` if right.
  * If no horizontal movement is needed, **omit this line**.

* **Second line:** vertical movement

  ```
  <value> <direction>
  ```

  * `<direction>` is `U` if Kian must move up, `D` if down.
  * If no vertical movement is needed, **omit this line**.

---

## Examples

### Sample Input 1

```
5 1 25
```

### Sample Output 1

```
2 R
2 U
```

---

### Sample Input 2

```
5 3 22
```

### Sample Output 2

```
3 U
```

---

### Sample Input 3

```
15 67 24
```

### Sample Output 3

```
3 R
8 U
```

---

## Explanation

* The tiles are numbered in a **clockwise spiral**, starting from the **bottom-left corner**.
* Each tile has coordinates `(row, column)`.
  The **bottom-left tile** (`1`) is at `(1, 1)`,
  and the **top-right tile** (`n² - n + 1`) is near the top edge.
* You need to find the coordinates of tiles `s` and `d`,
  compute the horizontal and vertical differences,
  and print them in the format described above.

---

## نسخهٔ فارسی (متن اصلی)

محدودیت زمان: ۱ ثانیه
محدودیت حافظه: ۲۵۶ مگابایت

کیان در اتاقی مربع‌شکل با کف کاشی‌کاری شده به ابعاد `n×n` گیر افتاده است.
کاشی‌ها به‌صورت **مارپیچی** و با شماره‌های یکتا شماره‌گذاری شده‌اند.

با گرفتن شماره‌ی کاشی‌ای که کیان روی آن قرار دارد (`s`) و شماره‌ی کاشی‌ای که شمع روی آن است (`d`)،
بگویید کیان **چند کاشی و در چه جهتی** باید حرکت کند تا به شمع برسد.

**ورودی:**
در یک خط سه عدد `n s d` داده می‌شود.

**خروجی:**
تعداد و جهت حرکت در راستای افقی (`L` یا `R`)
و عمودی (`U` یا `D`) را طبق فرمت گفته‌شده چاپ کنید.