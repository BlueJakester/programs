f=open("contacts5.txt", "r")

line = f.readline()
#print line,

l1 = line.split(" ")
#print l1

dict = {'fname': l1[0],
        'lname': l1[1],
        'phone': l1[2] }

#print dict
#print "==="

print "dict['fname']: ", dict['fname'], \
      "dict['lname']: ", dict['lname'], \
      "dict['phone']: ", dict['phone'],

f.close()
