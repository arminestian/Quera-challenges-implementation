number = int(input())

numbers = [0] * number
numbers = input().split()

for i in range(number):
    if (int(numbers[i]) > 15):
        print("cooler")
    else:
        print("heater")
