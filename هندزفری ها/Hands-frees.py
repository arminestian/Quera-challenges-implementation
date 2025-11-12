s1, s2 = input().split()
s3, s4 = input().split()

if s1 == s2 or s1 == s4 or s3 == s4 or s3 == s2:
    print("YES")
else:
    print("NO") 