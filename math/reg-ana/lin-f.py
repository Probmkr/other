import matplotlib.pyplot as plt

data_x = [1, 2.2, 3.1, 4, 4.7, 6, 7.5, 7.7, 9]
data_y = [4.1, 5, 5.8, 7.7, 7.8, 8.2, 10.5, 10.8, 11.8]

plt.plot(data_x, data_y, ".")
plt.xlim(0, 10)
# plt.ylim(0, 13)
# plt.show()

n = len(data_x)
sum_x = sum(data_x)
sum_y = sum(data_y)
sum_x2 = sum([x**2 for x in data_x])
sum_x_y = sum([data_x[i]*data_y[i] for i in range(n)])
a1 = (sum_x_y) / (sum_x2) -\
    (n * sum_x_y) / (sum_x**2) -\
    (sum_x * sum_y) / (n * sum_x2) +\
    (sum_y) / (sum_x)

a2 = - (sum_x * sum_x_y) / (n * sum_x2) +\
    (sum_x_y) / (sum_x) +\
    (sum_y) / (n) -\
    (sum_x2 * sum_y) / (sum_x**2)

res_x = range(n+1)
res_y = [a1 * x + a2 for x in res_x]

plt.plot(res_x, res_y, "-")
plt.show()