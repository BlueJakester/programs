f=open('test.txt', 'r+')
                       
f.seek(3, 0)
print "seek1 position: ",str(f.tell())
s1 = f.read(1)
print s1

print "read1 position: ",str(f.tell())

f.seek(3, 0)
print "seek2 position: ",str(f.tell())

f.write("X")

f.close()
