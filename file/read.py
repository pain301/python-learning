file_obj = open('./hello')
res1 = file_obj.read(5)
res2 = file_obj.read()
print res1+res2

#move pointer
file_obj.seek(0,0)

#read all lines
res3 = file_obj.readlines()
print res3

file_obj.seek(0,0)
for line in file_obj:
	print line.strip()

file_obj.close()
