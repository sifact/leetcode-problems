def Check(word1, word2):
    str1, str2 = '', ''

    for word in word1:
        str1 += word
    for word in word2:
        str2 += word

    return str1 == str2


w1, w2 = input(), input()
print(Check(w1, w2))
