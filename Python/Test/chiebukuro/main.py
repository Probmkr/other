num = int(input())
if num == 0:
	exit()
pm = num > 0
string = '+' if num else ':'
ten = int(num / 10)
for i in range(ten):
	if(num < 10):
		exit()
	print(string*5 + ' ' + string*5)
if ((num - 10*ten) >= 5):
	print(string*5 + ' ' + string*(num % 5))
else:
	print(string*(num % 5))
