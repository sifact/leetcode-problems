def sub_string(str1, str2):

    if len(str2) == 0:
        return True
    if len(str1) == 0:
        return False
    i, j = 0, 0
    while i < len(str2) and j < len(str1):
        if str2[i] == str1[j]:
            i += 1
        j += 1
    return True if i == len(str2) else False


s1, s2 = input(), input()
print(sub_string(s1, s2))

