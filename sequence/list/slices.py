week = ['monday','tuesday','wdensday','thursday','friday']
print week[2]
print week[-2]
print week[1:4]
print week[:5]
print week[::-1]
print week[:]
week[1:3] = ['hello','world']
print week
week[1:4] = []
print week
week[3:3] = ['new insert']
print week
