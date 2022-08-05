def sub_array(nums, k):
    dic = {0: -1}
    s = 0

    for i, n in enumerate(nums):
        if k != 0:
            s = (s + n) % k
        else:
            s += n
        if s not in dic:
            dic[s] = i
        else:
            if i - dic[s] >= 2:
                return True

    return False


array, K = list(map(int, input().split())), int(input())
print(sub_array(array, K))

