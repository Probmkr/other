from typing import Any, Sequence, Union

def search(seq: Sequence, key: Any) -> Union[int, bool]:
    ps = 0
    pl = len(seq) - 1

    while True:
        pc = (ps + pl) // 2
        if seq[pc] == key:
            return pc
        elif seq[pc] < key:
            ps = pc + 1
        else:
            pl = pc - 1
        if ps > pl:
            break
    return False

if __name__ == "__main__":
    seq = [3, 55, 34,6 ,34, 23452345, 345, 2345, 23452, 45234, 234, 3, 4, 3, 334, 3324, 33, 3, 8, 567, 378]
    seq.sort()
    index = search(seq, 334)
    print(index)
    print(seq[index])

