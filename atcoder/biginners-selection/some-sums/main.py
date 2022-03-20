n, a, b = map(int, input().split())
res = []
for i in range(1, n+1):
    if a <= sum(map(int, list(str(i)))) <= b:
        res.append(i)

print(sum(res))