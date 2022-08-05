def longest_palindrome(s):
    res = []

    for i in range(len(s)):
        # odd ase, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) >= 1:
            res.append(tmp)

        # if len(tmp) > len(res):
        #     res = tmp

        # even case, like "abba"
        tmp = helper(s, i, i + 1)
        if len(tmp) >= 1:
            res.append(tmp)

        # if len(tmp) > len(res):
        #     res = tmp

    return res


def helper(s, left, r):
    while left >= 0 and r < len(s) and s[left] == s[r]:
        left -= 1
        r += 1

    return s[left + 1:r]


# string = input()
# print(longest_palindrome(string))


# dp
def longest_palindrome2(s):
    ans = ''
    max_len = 0
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True
        max_len = 1
        ans = s[i]

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            ans = s[i:i + 2]
            max_len = 2

    for j in range(n):
        for i in range(0, j - 1):
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if max_len < j - i + 1:
                    ans = s[i:j + 1]
                    max_len = j - i + 1

    return ans


string = input()
print(longest_palindrome(string))



