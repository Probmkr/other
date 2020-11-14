def Sum(*x):
	SUM = 0
	for X in x:
		SUM += X
	return SUM

def Subt(x,*y):
	X = x
	for Y in y:
		X -= Y
	return X

def Multi(*x):
	MUL = 0
	for X in x:
		MUL += X
	return MUL