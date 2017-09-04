#!/usr/local/bin/python3

""" practice using dates and times.
"""

# YouTube tutorial https://www.youtube.com/watch?v=eirjjyP2qcQ

import datetime, pytz

# tday = datetime.date.today()
#print("{} is today".format(tday) )
#print("Hello World!")
#

# tdelta = datetime.timedelta(hours=7)
# print("{} is today + 7 days".format(tday + tdelta) )

# date2 = date1 + timedelta
# timedelta = date1 + date2

# bday = datetime.date(2017, 2, 22)
# till_bday = bday - tday
# print("until my bday:", till_bday)
# print("until my bday:", till_bday.days)
# print("seconds until my bday:", till_bday.total_seconds())

# t = datetime.time(9, 30, 45, 100000)
# print(t)
# print(t.hour)

# dt = datetime.datetime(2017, 2, 22, 9, 30, 45, 100000)
# print(dt)
# print(dt + tdelta, "plus 7 hours")
# print(dt.time())
# print(dt.date())

# dt_today = datetime.datetime.today()
# dt_utcnow = datetime.datetime.utcnow()
# print(" today", dt_today)
# print("   now", dt_now)
# print("utcnow", dt_utcnow)

# dt = datetime.datetime(2016, 11, 29, 20, 39, 30, tzinfo=pytz.UTC)
# print(dt)
# print(dt_now)
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print("UTC", dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print("MTN", dt_mtn)
print("ISO format", dt_mtn.isoformat())

# for tz in pytz.all_timezones:
#     print(tz)

# test comment
# comment again
# three
