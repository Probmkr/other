# coding: utf-8
# Your code here!
from os import path

lines = []

print('type "End" to end')
while 1:
	temp = input('> ')
	if (temp == 'End' or temp == 'end'):
		break
	if (temp != ''):
		lines.append(temp.split('/'))
print('read end')

indent = 0

prev = lines[0][0]

for i in lines:
    pathN = '/'.join(i)
    pathD = path.dirname(pathN)
    for j, con in enumerate(pathD.split('/')):
        # print('  '+str(j)) # for test
        # print(prev)        # for test
        try:
            if con != prev[j]:
                print('directory ', ' '*(indent-1), con+'/')
            else:
                pass
        except IndexError:
            print('directory ', ' '*(indent-1), con+'/')
        indent = (j+2)*2
        # print(indent)      # for test
    # print('file      ', ' '*(indent-1), f'{pathN:70}', f'{pathD:30}', prev) # for test
    print('file      ', ' '*(indent-1), i[-1])
    prev = i[:-1]

