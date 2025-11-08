cameras = []

for i in range(3):
    cameras.append(list(map(int, input().split())))

x = 0
y = 0

if cameras[0][0] == cameras[1][0]:
    x = cameras[2][0]
elif cameras[0][0] == cameras[2][0]:
    x = cameras[1][0]
elif cameras[1][0] == cameras[2][0]:
    x = cameras[0][0]
if cameras[0][1] == cameras[1][1]:
    y = cameras[2][1]
elif cameras[0][1] == cameras[2][1]:
    y = cameras[1][1]
elif cameras[1][1] == cameras[2][1]:
    y = cameras[0][1]
    
print(x, y)