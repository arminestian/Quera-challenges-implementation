t = int(input())

answers = []

for i in range(t):
    a, b, c, d = map(int, input().split())
    if a + c > b + d:
        answers.append("perspolis")
    elif a + c < b + d:
        answers.append("esteghlal")
    else:
        if a < d:
            answers.append("perspolis")
        elif a > d:
            answers.append("esteghlal")
        else:
            answers.append("penalty")
            
for i in answers:
    print(i)