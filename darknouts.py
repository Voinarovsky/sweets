a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if (sum(a[0 : 4]) * (sum(b[0:4])) )> 100:
    for i in range(10):
        b[i] += a[i]
    print(b)
if (a[0] + a[1] + a[2] + a[3] + a[4]) * (a[5] + a[6] + a[7] + a[8] + a[9]) < 10000:
    print(b)
    for i in range(10):
        b[i] += a[i]
    print(b)
if (a[5] + a[6] + a[7] + a[8] + a[9]) * (a[5] + a[6] + a[7] + a[8] + a[9]) > 1000:
    for i in range(10):
        b[i] += a[i]
print(b)