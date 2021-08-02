a = [
    ["あ"]*5
]*10

for i in a:
    for j in i:
        print(j, end="")
    print()

b = [[None]*len(a)]*len(a[0])

for i in range(len(a)):
    for j in range(len(a[0])):
        b[j][i] = a[i][j]

for i in b:
    for j in i:
        print(j, end="")
    print()