
numbers = list(map(int, input().split(' ')))

def swap(swapList, index1, index2):
    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

for j in range(len(numbers) - 1):
    if numbers[j] > numbers[j + 1]:
        swap(numbers, j, j + 1)

print(numbers)