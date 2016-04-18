import re
fhand = open('hello')
for line in fhand:
	line = line.strip()
	if re.search('From:',line):
		print line
