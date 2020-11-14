try:
	a = int(input('>>> '))
	b = int(input('>>> '))
	c = int(input('>>> '))
	print('%d\n%d\n%d' % (a,b,c))
except ValueError:
	print('Error: please enter number!')