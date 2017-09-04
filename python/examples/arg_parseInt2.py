#!/usr/local/bin/python3

# http://www.pythonforbeginners.com/argparse/argparse-tutorial

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number", help="display a square of a given number greater than 9",
                            type=int)
args = parser.parse_args()

if args.number < 10:
    print("enter a number >= 10")
else:
    print(args.number**2)
