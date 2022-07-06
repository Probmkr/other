ways, max_rain = map(int, input().split(' '))
way = [list(map(int, input().split(' '))) for _ in range(ways)]
new_way = [[None for _ in range(ways)] for _ in range(ways)]
for i in range(ways):
    new_way[i] = [way[j][i] for j in range(ways)]
way = new_way
max_way = [sorted(_, reverse=True) for _ in way]
i = 0
able_ways = []
for j in range(ways):
    if max_way[j][0] < max_rain:
        i += 1
        able_ways.append(j+1)
print(' '.join(map(str, able_ways)) if i else 'wait')
