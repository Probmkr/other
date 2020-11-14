import sys
try:
	opt = int(sys.argv[1])
except (ValueError, IndexError):
	print('''please enter number!
option is '1' '2' '3' '4' ''')
	exit()

print('ascii')
if opt >= 3:
	startnum = 0x00
else:
	startnum = 0x20

print()
for i in range(startnum,0x71,0x10):
	print(end = '  ')
	for j in range(0x10):
		if (i + j) == 0x7f and opt == 1:
			continue
		if opt == 4:
			print('%-8s' % repr(chr(i + j)),end = '')
		else:
			print(chr(i + j),end = '  ')
	print()
