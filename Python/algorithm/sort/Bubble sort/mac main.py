import time
import random as rdm

def swap(swapList, first, second):
    swapList[first], swapList[second] = swapList[second], swapList[first]

# numbers = list(map(int, input().split()))

# numbers = list(reversed(range(10000)))

# numbers = list(range(1000))

numbers = []
for i in range(10000):
    numbers.append(rdm.randrange(0, 100))

# print(numbers)

print('\n'*30, numbers, '\n'*20)
# time.sleep(3)
# print('\n'*50)

lenghth = len(numbers)

for i in range(lenghth - 1):
    for j in range(lenghth - i - 1):
        if numbers[j] > numbers[j + 1]:
            # print(f'{numbers[j]:3}, {numbers[j + 1]:3}', end=" ")
            # print(numbers)
            swap(numbers, j, j + 1)
        else:
            pass
            # print('        ', end=' ')
        # print(numbers)
        # time.sleep(0.01)

print('\n\n\n\n', numbers)