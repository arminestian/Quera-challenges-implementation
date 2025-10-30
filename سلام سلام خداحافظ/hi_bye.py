n = int(input())
people = list(input().split())

for i in range(1, len(people)):
    for j in range(i - 1, -1, -1):
        print("%s: salam %s!" % (people[i], people[j]))
        
for i in range(len(people)):
    print("%s: khodafez bacheha!" % people[i])
    for j in range(i + 1, len(people)):
        print("%s: khodafez %s!" % (people[j], people[i]))