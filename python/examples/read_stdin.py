#!/usr/bin/env python3

# will read lines from standard input and also read a filename passed on command line

import fileinput

for line in fileinput.input():
        print(">> {0}".format(line), end="") # print with leading '>> ' and no newline end=""
