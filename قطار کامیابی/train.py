k, a, b = map(int, input().split())
first_a = a
first_b = b

if a % k == 0 and b % k == 0:
    timer = abs(a - b) // k
else:
    distance_a = min(a % k, k - (a % k))
    distance_b = min(b % k, k - (b % k))
    
    if distance_a == a % k:
        a -= a % k
    else:
        a += k - (a % k)
    
    if distance_b == b % k:
        b -= b % k
    else:
        b += k - (b % k)
    timer = (distance_a + distance_b + abs(a - b) // k)
    
if (abs(first_a - first_b) < (distance_a + distance_b)):
    timer = abs(first_a - first_b)
    
print(timer)