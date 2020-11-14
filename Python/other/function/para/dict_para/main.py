def func(a,*b,**c):
	print(1)				# 1
	print(a)
	if b:
		print(2)			# 2
		pr = ', '.join(b)
		print(pr)
	if c:
		print(3)			# 3
		j = []
		for i in c:
			j.append('{}:{}'.format(i,c[i]))
		pr = ', '.join(j)
		print(pr)


func('ccc','dfw','DFW','gsg','hjhh',ff='gg',FF='GG',nn='vssss',s=3)