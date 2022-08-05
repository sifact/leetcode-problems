def is_ugly2(n):
    if n > 0:
        for i in range(2, 6):
            while n % i == 0:
                n //= i

    return n == 1


num = int(input())
print(is_ugly2(num))


def is_ugly(n):
    if n > 0:

        while n % 2 == 0:
            n //= 2

        for i in range(3, int(n ** 0.5) + 1, 2):

            while n % i == 0:
                n //= i
                if i > 5:
                    return False

        if n > 5:
            return False

        return True
