def close_primes(x, y):
    
    def is_prime(a):
        if a % a == 0 and a != 0:
            return True
        else:
            return False

    a = int(input("Enter a number: "))
    print(is_prime(a))

print(close_primes(1, 3)) # должно вывести False
print(close_primes(17, 19)) # должно вывести True
print(close_primes(37, 47)) # должно вывести False
print(close_primes(41, 47)) # должно вывести True
print(close_primes(43, 47)) # должно вывести True