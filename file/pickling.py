import pickle
f = open('nums','w')
pickle.dump(12.3,f)
pickle.dump([4,5,6],f)
f.close()

f = open('nums','r')
x = pickle.load(f)
print 'x:',x
x = pickle.load(f)
print 'x:',x
