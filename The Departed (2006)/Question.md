محدودیت زمان: ۱ ثانیه  
محدودیت حافظه: ۲۵۶ مگابایت

Sina and Nima are USVAJAK agents tracking the movements of an unnamed corrupt government official. Anonymous sources have informed them about his upcoming escape attempt. They now know he plans to use his diplomatic contacts to try and hitch a ride on a CIA jet leaving from Jabolgha airport.

It’s well-known that **all CIA jets have the string `FBI` somewhere in their registration codes**. They gathered a list of all jets scheduled for the designated day. There are exactly five jets on the list. Write a program that will find out all CIA jets.

---

## ورودی
There are exactly **5** rows of input, each row representing exactly one jet registration code from the list.  
A registration code is a sequence of at most **10** uppercase English letters, digits `0–9`, or dashes `-`.

---

## خروجی
The only line of output must contain a list of integers, indicating the corresponding input rows containing registrations of **CIA jets**, sorted in increasing order.

If there are **no** CIA jets, output the string:

```

HE GOT AWAY!

```

**Note:** Uppercase and lowercase letters are considered different.

---

## مثال

### ورودی نمونه ۱
```

A-FBI2
9A-IRKOK
RE-KGB3
I-NTERPOL
GM-MI6

```

### خروجی نمونه ۱
```

1

```

---

### ورودی نمونه ۲
```

N323-CIA
F5-B13I
F-BI-32
MPM-DU-CIA
HAKHFSHT

```

### خروجی نمونه ₂
```

HE GOT AWAY!

```

---

### ورودی نمونه ۳
```

45-FBI
BOND-007
DT-FBI14
S1N4-13
N1M4-FBILL

```

### خروجی نمونه ۳
```

1 3 5