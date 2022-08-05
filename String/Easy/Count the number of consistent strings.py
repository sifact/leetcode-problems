# Solution 1:
def countString(allowed, words):
    count = 0

    for word in words:
        count += 1
        for letter in word:
            if letter not in allowed:
                count -= 1
                break
    return count


# solution 2:
def countString2(allowed, words):
    return sum(all(letter in allowed for letter in word) for word in words)


allow = input()
word_s = input().split()
print(countString(allow, word_s))
