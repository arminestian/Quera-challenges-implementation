محدودیت زمان: ۱ ثانیه  
محدودیت حافظه: ۲۵۶ مگابایت  

Several balloons are arranged sequentially, each showing one of the letters from **a** to **z**. Amin wants to give a needle to Niloufar and ask her to select one or more balloons so that after popping them and joining the remaining balloons (without changing their order), he can reach a state where exactly **4** balloons remain in sequence, with the letters **acpc** written on them in order.

You need to write a program that, given the initial arrangement of balloons, determines whether this is possible or not.

---

## ورودی
The first line of input contains a positive integer **t**, representing the number of test cases.

```

1 ≤ t ≤ 10^4

```

In each test case, there is a single string **s**, consisting of lowercase English letters, showing the sequence of letters written on the balloons.

```

1 ≤ |s| ≤ 100

```

---

## خروجی
For each test case, print **YES** if it is possible to form the word `acpc`; otherwise, print **NO**.

---

## مثال‌ها

### ورودی نمونه ۱
```

2
amirkabirprogrammingcontest
amirkabircollegiateprogramcontest

```

### خروجی نمونه ۱
```

NO
YES
