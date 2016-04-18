def func1(argc1,argc2 = 'world'):
	print argc1,argc2

def func2(argc2='apple',argc1 = 'hello'):
	print argc1,argc2

def func3(argc1,*argc2):
	print argc1,argc2

def func4():
	return 1,2,3
func1('hello')
func2('fuck')
func3('pain','world','peace')
print func4()

a = 10
b = 20
def swap(x,y):
	x,y = y,x
swap(a,b)
print a,b
