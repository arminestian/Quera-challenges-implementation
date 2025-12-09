n = int(input())

Sina = {}
Nima = {}

for i in range((2 * n) - 1):

    name = input()
    if i < n:
        if name in Sina:
            Sina[name] += 1
        else:
            Sina[name] = 1
    else:
        if name in Nima:
            Nima[name] += 1
        else:
            Nima[name] = 1

for key, value in Sina.items():
    if key in Nima:
        if Sina[key] != Nima[key]:
            print(key)
            break
    else:
        print(key)
        break