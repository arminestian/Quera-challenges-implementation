# 🧩 Title Case Movie Names

**Time limit:** 1 second
**Memory limit:** 128 MB

فرزاد بعد از پایان امتحان‌های میان‌ترم می‌خواهد فیلم تماشا کند، اما نام فیلم‌هایی که از دانیال گرفته است نامنظم هستند.
او می‌خواهد نام هر فیلم به‌صورت مرتب نوشته شود، به طوری که **حرف اول هر کلمه uppercase** و **بقیه حروف lowercase** باشند.
برنامه‌ای بنویسید که این کار را برایش انجام دهد.


## Input

* The first line contains an integer `n` — the number of movie titles.
* The next `n` lines each contain one movie title (each less than 1000 characters).

### Constraints

```
1 ≤ n ≤ 10
```


## Output

Print the corrected (title-cased) movie names, one per line.


## Examples

### Sample Input 1

```
3
rEd riDing HOoD
DraCUla
Bad LiEutenAnt
```

### Sample Output 1

```
Red Riding Hood
Dracula
Bad Lieutenant
```


### Sample Input 2

```
2
21 jUMp Street
Mr. SMith GoEs To WashinGTon
```

### Sample Output 2

```
21 Jump Street
Mr. Smith Goes To Washington
```


## 📝 Explanation

هر خط از ورودی شامل یک نام فیلم است که باید حروف آن به شکل **Title Case** تبدیل شوند:

* حرف اول هر کلمه بزرگ (uppercase)
* سایر حروف کوچک (lowercase)


## 💡 Hint

در پایتون می‌توانید از متد زیر استفاده کنید:

```python
str.title()
```

## نسخهٔ فارسی (متن اصلی)

محدودیت زمان: ۱ ثانیه
محدودیت حافظه: ۱۲۸ مگابایت

در خط اول عدد `n` (تعداد فیلم‌ها) داده می‌شود و سپس در `n` خط نام فیلم‌ها وارد می‌شوند.
برنامه باید هر نام را طوری اصلاح کند که حرف اول هر کلمه بزرگ و بقیه حروف کوچک باشند.