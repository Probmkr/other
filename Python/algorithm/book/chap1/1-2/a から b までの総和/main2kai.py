a = 1#int(input('a : '))
b = 5000000#int(input('b : '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

sum += b
print(f'{b} = {sum}')

print(sum)
