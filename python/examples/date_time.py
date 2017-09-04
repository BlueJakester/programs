#!/usr/bin/python3

# date and time examples

import time

current_time = time.localtime()

#'2016-11-23 06:16:23'
print(time.strftime('%F %T', current_time))

#'2013-02-20 Wednesday'
print(time.strftime('%Y-%m-%d %A', current_time))

#'2013 Week 07 Day 3'
print(time.strftime('%Y Week %U Day %w', current_time))

#'Wed, 20 Feb 2013 23:52:14 GMT'
print(time.strftime('%a, %d %b %Y %H:%M:%S GMT', current_time))

#from time import gmtime, strftime
utctime = time.gmtime()
print(time.strftime("GMT %a, %d %b %Y %H:%M:%S", utctime))

#from time import localtime, strftime
print(time.strftime("LOC %a, %d %b %Y %H:%M:%S", current_time))
