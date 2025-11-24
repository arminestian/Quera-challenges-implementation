T = int(input())

mylist = list()
for i in range(T):
    mylist.append(int(input()))
    
for i in mylist:
    if i <= 1023:
        print(str(i) + "B")
    elif (1023 < i <= i * 1024) and (i // 1024 < 1024):
        print(str(i // 1024) + "KiB")
    elif 1023< i <= i * 1024 * 1024:
        print(str(i // (1024 * 1024)) + "MiB")