def morseCode(words):
    d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
         ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
         "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    return len({''.join(d[ord(letter) - ord('a')] for letter in word) for word in words})


w = input().split()
print(morseCode(w))
