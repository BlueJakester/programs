#!/usr/local/bin/python3

# http://www.pythonforbeginners.com/argparse/argparse-tutorial

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("number", help="display a square of a given number",
                            type=int)
args = parser.parse_args()
print(args.number**2)
