```markdown
محدودیت زمان: ۱ ثانیه  
محدودیت حافظه: ۲۵۶ مگابایت  

Gunnar and Emma play a lot of board games at home, so they own many dice that are not normal 6-sided dice. For example they own a die that has 10 sides with numbers 47, 48, ..., 56 on it.

There has been a big storm in Stockholm, so Gunnar and Emma have been stuck at home without electricity for a couple of hours. They have finished playing all the games they have, so they came up with a new one.

Each player has 2 dice which he or she rolls. The player with a bigger sum wins. If both sums are the same, the game ends in a tie.

Given the description of Gunnar’s and Emma’s dice, which player has higher chances of winning?

All of their dice have the following property: each die contains numbers 
a,a + 1, ..., b, where a and b are the lowest and highest numbers respectively on the die. Each number appears exactly on one side, so the die has b − a + 1 sides.

---

### ورودی
The first line contains four integers a₁, b₁, a₂, b₂ that describe Gunnar’s dice. Dice number i contains numbers aᵢ, aᵢ+1,..., bᵢ on its sides. You may assume that 1 ≤ aᵢ ≤ bᵢ ≤ 100.  
You can further assume that each die has at least four sides, so aᵢ + 3 ≤ bᵢ.

The second line contains the description of Emma’s dice in the same format.

---

### خروجی
Output the name of the player that has higher probability of winning.  
Output `"Tie"` if both players have same probability of winning.

---

### مثال‌ها

#### ورودی نمونه ۱
```

1 4 1 4
1 6 1 6

```
#### خروجی نمونه ۱
```

Emma

```

---

#### ورودی نمونه ۲
```

1 8 1 8
1 10 2 5

```
#### خروجی نمونه ۲
```

Tie

```

---

#### ورودی نمونه ۳
```

2 5 2 7
1 5 2 5

```
#### خروجی نمونه ۳
```

Gunnar

```
```