n = int(input())

pens = list(map(int, input().split()))
counters = [0] * 101
minimum = 100
pen_number = 0

for i in range(len(pens)):
    counters[pens[i]] += 1

for i in range(len(counters)):
    if counters[i] != 0:
        minimum = min(counters[i], minimum)

for i in range(len(counters) - 1, 0, -1):
    if counters[i] == minimum:
        pen_number = i
        
print(pen_number)