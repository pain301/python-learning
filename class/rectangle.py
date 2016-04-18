class Point:
	pass

class Rectangle:
	pass

def findCenter(box):
	p = Point()
	p.x = box.corner.x+box.width/2
	p.y = box.corner.y+box.height/2
	return p

def moveRectangle(box,dx,dy):
	box.corner.x+=dx
	box.corner.y+=dy

def printPoint(p):
	print '(%d,%d)'%(p.x,p.y)

box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 0
box.corner.y = 0
printPoint(findCenter(box))
moveRectangle(box,100,100)
printPoint(findCenter(box))
