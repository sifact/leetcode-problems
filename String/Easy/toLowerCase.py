def toLowerCase(string):
    return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90
                   else c for c in string)


s = input()
print(toLowerCase(s))
