import signal
import os
import time

def receive_signal(signum, stack):
    if signum == 2:
        print ("Recevied SIGINT {0}, exiting".format(signum))
        quit()
    else:
        print ('Received:', signum)

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)
signal.signal(signal.SIGINT, receive_signal)


print ('My PID is:', os.getpid())

while True:
    print ('Waiting...')
    time.sleep(3)
