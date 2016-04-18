def inputNum():
	x = input('input a number:')
	if(x==10):
		raise ValueError,'10 is not a good number'
	return x

inputNum()
