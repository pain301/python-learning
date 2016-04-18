a = 'apple'
b = 'apple'
print id(a)
print id(b)
a = [1,2,3]
b = [1,2,3]
print id(a)
print id(b)
b = a
print id(a)
print id(b)
b[1] = 200
print a,b
