n = int(input())

string = list(input().split())
for i in range(n - 1, -1, -1):
    print(string[i], end = " ")