# -*- coding: ascii -*-
import os.path as Path
f = open('text.txt','r')
for i in range(Path.getsize(f.name)):
	f.seek(i)
	try:
		cha = f.read(1)
	except UnicodeDecodeError:
		print('n')
	print(cha,end='')
	if cha == ' ':
		print(end=' ')