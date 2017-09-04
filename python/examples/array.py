# test comment from Atom Editor on iMac

# from http://www.thegeekstuff.com/2013/08/python-array
#
# An array is a data structure that stores values of same data type.
# In Python, this is the main difference between arrays and lists.

# While python lists can contain values corresponding to different data types,
# arrays in python can only contain values corresponding to same data type.
# In this tutorial, we will understand the Python arrays with few examples.

# To use arrays in python language, you need to import the standard ‘array’ module.
# This is because array is not a fundamental data type like strings, integer etc.
# Here is how you can import ‘array’ module in python :

from array import *

# Once you have imported the ‘array’ module, you can declare an array. Here is how you do it:
#    arrayIdentifierName = array(typecode, [Initializers]

# my_array = array('i',[1,2,3,4])
#
# In the example above, typecode used is ‘i’. This typecode represents signed integer whose size is 2 bytes.
#
# Typecodes are the codes that are used to define the type of array values or the type of array. Here is the list of available typecodes:
#
#     ‘b’ -> Represents signed integer of size 1 byte
#     ‘B’ -> Represents unsigned integer of size 1 byte
#     ‘c’ -> Represents character of size 1 byte
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

my_array = array('i', [1,2,3,4,5])
for i in my_array:
    print(i)

# access element

print ("element 1:", my_array[1])

# Append any value to the array using append() method
print("append 6")
my_array.append(6)
for i in my_array:
    print(i)

# Insert value in an array using insert() method
print("insert 0 at element 0")
my_array.insert(0,0)
for i in my_array:
    print(i)
