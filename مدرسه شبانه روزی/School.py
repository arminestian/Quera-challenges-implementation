def find_lcm(num1, num2):
	if(num1>num2):
		num = num1
		den = num2
	else:
		num = num2
		den = num1
	rem = num % den
	while(rem != 0):
		num = den
		den = rem
		rem = num % den
	gcd = den
	lcm = int(int(num1 * num2)/int(gcd))
	return lcm
	
n = int(input())
a = list()
for i in range(n):
    a.append(int(input()))

num1 = a[0]
num2 = a[1]
lcm = find_lcm(num1, num2)

for i in range(2, len(a)):
	lcm = find_lcm(lcm, a[i])
	
print((lcm + 1) % 30)