def _isPrime(n, d):
    if d < 2:
        return True
    if n % d == 0:
        return False
    return _isPrime(n, d - 1)


def isPrime(n):
    return _isPrime(n, int(n / 2))


print(isPrime(100))
print(isPrime(99))
print(isPrime(17))
print(isPrime(7))
print(isPrime(3))
print(isPrime(2))
