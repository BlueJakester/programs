#import time

from time import gmtime, strftime
print strftime("GMT %a, %d %b %Y %H:%M:%S", gmtime())

from time import localtime, strftime
print strftime("LOC %a, %d %b %Y %H:%M:%S", localtime())
