#!/usr/bin/env python3

# parse command line for filename
# read and print lines from file
# print "match" if string found in a line

import sys, argparse

# declare a parser
parser = argparse.ArgumentParser()

# add argument "filename" to parser to store argv[1] in
parser.add_argument("filename", help="file to process")
# populate the args
args = parser.parse_args()

# process the file if it can be opened
try:
    with open(args.filename, 'r') as f:
        for line in f:
            line = line.strip('\n') # removes newline
            if 'jeff' in line:
                print("match: {0}".format(line))
            else:
                print("{0}".format(line))

# if the file cannot be opened
except:
    print("could not open file: {0}".format(args.filename))
