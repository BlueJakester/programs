#!/usr/bin/env python

# simple script to read and print command line arguments

import sys

if len(sys.argv) == 1:
    print("No arguments received.")
    sys.exit(0)

print ("number of args: {0}".format(len(sys.argv)) )

i = 0
while i < len(sys.argv):
    print("argv{0} {1}".format(i, sys.argv[i]))
    i += 1
