from typing import MutableSequence

def reverse(sequence: MutableSequence) -> MutableSequence:
    n = len(sequence)
    for i in range(n // 2):
        sequence[i], sequence[n - i - 1] = sequence[n - i - 1], sequence[i]

if __name__ == '__main__':
    temp_list = [2, 4, 3, 6, 7]
    print(temp_list)
    reverse(temp_list)
    print(temp_list)