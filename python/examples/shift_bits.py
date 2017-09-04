#!/usr/local/bin/python3

import time
i = 1
y = 1
for x in range(8):
    # bitwise shift x spaces left. i.e. if i=1 (0001) and x=1, i becomes (0010)
    s = i << x

    # print padded binary representation, i.e. 0b00001000
    s = format(s, '#010b')
    print("{0} {1}".format(s,y)) 

    # used to represent current binary value with integer. i.e. 1, 2, 4, 16...
    y *= 2 
