#!/usr/bin/python3

# Function definition
def printinfo( name ):
   print ("Name: ", name)
   return;

# list of names
names = ["Joe", "Tom", "Gil", "Kim"]
i = 0

while i < len(names):
    printinfo(names[i])
    i += 1
