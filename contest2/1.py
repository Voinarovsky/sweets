a, b = map(int, input().split())
s = [for i in range(10001)]
if b>a:
    s = s[(a+1):b]
    s = s[0]
    print(s)
elif b<a:
    s = s[(b+1):a]
    n = s[0]
    print(n)
else:
    print(-1)