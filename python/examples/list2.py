a = ['a', 'b', 'c']
b = ['a', 'b', 'c']
print a

a.append('d')
print a

# appends list b to list a
a.extend(b)
print a

a.insert(0, 'z')
print a

# position of 'b' in list
print "index of first b: ", a.index('b')

# the number of times 'b' occurs in list
print " occurences of b: ", a.count('b')

a.sort()
print a

a.reverse()
print a
