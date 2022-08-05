# Traverse backwards
# 1. if current char is '#', map prev 2 chars and move ptr 3 chars backward
# 2. Otherwise, map current char and move ptr 1 char backward


def freqAlphabets(s):
    i = len(s) - 1
    ans = ''

    while i >= 0:
        if s[i] == '#':
            ans += alpha(s[i-2:i])
            i -= 3
        else:
            ans += alpha(s[i])
            i -= 1

    return ans[::-1]


# def alpha(num):
    # return chr(int(num) + ord('a') - 1)

def freqAlphabets2(s):
    i, res = 0, ''

    while i < len(s):
        if i + 2 < len(s) and s[i + 2] == '#':
            res += alpha(s[i:i + 2])
            i += 3
        else:
            res += alpha(s[i])
            i += 1

    return res


def alpha(num):
    return chr(int(num) + ord('a') - 1)


string = input()
print(freqAlphabets2(string))
