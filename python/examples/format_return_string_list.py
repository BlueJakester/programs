#!/usr/bin/python3

# how to format a list and return it to the calling function

def formatLine():
    line = ['happy', 'holidays', 'to', 'all']
    return( "{0}-{1}-{2} {3}".format( line[0],line[1],line[2],line[3] ) )

str1 = formatLine()
print(str1)
