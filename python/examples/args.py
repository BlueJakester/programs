import sys

# testing command line args

if len(sys.argv) == 1:
	print("No arguments received.")
	sys.exit(0)

print ("parameters received: {}".format(len(sys.argv)) )

#print ('Argument List:', str(sys.argv))

i = 0

while i < len(sys.argv):
    print("{0}: {1}".format(i, sys.argv[i]))
    i += 1
