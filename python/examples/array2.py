#!/usr/bin/python3

from array import *

import time

#     ‘b’ -> Represents signed integer of size 1 byte
#     ‘B’ -> Represents unsigned integer of size 1 byte
# invalid    ‘c’ -> Represents character of size 1 byte
#     ‘u’ -> Represents unicode character of size 2 bytes
#     ‘h’ -> Represents signed integer of size 2 bytes
#     ‘H’ -> Represents unsigned integer of size 2 bytes
#     ‘i’ -> Represents signed integer of size 2 bytes
#     ‘I’ -> Represents unsigned integer of size 2 bytes
#     ‘w’ -> Represents unicode character of size 4 bytes
#     ‘l’ -> Represents signed integer of size 4 bytes
#     ‘L’ -> Represents unsigned integer of size 4 bytes
#     ‘f’ -> Represents floating point of size 4 bytes
#     ‘d’ -> Represents floating point of size 8 bytes

# integer 
#my_array = array('i')

# float
my_array = array('d')

x = 0
while x < 3:
    #epoch = int(time.time()) # integer
    epoch = time.time()
    my_array.append(epoch)
    print(epoch)
    x += 1
    time.sleep(1)

print("\nmy_array length:", len(my_array))
x = 0
# example output for following while loop
#
# my_array[0] 1479944908.601716
# my_array[1] 1479944909.602690
# my_array[2] 1479944910.603933
while x < len(my_array):
    print( "my_array[%d]" % x, end=" " )
    print( "%.6f" % my_array[x] ) # prints float with 6 decimal precision, i.e. 1479944387.716569
    x += 1

