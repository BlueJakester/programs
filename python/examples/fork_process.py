import os, time

pid = os.fork()

if pid:
    print('Child process id:', pid)
    time.sleep(15)
    print("parent process exiting")
else:
    print('I am the child')
    time.sleep(20)
    print("child process exiting")

