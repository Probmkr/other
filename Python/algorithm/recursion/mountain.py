def layer(max, i = 1):
    if i < max:
        print('*' * i)
        print('*' * layer(max, i + 1))
    elif i == max:
        print('*' * i)
    return i - 1

max = int(input('>> '))
print('\n\n')

layer(max)