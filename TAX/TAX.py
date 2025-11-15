incomes = []

while True:
    income = int(input())
    if income == 0:
        break
    incomes.append(income)
    
for i in range(len(incomes)):
    if incomes[i] <= 1000000:
        print(incomes[i])
    elif 1000000 < incomes[i] <= 5000000:
        print(int(0.9 * incomes[i]))
    else:
        print(int(0.8 * incomes[i]))