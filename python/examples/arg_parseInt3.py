#!/usr/local/bin/python3

# https://pymotw.com/2/argparse/

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a', action="store", dest="a", type=int, help="integer")
parser.add_argument('-b', action="store", dest="b", type=int, help="integer")
parser.add_argument('-c', action="store", dest="c", type=int, help="integer")

args = parser.parse_args()

print("{0}+{1}+{2}={3}".format(args.a,args.b,args.c,args.a+args.b+args.c))

# example usage and output
# $ ./arg_parseInt3.py -a 1 -b 2 -c 3
# 1+2+3=6
# $ ./arg_parseInt3.py -a 1 -b 2 -c3
# 1+2+3=6
# $ ./arg_parseInt3.py -a1 -b2 -c3
# 1+2+3=6
# $ ./arg_parseInt3.py -b2 -c3 -a1
# 1+2+3=6
