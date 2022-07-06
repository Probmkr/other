import time
import numpy as np
import math

start = 0x20
end = 0x7f
length = 5

dictlist = ['']*sum([math.factorial(i) for i in range(1, length+1)])*(end - start)

for i in range(length):
    for j in range(math.factorial(length - i)):
        pass
        # temp_char =


print(len(dictlist))

# for i in dictlist:
#     print(i)
