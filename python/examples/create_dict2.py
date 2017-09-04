f=open("contacts5.txt", "r")

#line = f.readline()
#print line,

for line in f:
    l1 = line.split(" ")
    dict = {
        'fname': l1[0], 
        'lname': l1[1],
        'phone': l1[2]
        }
    print "dict['fname']: ", dict['fname']
    print "dict['lname']: ", dict['lname']
    print "dict['phone']: ", dict['phone']    

    
f.close()
