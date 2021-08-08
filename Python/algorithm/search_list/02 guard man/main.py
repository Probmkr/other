from typing import Sequence, Any, Union
import copy


def search(seq: Sequence, key: Any) -> Union[int, bool]:
    i = 0
    seq = copy.deepcopy(seq)

    seq.append(key)

    while True:
        if seq[i] == key:
            return False if i == len(seq) else i
        i += 1


if __name__ == '__main__':
    seq = [3, 6, 4, 5, 5, 2, 1, 3, 4, 80, 3, 4, 5, 45, 8]
    index = search(seq, 80)
    print(index)
    if index >= 0:
        print(f'seq[{index}] = {seq[index]}')


