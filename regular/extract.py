import re

def extract1(line):
	start = line.find('@')	
	end = line.find(' ',start)
	return line[start+1:end]

def extract2(line):
	line = line.split()[1]
	line = line.split('@')[1]
	return line

def extract3(line):
	return re.findall('@([^ ]*)',line)

def extract4(line):
	return re.findall('^From: .*@([^ ]*)',line)

def extract5(line):
	return re.findall('^From: (\S+@\S+)',line)

def extract6(line):
	return re.findall('([0-9.]+)',line)

fhand = open('hello')
for line in fhand:
	print extract6(line)

