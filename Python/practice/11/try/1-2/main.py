while 1:
	try:
		num = int(input('enter number > '))
		break
	except ValueError:
		print('Error: please enter number!')
print(num)