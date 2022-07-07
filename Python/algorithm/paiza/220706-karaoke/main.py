human, length = map(int, input().split(' '))
model = [int(input()) for _ in range(length)]
humans = [[int(input()) for _ in range(length)] for _ in range(human)]
scores = []
for i in range(human):
    score = 100
    for j in range(length):
        diff = abs(humans[i][j] - int(model[j]))
        if 5 < diff <= 10:
            score -= 1
        elif 10 < diff <= 20:
            score -= 2
        elif 20 < diff <= 30:
            score -= 3
        elif diff > 30:
            score -= 5
    scores.append(score)

print(max(scores) if max(scores) > 0 else 0)
