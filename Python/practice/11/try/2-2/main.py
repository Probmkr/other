a = [1,2,1,0,3]
print(a)
for i in a:
	try:
		print(6/i)
	except ZeroDivisionError:
		print('Error')