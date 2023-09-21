n = 1000000007
counter = 0
for i in range(2,(n+1)//2):
    if n % i == 0:
        counter += 1
if counter == 1:
    print(f'{n} число простое')
else:
    print(f'{n} число непростое')