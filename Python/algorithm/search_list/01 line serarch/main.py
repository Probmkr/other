from typing import Sequence, Any, Union


def search(arr: Sequence, key: Any) -> Union[int, bool]:
    i = 0

    while True:
        if i == len(arr):
            return -1
        if arr[i] == key:
            return i
        i += 1


if __name__ == '__main__':
    arr = [3, 6, 4, 5, 5, 2, 1, 3, 4, 80, 3, 4, 5, 45, 8]
    index = search(arr, 80)
    print(index)
    if index >= 0:
        print(f'arr[{index}] = {arr[index]}')


