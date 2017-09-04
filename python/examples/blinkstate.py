import machine, time, mymodules, mytime

ledBlue  = machine.Pin(2, machine.Pin.OUT)
ledBlue.high() # high is off

# state = 0; # This is global variable.

def flipLed(value):
    if value == 0:
        ledBlue.low()
        # print("ledBlue.low()", state)
        return(1)
    else:
        ledBlue.high()
        # print("ledBlue.high()", state)
        return(0)

if __name__ == "__main__":
    global state
    state = 0
    i = 0
    while i < 10: # will light led 5 times
        state = flipLed(state)
        time.sleep(.5)
        i += 1
