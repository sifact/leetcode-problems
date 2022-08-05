def rob(nums):
    def simple_rob(x):

        dp = [0] * len(x)

        dp[0] = x[0]
        dp[1] = max(x[0], x[1])

        for i in range(2, len(x)):
            dp[i] = max(dp[i - 2] + x[i], dp[i - 1])
        return dp[-1]

    if len(nums) == 1:
        return nums[0]

    return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))


num = list(map(int, input().split()))
print(rob(num))