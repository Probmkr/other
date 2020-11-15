def layer(max, i = 1):
    if i < max:
        print('*' * i)
        print('*' * layer(max, i + 1))
    elif i == max:
        print('*' * i)
    return i - 1

def layer_not_recursion(max, i = 1):
    for j in range(i, max + 1):
        print('*' * j)
    for j in reversed(range(i, max)):
        print('*' * j)

if __name__=='__main__':

    max = int(input('>> '))
    try:
        i = int(input('>> '))
    except ValueError:
        i = 1
    print('\n\n')

    layer(max, i)