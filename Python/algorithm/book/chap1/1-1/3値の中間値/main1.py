def MyMid(a, b, c):
    if a >= b:
        # print('a >= b true')
        if b >= c:
            # print('b >= c true')
            return b
        elif a <= c:
            # print('a <= c true')
            return a
        else:
            # print('else')
            return c
    elif a > c:
        # print('a > c true')
        return a
    elif b > c:
        # print('b > c true')
        return c
    else:
        # print('else')
        return b
    

 
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            print(f'{i} {j} {k} -> {MyMid(i, j, k)}')
    