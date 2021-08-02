# 二の倍数以外の数を全ての素数で割る
#
# 766633

import sys
# maxnum = int(input('enter bigger than 3 > '))
# maxnum = int(sys.argv[1])
maxnum = 10000

count = 0

prime = [2]

ptr = 1
if maxnum < 3:
    print('please enter than bigger 3')
    exit()

for i in range(3, maxnum + 1, 2):
    for j in range(1, ptr):
        count += 1
        if i % prime[j] == 0:
            break
    else:
        prime.append(i)
        ptr += 1

print(prime)
print(count)