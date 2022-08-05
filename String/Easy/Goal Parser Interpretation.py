def goal_parser(str):
    d = {'G': 'G', '()': 'o', '(al)': 'al'}

    tmp = ''
    res = ''
    for j in range(len(str)):
        tmp += str[j]
        if tmp in d:
            res += d[tmp]
            tmp = ''

    return res


string = input()
print(goal_parser(string))

