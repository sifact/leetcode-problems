def word_break(s, word_dict):

    n = len(s)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for w in word_dict:
            if dp[i - len(w)] and s[i - len(w):i] == w:
                dp[i] = True

    return dp[-1]


string = input()
word_dict = input().split()

print(word_break(string, word_dict))
