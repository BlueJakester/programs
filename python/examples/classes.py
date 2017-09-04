import time, os

callcount = 0

# define a class with two functions.
class Myclass():
    c = 0

    def printTime(self):
        current_time = time.localtime()
        print("current date-time {}".format(time.strftime('%F %T', current_time)) )
        self.c += 1
        return(self.c)
    
    def systemCall(self, str1):
        os.system(str1)
        self.c += 1
        return(self.c)

# see explanation for this below
if __name__ == '__main__':
    print()
    # create an object of Myclass
    obj1 = Myclass()
    # create another object of Myclass, which is essentially a copy
    obj2 = Myclass()

    # make a few calls to object 1 and keep count by updating return code rc
    calls_to_obj1 = obj1.printTime()
    time.sleep(.5)
    calls_to_obj1 = obj1.printTime()
    time.sleep(.5)
    calls_to_obj1 = obj1.systemCall("pwd")
    time.sleep(.5)

    calls_to_obj2 = obj2.printTime() # now call object 2

    print( "\ncalls_to_obj1 = {}".format(calls_to_obj1) )
    print( "calls_to_obj2 = {}\n".format(calls_to_obj2) )
    SystemExit

"""
When the Python interpreter reads a source file, it executes all of the code found in it.

Before executing the code, it will define a few special variables. For example, if the python 
interpreter is running that module (the source file) as the main program, it sets the
special __name__ variable to have a value "__main__". If this file is being imported from another 
module, __name__ will be set to the module's name.

In the case of your script, from the command line you type:

    python3 calsses.py

After setting up the special variables, it will execute the import statement and load those modules.
It will then evaluate the def block, creating a function object and creating a variable called
myfunction that points to the function object. It will then read the if statement and see 
that __name__ does equal "__main__", so it will execute the block shown there.

One of the reasons for doing this is that sometimes you write a module (a .py file) where it can
be executed directly. Alternatively, it can also be imported and used in another module. By doing
the main check, you can have that code only execute when you want to run the module as a program
and not have it execute when someone just wants to import your module and call your functions themselves.
"""
