def is_between(x, y, z, n):
    if y < z:
        return y < x < z
    else:
        return x > y or x < z

def do_intersect(a, b, c, d, n):
    return (is_between(c, a, b, n) != is_between(d, a, b, n)) and (is_between(a, c, d, n) != is_between(b, c, d, n))

# دریافت ورودی
n = int(input())
a, b = map(int, input().split())
c, d = map(int, input().split())

if do_intersect(a, b, c, d, n):
    print(4)
else:
    print(3)
