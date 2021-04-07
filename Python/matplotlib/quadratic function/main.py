from matplotlib import pyplot

x = [i for i in range(-100, 101)]
y = [i**2 for i in range(-100, 101)]

pyplot.plot(x, y)
pyplot.plot([0, 0], [-1000, 11000], color='black', linestyle='dashed')
pyplot.plot([-150, 150], [0, 0], color='black', linestyle='dashed')

pyplot.show()