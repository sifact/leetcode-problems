from itertools import combinations_with_replacement


# Backtracking/dfs:
def combinationSums(candidates, tar):
    def backTr(target, curr_sol, k):
        if target == 0:
            sol.append(curr_sol)

        if target < 0 or k >= len(candidates):
            return

        for i in range(k, len(candidates)):

            backTr(target - candidates[i], curr_sol + [candidates[i]], i)

    sol = []
    backTr(tar, [], 0)
    return sol


# Brute-force approach:
def combinationSum(nums, target):
    min_num = min(nums)
    ans = []
    for i in range(target // min_num):
        for comb in combinations_with_replacement(nums, i + 1):
            if sum(comb) == target:
                ans.append(comb)
    return ans


# my attempt (:
def combination_sum(nums, target):
    nums.insert(0, 0)
    res = []
    dfs(nums, target, [], res)
    return res


def dfs(nums, target, path, res):
    if target < 0:
        return
    if target == 0:
        if sorted(path) not in res:
            res.append(sorted(path))
        return

    for i in range(1, len(nums)):
        dfs(nums[i:], target - nums[i], path + [nums[i]], res)


def combination_sum2(nums, target):

    res = []
    dfs(sorted(nums), target, 0, [], res)
    return res


def dfs(nums, target, idx, path, res):
    if target <= 0:
        if target == 0:
            res.append(path)
        return

    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i - 1]:
            continue
        dfs(nums, target - nums[i], i + 1, path + [nums[i]], res)


a = list(map(int, input().split()))
n = int(input())
print(combination_sum2(a, n))
