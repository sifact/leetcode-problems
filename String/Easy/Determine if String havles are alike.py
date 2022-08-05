def halvesAreAlike(s):
    vowels = 'aeiouAEIOU'
    a = b = 0
    i, j = 0, len(s) - 1

    while i < j:
        a += s[i] in vowels  # boolean True - 1, False - 0
        b += s[j] in vowels
        i += 1
        j -= 1

    return a == b


string = input()
print(halvesAreAlike(string))
