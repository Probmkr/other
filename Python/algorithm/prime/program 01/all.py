# 全ての数を全ての数で割る
#
# 5775223

import sys
# maxnum = int(input('enter bigger than 3 > '))
# maxnum = int(sys.argv[1])
maxnum = 10000

count = 0

prime = [2]
if maxnum < 3:
    print('please enter than bigger 3')
    exit()

for i in range(3, maxnum + 1):
    for j in range(2, i):
        count += 1
        if i % j == 0:
            break
    else:
        prime.append(i)

print(prime)
print(count)