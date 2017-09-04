# pad output example

for x in range(1, 10):
    print repr(x).rjust(3), repr(x*10).rjust(3)

print "--------------------------"

# pad to left with zeros
for x in range(1, 20):
    print str(x).zfill(3), repr(x*10).zfill(4)
