# split a string

f = open('text.txt', 'r')

#line = f.readline()
#print line,

#listline = line.split()
#print listline

#i = len(listline)
#x = 0
#while x < len(listline):
#    print listline[x]
#    x=x+1

for line in f:
    listline = line.split()
    day = listline[0]
    time = listline[3]
    print day, time
    sec = time[6:8]
    if int(sec) == 24:
        print "seconds are: ",sec
    if day == 'Fri':
        print "day is Friday"



f.close()
