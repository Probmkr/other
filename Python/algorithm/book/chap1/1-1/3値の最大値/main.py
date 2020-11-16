def MyMax(x: int, y: int, z: int) -> int:
    max_value = x
    if y > max_value:
        max_value = y
    if z > max_value:
        max_value = z

    return max_value


# a = input('first  : ')
# b = input('second : ')
# c = input('third  : ')

# print(f'maxim value is {MyMax(a, b, c)}')
if __name__ == '__main__':
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                print(f'{i} {j} {k} -> {MyMax(i, j, k)}')
