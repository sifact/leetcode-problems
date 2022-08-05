def judgeCircle(s):

    res1, res2 = 0, 0

    for i in s:
        if i == 'L':
            res1 += -1
        if i == 'R':
            res1 += 1
        if i == 'U':
            res2 += 2
        if i == 'D':
            res2 += -2

    return res2 == res1 == 0


string = input()
print(judgeCircle(string))
