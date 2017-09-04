import json

f=open("sequence.txt", "w")

seq = ("John", "Doe", "303-555-1212")
print seq

# write the list to a text file
json.dump(seq,f)
f.close()

# read list from text file
f=open("sequence.txt", "r")
print "reading file"
x=json.load(f)
print x," len ",len(x)

i=0
while i < len(x): 
    print x[i]
    i=i+1

f.close()
