import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
#html = r.read()
for line in fhand:
	print line.strip()	
