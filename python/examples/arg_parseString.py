#!/usr/local/bin/python3

# http://www.pythonforbeginners.com/argparse/argparse-tutorial

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("string", help="echo the string you use here")
args = parser.parse_args()  # returns data from the options specified (string)

print(args.string)    
