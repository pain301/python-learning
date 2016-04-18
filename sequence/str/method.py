str1 = 'Email from mlbing@163.com'
print 'str1.lower()',str1.lower()
print 'str1.upper()',str1.upper()
begin = str1.find('mlbing',9)
print 'email:',str1[begin:]
print 'str1.find(\'163\',10,20)',str1.find('163',10,25)

str2 = 'hello world'
print 'str2:',str2
print 'str2 replace world by pain:',str2.replace('world','pain')

str3 = '   I hate Python\n'
print 'str3',str3
print 'str3.rstrip()',str3.rstrip()
print 'str3.strip()',str3.strip()
