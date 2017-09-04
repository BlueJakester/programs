# file reading

f = open('file_write.txt', 'rw+')

string0=" "

for line in f:
    # Get the current position of the file.
    pos = f.tell()
    print "Current Position: %d" % (pos)
    print line

f.close()
