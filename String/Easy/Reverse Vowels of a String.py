def reverseVowels(s):
    s = list(s)
    vows = 'aeiouAeiou'

    left, r = 0, len(s) - 1

    while left <= r:
        while left <= r and s[left] not in vows:
            left += 1
        while left <= r and s[r] not in vows:
            r -= 1
        if left > r:
            break
        s[left], s[r] = s[r], s[left]
        left, r = left + 1, r - 1
    return ''.join(s)


string = input()
print(reverseVowels(string))
