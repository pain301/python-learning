purse = dict()
purse['money'] = 12
purse['candy'] = 20
purse['book'] = 8
tmp = list()
for key,value in purse.items():
	tmp.append((value,key))
tmp.sort(reverse=True)
print tmp
