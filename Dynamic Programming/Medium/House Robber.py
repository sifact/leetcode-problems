def rob(nums):
    n = len(nums)

    if n == 1:
        return nums[0]

    dp = [0] * n

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[-1]


num = list(map(int, input().split()))
print(rob(num))


# two variables:
def rob1(nums):
    def simple_rob1(x):
        last, now = 0, 0

        for i in x:
            last, now = now, max(last + i, now)
        return now

    return max(simple_rob1(nums[1:]), simple_rob1(nums[:-1]))


# num = list(map(int, input().split()))
# print(rob1(num))
