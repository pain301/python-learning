import copy

class Point:
	pass

def samePoint(p1,p2):
	return (p1.x==p2.x) and (p1.y==p2.y)

def printPoint(p):
	print '(%d,%d)'%(p.x,p.y)

class Rect:
	pass

def findCenter(box):
	p = Point()
	p.x = box.corner.x + box.width/2
	p.y = box.corner.y + box.height/2
	return p

def growRect(box,dw,dh):
	box.width+=dw
	box.height+=dh

def moveRect(box,dx,dy):
	box.corner.x+=dx
	box.corner.y+=dy

def printRect(box):
	p = Point()
	p = findCenter(box)
	print 'box center:'
	printPoint(p)
	print 'width:%d,height:%d'%(box.width,box.height)
	
p1 = Point()
p1.x = 3
p1.y = 4
p2 = copy.copy(p1)
print p1==p2
print samePoint(p1,p2)

box = Rect()
box.width = 100
box.height = 50
box.corner = Point()
box.corner.x = 0
box.corner.y = 0
print 'box:'
printRect(box)
tmp = copy.deepcopy(box) #copy.copy(box) tmp = box
growRect(tmp,100,100)
print 'box:'
printRect(box)
print 'tmp:'
printRect(tmp)

print '--------------------'
moveRect(tmp,100,100)
print 'box:'
printRect(box)
print 'tmp:'
printRect(tmp)
