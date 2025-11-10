chocolates = list(map(int, input().split()))

dict_eaten = {
    0 : 0,
    1 : 0,
    2 : 0,
    3 : 0
}

i = 0
while (0 not in chocolates):
    dict_eaten[i % 4] += 1
    chocolates[i % 4] -= 1
    temp = chocolates[0]
    chocolates.remove(temp)
    chocolates.append(temp)
    i += 1

print(dict_eaten[0], dict_eaten[1], dict_eaten[2], dict_eaten[3])
