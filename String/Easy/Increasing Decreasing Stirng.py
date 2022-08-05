from collections import Counter


def sortString(s):
    cnt, ans, asc = Counter(s), [], True

    while cnt:
        for c in sorted(cnt.keys()) if asc else reversed(sorted(cnt.keys())):
            ans.append(c)
            cnt[c] -= 1
            if cnt[c] == 0:
                del cnt[c]

        asc = not asc
    return ''.join(ans)


string = input()
print(sortString(string))
