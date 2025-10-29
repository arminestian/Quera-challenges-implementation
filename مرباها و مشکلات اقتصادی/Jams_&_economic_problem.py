n, k = map(int, input().split())
a = list(map(int, input().split()))

jam = 0
capacity = n * k

for i in a:
    jam += i
capacity -= jam

print(capacity // k)