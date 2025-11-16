corners = []
x = []
y = []
z = []

for i in range(7):
    corners.append(list(map(int, input().split())))

for i in range(7):
    for j in range(3):
        if j == 0:
            x.append(corners[i][j])
        elif j == 1:
            y.append(corners[i][j])
        elif j == 2:
            z.append(corners[i][j])

x_prime = list(set(x.copy()))
y_prime = list(set(y.copy()))
z_prime = list(set(z.copy()))

if x.count(x_prime[0]) < x.count(x_prime[1]):
    x_point = x_prime[0]
else:
    x_point = x_prime[1]
if y.count(y_prime[0]) < y.count(y_prime[1]):
    y_point = y_prime[0]
else:
    y_point = y_prime[1]
if z.count(z_prime[0]) < z.count(z_prime[1]):
    z_point = z_prime[0]
else:
    z_point = z_prime[1]
    
print(x_point, y_point, z_point)