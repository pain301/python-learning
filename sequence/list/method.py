aList = [2,4,8,1,3,7,10];
aList.sort()
aList.pop()
aList.pop(0)
aList.append(110)
print aList
del aList[1:4]
print aList
print 'average of list is %.2f'%(sum(aList)/len(aList))
aList.sort(reverse = True)
print aList
aList.reverse()
print aList

bList = ['apple','banana','linux','python','popular game']
print bList
bList.sort()
print bList
bList.sort(key = len)
print bList


week = ['monday','thuesday','wdensday','thursday','friday']
weekend = ['saturday','sunday']
print week
week.extend(weekend)
print week
