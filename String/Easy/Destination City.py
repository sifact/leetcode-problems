def desCity(paths):
    return (set([path[1] for path in paths]) - set([path[0] for path in paths])).pop()


p = []
for i in range(int(input())):
    p.append(input().split())
print(desCity(p))
