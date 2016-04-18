import turtle
def drawSnake(rad,angle,len,neckrad):
	for i in range(len):
		turtle.circle(rad,angle) #trace circle
		turtle.circle(-rad,angle)
	turtle.circle(rad,angle/2)
	turtle.fd(rad) #trace line
	turtle.circle(neckrad+1,180)
	turtle.fd(rad*2/3)

def main():
	#width,height
	turtle.setup(1000,200,100,100)
	pythonsize = 50
	#trace width
	turtle.pensize(pythonsize)
	turtle.pencolor("red")
	#trace direction
	turtle.seth(-40)
	drawSnake(40,80,3,pythonsize/2)

main()
