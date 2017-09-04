# Calculate seconds since the epoch 1970-01-01

import datetime

NTP = datetime.datetime(2016, 12, 25, 19, 22, 48)
print("NTP", NTP)

RTC = datetime.datetime(2016, 12, 25, 19, 22, 57)
print("RTC", RTC)

ns = (NTP - datetime.datetime(1970,1,1)).total_seconds()
print("NTP seconds since epoch {0}".format(ns))

rs = (RTC - datetime.datetime(1970,1,1)).total_seconds()
print("RTC seconds since epoch {0}".format(rs))

diff = rs - ns
print("difference of {0:0.2f} seconds".format(diff))
