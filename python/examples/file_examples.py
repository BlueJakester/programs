# file reading

f = open('text.txt', 'r')

for line in f:
    print line, # the comma chomps of \n

f.close()

###

f = open('text.txt', 'r')

i = 0

for line in f:
    print i, line, # the comma chomps of \n
    i=i+1

f.close()
