import time

template = '{} - {:0.2f} - {:0.2f}'

print(template.format(
    time.ctime(), time.time(), time.clock())
)

# for i in range(2, 0, -1):
#     print('Sleeping', i)
#     time.sleep(i)
#     print(template.format( time.ctime(), time.time(), time.clock()) )

template2 = 'time.time() {:0.4f}'

for i in range(10):
    print( template2.format(time.time()) )
    time.sleep(.1)
