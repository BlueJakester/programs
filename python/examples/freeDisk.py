import os

# check the root filesystem
s = os.statvfs('/')

freespace = (s.f_bavail * s.f_frsize) / (1024 * 1024)

print("disk free / {0} megabytes".format(freespace))

