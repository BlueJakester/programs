#!/usr/bin/python3

import time
x = 1

# function 
def printinfo( name ):
    myTime = currentTime()
    # format output, i.e. '02: 2016-11-23 06:41:03 = Orange'
    print('{:02d}: {} = {}'.format(x, myTime, name))
    return;

# function 
def currentTime():
    current_time = time.localtime()
    return(time.strftime('%F %T', current_time)) #'2016-11-23 06:16:23'

names = ["Apple", "Orange", "Peach", "Pear"]

for i in names:
    printinfo(i)
    x += 1
    time.sleep(1)
