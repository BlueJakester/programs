# error handling
# open close file loop on single line
# strip newline
# check ticks for millis start and stop

import time

fname='data.txt'

def readit():
    try:
        with open(fname, 'r') as f:
            line = f.read()
            line = line.strip('\n') # chomps removes newline return \n
            print("{0}".format(line) )
    except:
        print("error opening file {0}".format(fname))

if __name__ == "__main__":
    t0= time.clock()
    readit()
    t= time.clock()
    print("millis start {0:0.6f}".format(t0) )
    print("millis   end {0:0.6f}".format(t) )
    print("millis  diff {0:0.6f}".format(t - t0 ) ) # t is CPU seconds elapsed (floating point)
