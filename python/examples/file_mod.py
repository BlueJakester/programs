# file reading

def catfile():
    filein=open('file_write.txt', 'r')
    for line in filein:
        print line,
    filein.close()
    print

# show contents before
catfile()

# main section
filein  = open('file_write.txt', 'r+')
string0=" "
while 1:
    line = filein.readline()
    if not line:
        break
    #
    listline = line.split()
    recno = int(listline[0])
    day = listline[1]
    time = listline[3]
    sec = time[6:8]
    if recno == 8:
        print "file position: ",str(filein.tell())
        linelen = len(line)
        filein.seek(-linelen, 1)
        print "seek position: ",str(filein.tell())
        print line,
        listline[1]="XXX"
        newstring = string0.join(listline)+"\n"
        print newstring
        filein.write(newstring)
        break

filein.close()

# show contents after
catfile()
