#!/usr/local/bin/python3

# demonstrate what binary representation of integers looks like

i = 1
while i <= 255:
    g = format(i, '#010b')       # padded binary as ascii
    print("{0} {1}".format(g,i)) 
    i *= 2
