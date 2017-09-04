f=open('test.txt', 'rw')

f.seek(3, 0)
s1 = f.read(1)
print s1
f.close()

f=open('test.txt', 'r+')
f.seek(3, 0)
f.write("X")

f.close()
