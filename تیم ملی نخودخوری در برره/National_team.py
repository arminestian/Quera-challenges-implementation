a, b, c = map(int, input().split())
Farhad = list(map(int, input().split()))
Sahar = list(map(int, input().split()))
Shadooneh = list(map(int, input().split()))

people = []
start = min(Farhad[0], Sahar[0], Shadooneh[0])
end = max(Farhad[1], Sahar[1], Shadooneh[1])
cost = 0

for i in range(start, end):
    if i == Farhad[0]:
        people.append("Farhad")
    if i == Sahar[0]:
        people.append("Sahar")
    if i == Shadooneh[0]:
        people.append("Shadooneh")
    if i == Farhad[1]:
        people.remove("Farhad")
    if i == Sahar[1]:
        people.remove("Sahar")
    if i == Shadooneh[1]:
        people.remove("Shadooneh")
    if len(people) == 1:
        cost += a
    elif len(people) == 2:
        cost += 2 * b
    elif len(people) == 3:
        cost += 3 * c
        
print(cost)