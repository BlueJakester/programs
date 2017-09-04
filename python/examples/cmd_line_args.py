#!/usr/bin/python

import sys

if len(sys.argv) < 2:
    print "No command line arguments, exit."
    exit()

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
