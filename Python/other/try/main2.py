while 1:
	try:
		num = int(input('>>> '))
		print(num + 10)
		break
	except ValueError:
		print('enter number')
