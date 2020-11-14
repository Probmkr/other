# main.py
import random as rnd
import datetime

i = 0
numberX = rnd.randint(1,100)
ans = ''
print("\nlet's guess numberX (1~100)\n")
while 1:
	i += 1
	try:
		ans = int(input('enter number >> '))
	except ValueError:
		print("\nplease enter 'number'\n")
		continue
	
	if(ans == numberX):
		break
	elif(ans < numberX):
		print('numberX is more biger\n')
	elif(ans > numberX):
		print('numberX is more smaller\n')

print('\nCongratulation! numberX is %d\n\n\n' % numberX)
print('you tryed %d time\n' % i)
rank = ''
if(i <= 2):
	rank = 'S'
elif(i <= 4):
	rank = 'A'
elif(i <= 6):
	rank = 'B'
elif(i <= 10):
	rank = 'C'
else:
	rank = 'Z'

print('rank %s' % rank)

with open('SaveData.txt','a') as f:
	f.writelines(str(datetime.date.today()) + ': ' + rank + ' ' + str(i) + ' ')