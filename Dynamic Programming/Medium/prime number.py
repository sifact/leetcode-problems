import math


def count_primes(n):
    if n < 3:
        return 0
    primes = [1] * n
    primes[0] = primes[1] = 0

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [0] * len(primes[i * i:n:i])

    return primes


# num = int(input())
# print(count_primes(num))


def count_prime_factor(n):

    # print the number of two's that evenly divisible by 2
    while n % 2 == 0:
        print(2)
        n //= 2

    # n must be odd at this point
    # so a skip of 2 (i += 2) can be used

    for i in range(3, int(math.sqrt(n)), 2):

        while n % i == 0:
            print(i)
            n = n // i

    # if n is a prime number greater than 2
    if n > 2:
        print(n)


num = int(input())
count_prime_factor(num)

