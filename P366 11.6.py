def f(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] += 1


def printM(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = "")
        print()

m = [[0, 0], [0, 1]]
print(len(m))
print(len(m[0]))
printM(m)
f(m)
printM(m)