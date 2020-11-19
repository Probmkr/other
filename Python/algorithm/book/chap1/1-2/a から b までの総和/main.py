a = int(input('a : '))
b = int(input('b : '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    sum += i

print(sum)
