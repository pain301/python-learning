fruit = dict()
fruit['apples'] = 5.12
fruit['bananas'] = 4.55
fruit['melons'] = 6.15
print 'fruit:',fruit

print 'keys:',fruit.keys()
print 'values:',fruit.values()
print 'items:',fruit.items()
print 'has apples:',fruit.has_key('apples')

alias = fruit
copy = fruit.copy()
alias['apples'] = 6.66
print 'fruit:',fruit
copy['apples'] = 7.77
print 'fruit:',fruit
print 'copy',copy
