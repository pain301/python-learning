def copy(dst,src):
	f1 = open(src,'r')
	f2 = open(dst,'w')
	while True:
		line = f1.read(512)
		if(line==''):
			break;
		f2.write(line)
	f1.close()
	f2.close()

copy('pain','hello')
