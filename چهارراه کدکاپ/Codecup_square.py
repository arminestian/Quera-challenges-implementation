t = int(input())

answers = list()

for i in range(t):
    m, n = map(int, input().split())
    if m == n:
        answers.append(n + 1)
    else:
        answers.append(max(m, n))
        
for i in answers:
    print(i)