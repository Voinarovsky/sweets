a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sum_1 = sum(a[0:5])
sum_2 = sum(a[5:])

def com():
    global b
    b = [b[i] + a[i] for i in range(10)]
    print(b)

if sum_1 * sum_2 > 100:
    com()

if sum_1 * sum_2 < 10000:
    com()

if sum_2 * sum_2 > 1000:
    com()