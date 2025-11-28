n = int(input())
s = input()

#Keyvan Nezam Shirfarhad
people = [0, 0, 0]

for i in range(n):
    if (i % 6 == 0 or i % 6 == 1) and int(s[i]) == 3:
        people[0] += 1
    if (i % 6 == 2 or i % 6 == 3) and int(s[i]) == 1:
        people[0] += 1
    if (i % 6 == 4 or i % 6 == 5) and int(s[i]) == 2:
        people[0] += 1
    if i % 3 == 0 and int(s[i]) == 1:
        people[1] += 1
    if i % 3 == 1 and int(s[i]) == 2:
        people[1] += 1
    if i % 3 == 2 and int(s[i]) == 3:
        people[1] += 1
    if (i % 4 == 0 or i % 4 == 2) and int(s[i]) == 2:
        people[2] += 1
    if i % 4 == 1 and int(s[i]) == 1:
        people[2] += 1
    if i % 4 == 3 and int(s[i]) == 3:
        people[2] += 1
        
if True:
    print(max(people))
    if max(people) == people[0]:
        print("keyvoon")
    if max(people) == people[1]:
        print("nezam")
    if max(people) == people[2]:
        print("shir farhad")