#!/usr/local/bin/python3

# this version reads lines from stdin
import fileinput

# example command line
# ubuntus '/home/jpj/yun/wx/reportDaily.py 2017-01-01' | ./drywx3.py
# example line of data
# 2017-08-01   86   51   57  0.00

i = 0
x = 0

# function to print out counts of dry days and dates
def prTally(var0, var2, var3):
    print("{0} to {1}: {2}".format(var0, var2, var3))

def prHeading(startDate):
    print("\nConsecutive dry days {0}".format(startDate[0:4]))
    print("=========================")

if __name__ == "__main__":

    for line in fileinput.input():
        line = line.strip('\n')
        if "201" in line:           # if there is a date
            line = line.split()      # parse the line
            if i == 0:
                beginDate = line[0]  # date of first record
                prHeading(beginDate) # print column headings
            i += 1                   # counter
            prec = float(line[4])    # convert precipitation text to float
            if prec == 0:            # days without precipitation
                if x == 0:
                    firstDate = line[0]
                else:
                    lastDate = line[0]
                x += 1
            else:                    # if there was precipitation print counts and reset counter
                if x == 1:
                    pass # don't bother showing one day only
                    #prTally(firstDate, firstDate, x) # print out same to - from date for single row
                if x > 1:
                    prTally(firstDate, lastDate, x)  # print out date range for mulitple rows
                x = 0

    # finish up by printing final tally
    if x == 1:
        prTally(firstDate, firstDate, x) # print out same to - from date for single row
    if x > 1:
        prTally(firstDate, lastDate, x)  # print out date range for mulitple rows

    print() # blank line for spacing
