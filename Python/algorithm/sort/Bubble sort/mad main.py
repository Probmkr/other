import time
import random as rdm

def swap(swapList, first, second):
    swapList[first], swapList[second] = swapList[second], swapList[first]

# numbers = list(map(int, input().split()))
# numbers = list(reversed(range(40)))
# numbers = list(range(1000))
numbers = []
for i in range(40):
    numbers.append(rdm.randrange(0, 100))
# print(numbers)
lenghth = len(numbers)

for i in range(lenghth - 1):
    for j in range(lenghth - i - 1):
        if numbers[j] > numbers[j + 1]:
            print(f'{numbers[j]:3}, {numbers[j + 1]:3}', end=" ")
            swap(numbers, j, j + 1)
        else:
            print('        ', end=' ')
        print(numbers)
        time.sleep(0.05)

print(numbers)