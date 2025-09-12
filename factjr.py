import time
import math


def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(limit + 1) if sieve[i]]


def build_wheel(basis):
    if not basis:
        return []

    wheel_size = 1
    for p in basis:
        wheel_size *= p

    wheel = []
    for num in range(1, wheel_size + 1):
        if all(num % p != 0 for p in basis):
            wheel.append(num)

    wheel.append(wheel[0] + wheel_size)

    increments = [wheel[i] - wheel[i - 1] for i in range(1, len(wheel))]
    return increments


def is_prime(n, basis):
    if n < 2:
        return False

    for p in basis:
        if n % p == 0:
            return n == p

    if not basis:
        max_divisor = math.isqrt(n)
        primes = sieve_of_eratosthenes(max_divisor)
        for p in primes:
            if n % p == 0:
                return n == p
        return True

    max_divisor = math.isqrt(n)
    primes = sieve_of_eratosthenes(max_divisor)

    wheel_primes = [p for p in primes if p > basis[-1]] if basis else primes

    increments = build_wheel(basis)
    if not increments:
        for p in wheel_primes:
            if n % p == 0:
                return False
        return True

    i = 0
    len_increments = len(increments)
    k = basis[-1] if basis else 2

    while k <= max_divisor:
        if k in wheel_primes and n % k == 0:
            return False
        k += increments[i]
        i = (i + 1) % len_increments

    return True


def test_large_numbers(basis, numbers_to_test):
    print(f"\nТестирование с базой {basis}:")
    for num in numbers_to_test:
        start_time = time.time()
        prime = is_prime(num, basis)
        duration = time.time() - start_time
        print(f"{num}: {'Простое' if prime else 'Составное'}, время: {duration:.6f} сек")


bases = [
    [],
    [2],
    [2, 3],
    [2, 3, 5],
    [2, 3, 5, 7],
    [2, 3, 5, 7, 11],
    [2, 3, 5, 7, 11, 13],
    [2, 3, 5, 7, 11, 13, 17]
]

test_numbers = [
    1000000007,
    1000000009,
    2147483647
]

for basis in bases:
    test_large_numbers(basis, test_numbers)