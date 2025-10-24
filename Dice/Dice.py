a1, b1, a2, b2 = map(int, input().split())
a3, b3, a4, b4 = map(int, input().split())

sum1 = a1 + b1 + a2 + b2
sum2 = a3 + b3 + a4 + b4

if sum1 > sum2:
    print("Gunnar")
elif sum1 <sum2:
    print("Emma")
else:
    print("Tie")