def partition(s):
    res = []
    dfs(s, [], res)
    return res


def dfs(s, path, res):

    # base case
    if not s:
        res.append(path)
        return
    for i in range(1, len(s) + 1):
        if is_pal(s[:i]):
            dfs(s[i:], path + [s[:i]], res)


def is_pal(s):
    return s == s[::-1]


string = input()
print(partition(string))



