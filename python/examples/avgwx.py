#!/usr/local/bin/python3

# reads lines from stdin or single filename
import fileinput

# example command line
# ubuntus '/home/jpj/yun/wx/reportDaily.py 2017-01-01' | ./avgwx.py
# example line of data
# 2017-08-01   86   51   57  0.00

# counters
i = 0
x = 0

# vars for sum of high and low temps
totHigh = 0
totLow  = 0
totPrec = 0
totRain = 0.00

# vars for month, day, year strings
nextYear    = ""
nextMonth   = ""
firstYear   = ""
firstMonth  = ""

# conver numberical month to string month
def toMonth(m):
    if m == 1:
        return("Jan")
    elif m == 2:
        return("Feb")
    elif m == 3:
        return("Mar")
    elif m == 4:
        return("Apr")
    elif m == 5:
        return("May")
    elif m == 6:
        return("Jun")
    elif m == 7:
        return("Jul")
    elif m == 8:
        return("Aug")
    elif m == 9:
        return("Sep")
    elif m == 10:
        return("Oct")
    elif m == 11:
        return("Nov")
    elif m == 12:
        return("Dec")

# main 
if __name__ == "__main__":

    # print column headings once
    print("   \t   \tAvg\tAvg\tRain")
    print("Year\tMonth\tHigh\tLow\tInches")
    print("======================================")

    # main loop 
    for rawLine in fileinput.input(): # read lines from stdin 
        rawLine = rawLine.strip('\n') # strip newline
        if "201" in rawLine:           # if date, otherwise skip blank lines, etc.
            x += 1                     # row counter
            line = rawLine.split()     # parse the line
            currentDate  = line[0]  # get YYYY-MM
            currentHigh  = line[1]  # get maxF
            currentLow   = line[2]  # get minF
            currentPrec  = line[4]  # get minF
            totHigh += int(currentHigh) # sum high temp
            totLow  += int(currentLow)   # sum low temp
            totPrec += float(currentPrec)  # sum precipitation
            totRain += float(currentPrec)

            if i == 0:          # first row only
                firstYear  = currentDate[0:4]
                firstMonth = currentDate[5:7]
                i += 1
            else:               # subsequent rows
                nextYear  = currentDate[0:4]
                nextMonth = currentDate[5:7]
                # month changed, output counts, shift data and reset counter
                if firstMonth != nextMonth:
                    print("{0}\t{1}\t{2}\t{3}\t{4:6.2f}".format( firstYear, toMonth(int(firstMonth)), int(totHigh/x), int(totLow/x), float(totPrec)) )
                    x = 1
                    totHigh = int(currentHigh)
                    totLow  = int(currentLow)
                    totPrec = float(currentPrec)
                    firstYear  = currentDate[0:4]
                    firstMonth = currentDate[5:7]
                    nextYear  = ""
                    nextMonth = ""

# after last row with no month change print results.
print("{0}\t{1}\t{2}\t{3}\t{4:6.2f}".format( firstYear, toMonth(int(firstMonth)), int(totHigh/x), int(totLow/x), float(totPrec)) )

# show total precipitation
print("\t\t\t\t =====")
print("\t\t\tTotal\t{0:6.2f}".format( float(totRain) ))
