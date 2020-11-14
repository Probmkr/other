#prog1.py
ans = '0'
print("'1' normal\n'2' continue\n'3' break\n")
while 1:
	ans = input(" >> ")
	
	print('P\n')

	if ans == '2':
		continue
	if ans == '3':
		break
	
	print('A\n')
