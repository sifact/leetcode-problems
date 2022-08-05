# naive way:
def toGotLatin(s):

    sentence = s.split(' ')
    vowels = "aeiou"
    for i in range(len(sentence)):
        if sentence[i][0] in vowels:
            sentence[i] += 'ma'
            sentence[i] += (i + 1) * 'a'

        else:
            a = list(sentence[i])
            b = a[0]
            a.remove(a[0])
            a.append(b)
            a += 'ma'
            a += (i + 1) * 'a'

            sentence[i] = "".join(a)

    return " ".join(sentence)


# precise way:
def toGoatLatin(s):
    vowel = set('aeiouAEIOU')

    def latin(w, i):
        if w[0] not in vowel:
            w = w[1:] + w[0]
        return w + 'ma' + 'a' * (i + 1)

    return ' '.join(latin(w, i) for i, w in enumerate(s.split()))


string = input()
print(toGotLatin(string))
