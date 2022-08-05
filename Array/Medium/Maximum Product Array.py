def maxProduct(nums):
    mini, maxi, res = 1, 1, nums[0]

    for n in nums:
        a = mini * n

        b = maxi * n

        mini = min(a, b, n)

        maxi = max(a, b, n)

        res = max(res, maxi)

    return res

# 1 -3


def max_product(nums):

    dp = [0] * len(nums)

    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] * nums[i], nums[i])

    return max(dp)


array = list(map(int, input().split()))
print(maxProduct(array))
