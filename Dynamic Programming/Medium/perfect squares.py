def num_squares(n):
    dp = [0] + [float('inf')] * n

    for i in range(1, n + 1):
        dp[i] = min(dp[i - j * j] for j in range(1, int(i ** 0.5) + 1)) + 1

    return dp[n]


def num_square(n):
    dp = [0] + [float('inf')] * n

    for i in range(1, n + 1):
        for j in range(1, int(i ** 0.5) + 1):
            curr = dp[i - j * j] + 1
            dp[i] = min(curr, dp[i])

    return dp[-1]


num = int(input())
print(num_square(num))
