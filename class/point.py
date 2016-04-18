import math

class Point:
	def __init__(self,x = 0,y = 0):
		self.x = x	
		self.y = y
	def __str__(self):
		return '('+str(self.x)+','+str(self.y)+')'
	def __add__(self,other):
		return Point(self.x+other.x,self.y+other.y)
	def __mul__(self,other):
		return Point(self.x*other.x,self.y*other.y)
	def __rmul__(self,other):
		return Point(other*self.x,other*self.y)
	pass

def samePoint(p1,p2):
	return (p1.x==p2.x) and (p1.y==p2.y)

blank =  Point()
blank.x = 3.0
blank.y = 4.0

print blank

p1 = Point(y = 4)
p2 = Point(y = 4)
print p1 is p2
print samePoint(p1,p2)

print p1+p2
print p1*p2
print 3*p1
