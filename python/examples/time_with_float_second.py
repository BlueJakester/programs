#!/usr/bin/python3

import time
from datetime import datetime

try:
    while True:
        #print( datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') )
        print( datetime.now().strftime('%H:%M:%S.%f') )
        time.sleep(1)

except KeyboardInterrupt: # if CNTL-C entered
    quit()
