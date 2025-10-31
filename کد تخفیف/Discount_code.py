n, t = input().split()
n = int(n)
t = set(t)
answers = []
for i in range(n):
    flag = True
    s = set(input())

    if s == t:
        answers.append("Yes")
    else:
        answers.append("No")
        
for i in answers:
    print(i)