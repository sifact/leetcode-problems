# floyd cycle detection algorithm
def digit_square_sum(n):
    s = 0

    while n:
        tmp = n % 10
        s += tmp * tmp
        n //= 10

    return s


def is_happy(n):
    slow, fast = n, digit_square_sum(n)

    while slow != fast:
        slow = digit_square_sum(slow)
        fast = digit_square_sum(digit_square_sum(fast))

    return slow == 1


# using set:
def is_happy2(n):
    seen = set()

    while n not in seen:
        seen.add(n)
        n = sum([int(i) ** 2 for i in str(n)])

    return n == 1


num = int(input())
print(is_happy2(num))

