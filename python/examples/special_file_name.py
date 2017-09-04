import os, sys

def hw():
    print("Hello World!")
    print( "printing __name__ from hw() function: {0}".format(__name__) )

if __name__ == "__main__":
    hw()
    print( "printing __file__ from main(): {0}".format(__file__) )
    print( "printing __name__ from main(): {0}".format(__name__) )
