/*
 * A better blink without delay or running a process at intervals without a delay
 *
 * Jack's example program modified to work with builtin LED pin 13 on Arduino Uno
 */

#include "Timer.h"  //http://github.com/JChristensen/Timer
Timer t;            //instantiate the timer object

void setup(void)
{
    pinMode(LED_BUILTIN, OUTPUT);
    t.oscillate(LED_BUILTIN, 1000, LOW); // sets up the time for 1 second intervals
}

void loop(void)
{
    // only requires a few milliseconds to run the timer update
    t.update();

    // other code here, runs without a delay() function above
}

