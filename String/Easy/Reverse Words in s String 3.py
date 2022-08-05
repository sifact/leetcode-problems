def reverseString(s):
    tmp = s.split()
    res = []

    for i in range(len(tmp)):
        res.append(tmp[i][::-1])

    return " ".join(res)


string = input()
print(reverseString(string))
