#!/usr/local/bin/python3
import sys

if len(sys.argv) == 1:
    print("usage: {0} n (n = positions to shift, max 7)".format(sys.argv[0]))
    sys.exit(0)

i = 1
x = int(sys.argv[1])

print("0b00000001 will be << {0}".format(x)) 

# bitwise shift x spaces left. i.e. if i=1 (0001) and x=1, i becomes (0010)
s = i << x

# print padded binary representation, i.e. 0b00001000
s = format(s, '#010b')
print("{0} {1}".format(s,x)) 
