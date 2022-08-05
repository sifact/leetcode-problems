s = "I am sifat, I am from Mymensingh"
n = len(s)

while n > 1:
    n = int(n / 2)

    print(s[:n])
    s = s[n:]
    n = len(s)

print(s)


