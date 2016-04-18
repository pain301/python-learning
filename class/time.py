class Time:
	def __init__(self,hours = 0,minutes = 0,seconds = 0):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds
	def printTime(time):
		print '%dh:%dm:%ds'%(time.hours,time.minutes,time.seconds) 
	def increment(self,seconds):
		time.seconds+=seconds	
		time.minutes+=time.seconds/60
		time.seconds%=60
		time.hours+=time.minutes/60
		time.minutes%=60
		time.hours%=24

	def after(self,time):
		if self.hours>time.hours:
			return 1
		elif self.hours<time.hours:
			return 0
	pass

time = Time()
time.hours = 12
time.minutes = 30
time.seconds = 30
time.printTime()
time.increment(100)
time.printTime()

cur = Time(hours = 13,seconds = 30)
cur.printTime()

if time.after(cur):
	print 'time after cur'
else:
	print 'time before cur'
