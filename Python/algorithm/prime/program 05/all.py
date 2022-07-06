# 二の倍数以外の数を自身の平方数より小さいの素数で割る
#
# 78736

import sys
#maxnum = 10000
#maxnum = int(input('enter bigger than 3 > '))
maxnum = int(sys.argv[1])

count = 0
allcount = 0

prime = [2]

if maxnum < 3:
    print('please enter than bigger 3')
    exit()

for i in range(3, maxnum + 1, 2):
    j = 0
    while prime[j]**2 <= i:
        count += 2
        if i % prime[j] == 0:
            break
        j += 1
    else:
        prime.append(i)
        count += 1
        allcount += 1

print(prime)
print(count)
print(allcount)
