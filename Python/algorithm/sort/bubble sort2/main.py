import time
import random as rdm


def swap(swapList, first, second):
    swapList[first], swapList[second] = swapList[second], swapList[first]

count = 0

# numbers = list(map(int, input().split()))

# numbers = list(reversed(range(50)))

# numbers = list(range(1000))

numbers = []
# for i in range(40):
#     numbers.append(rdm.randrange(0, 100))

numbers = [4, 5, 3, 7, 43, 5, 2, 4, 3 ,354, 62, 3, 2, 345, 32, 1234, 123, 4, 12, 24 ,123, 234]

# print(numbers)

print('\n'*30, numbers, '\n'*20)
# time.sleep(3)
# print('\n'*50)

lenghth = len(numbers)

for i in range(lenghth - 1):
    exchng = 0
    for j in range(lenghth - i - 1):
        if numbers[j] > numbers[j + 1]:
            print(f'{numbers[j]:4}, {numbers[j + 1]:4}', end=" ")
            # print(numbers)
            swap(numbers, j, j + 1)
            exchng += 1
        else:
            pass
            print('          ', end=' ')
        print(numbers)
        time.sleep(0.01)
        count += 1
    if exchng == 0:
        break

print('\n\n\n\n', numbers)
print(count)