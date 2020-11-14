def func(A=0,B=0,C=0,a=0,*,b=0,c=0):
	print(A,end=', ')
	print(B,end=', ')
	print(C,end=', ')
	print(a,end=', ')
	print(b,end=', ')
	print(c)

try:
	print('\n\n\nfunc(1,1,1,1,1,1)')
	func(1,1,1,1,1,1)
except TypeError as a:
	print('\nThis is error (ValueError) >> ',end='') 
	print(a)

print('\n\nfunc(1,C=6,b=4)\n')
func(1,C=6,b=4)

print('\nfunc(3,a=6,3)\n')
print('This is error (SyntaxError) >> positional argument follows keyword argument\n')

print('\nfunc(c=2,A=3,C=5)\n')
func(c=2,A=3,C=5)
print('\n\n')