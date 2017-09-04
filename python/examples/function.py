#!/usr/bin/python3

# A default argument is an argument that assumes a default value if a
# value is not provided in the function call for that argument. The
# following example gives an idea on default arguments, it prints
# default age if it is not passed

# Function definition is here
def printinfo( name = "Mike", age = 35 ):
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="Vicky" )
printinfo( name="Vicky" )
printinfo()
