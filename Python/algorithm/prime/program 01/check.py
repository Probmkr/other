import sys
# num = int(input('enter bigger than 3 > '))
# num = int(sys.argv[1])
num = 99989

count = 0

if num < 3:
    print('please enter than bigger 3')
    exit()

isPrime = True
for i in range(2, num):
    count += 1
    if num % i == 0:
        isPrime = False
        break

print(isPrime, count)