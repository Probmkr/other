def move(no: int, x: int, y: int) -> None:
    if no > 1:
        tno, tx, ty = no - 1, x, 6 - x - y
        print("'1'\n", tno, tx, ty)
        move(tno, tx, ty)

    print("'2'")
    print(f'円盤[{no}]を{x}軸から{y}軸へ移動')

    if no > 1:
        tno, tx, ty = no - 1, 6 - x - y, y
        print("'1'\n", tno, tx, ty)
        move(tno, tx, ty)

n = int(input('円盤の数 > '))

move(n, 1, 3)