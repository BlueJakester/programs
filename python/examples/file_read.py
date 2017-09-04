# open file for reading
f1=open('text.txt','r')

# how many lines in file
#print "number of lines: " + str(len(f1))

# get and print first line
#print f1.readline()

# close file
f1.close()
#################################

# open file for reading
f1=open('text.txt','r')

# get and print all lines
print f1.read()

# close file
f1.close()
#################################

# open file for reading
f1=open('text.txt','r')

# create a list of lines
lines = f1.readlines()
# how many lines
numlines = len(lines)
print "number of lines in list: " + str(numlines)

# close file
f1.close()
#################################

# print lines one at a time
# i=0
# while i < numlines:
#    print lines[i]
#    i = i + 1
    
#################################
# write lines to a file
# open file for appending
f1=open('text.txt','a')

f1.write("processed\n")

# close file
f1.close()
#################################
