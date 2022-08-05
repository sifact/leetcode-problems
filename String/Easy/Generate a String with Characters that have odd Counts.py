def generateTheString(num):
    if num % 2 == 0:
        return 'a' * (num - 1) + 'b'
    return 'a' * num


n = int(input())
print(generateTheString(n))
