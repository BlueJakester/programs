import time

for i in range(20):
    asciibinary = "{0:04b}".format(int(str(i),16))
    print("{:0d}".format(i))
    print(asciibinary)
    time.sleep(.5)
