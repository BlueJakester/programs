#!/usr/local/bin/python3

# http://www.pythonforbeginners.com/argparse/argparse-tutorial

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("string1", help="echo string1")
parser.add_argument("string2", help="echo string2")
args = parser.parse_args()  # returns data from the options specified (string)

if args.verbose:
    print("verbosity turned on")
    print("this is the 1st string passed: ",args.string1)    
    print("this is the 2nd string passed: ",args.string2)    
else:
    print(args.string1)    
    print(args.string2)    
