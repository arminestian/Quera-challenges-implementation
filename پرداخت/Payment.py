t = int(input())

answers = list()

for i in range(t):
    n = int(input())
    letters = [[0 for i in range(26)] for j in range(n)]
    for j in range(n):
        S = input()
        for k in range(len(S)):
            letters[j][ord(S[k]) % 97] += 1
            
    ans = 0
    for j in range(26):
        temp = 0
        for k in range(len(letters)):
            temp = max(temp, letters[k][j])
        ans += temp
    answers.append(ans)

for i in answers:
    print(i)