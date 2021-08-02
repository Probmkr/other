# 二の倍数以外の数を二の倍数以外の数で割る
#
# 2884498

import sys
# maxnum = int(input('enter bigger than 3 > '))
# maxnum = int(sys.argv[1])
maxnum = 10000

count = 0

prime = [2]
if maxnum < 3:
    print('please enter than bigger 3')
    exit()

for i in range(3, maxnum + 1, 2):
    for j in range(3, i, 2):
        count += 1
        if i % j == 0:
            break
    else:
        prime.append(i)

print(prime)
print(count)