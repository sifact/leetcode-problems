# naive way:
def count_bits(num):

    return [bin(i)[2:].count('1') for i in range(num + 1)]


# dynamic programming:

def count_bits2(num):

    dp = [0] * (num + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, num + 1):
        if i % 2 == 0:
            dp[i] = dp[i // 2]
        else:
            dp[i] = dp[i // 2] + 1

    return dp


n = int(input())
print(count_bits2(n))
