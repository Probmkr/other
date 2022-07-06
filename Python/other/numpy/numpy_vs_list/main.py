import numpy as np
import time
N = 100
a_list = [[1] * N for i in range(N)]
b_list = [[2] * N for i in range(N)]
c_list = [[0] * N for i in range(N)]
a_numpy = np.array(a_list)
b_numpy = np.array(b_list)

# list
start = time.time()
for i in range(N):
    for j in range(N):
        for k in range(N):
            c_list[i][j] += a_list[i][k] * b_list[k][j]

end = time.time() - start
print(c_list)
input()
print(f"list {end} seconds")
input()

#NumPy
start = time.time()
c_numpy = np.dot(a_numpy, b_numpy)
end = time.time() - start
print(c_numpy)
input()
print(f"NumPy {end} seconds")
