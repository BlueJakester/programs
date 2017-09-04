total = 0; # This is global variable.

def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   global total
   total = arg1 + arg2; # Here total is local variable.
   return total;

def timestwo():
    global total
    total = (total * 2)

def printTotal(str1):
    global total
    print( "{0} {1}".format(str1, total) )

if __name__ == "__main__":
    printTotal(" pre sum")
    sum( 10, 20 )
    printTotal("post sum")
    timestwo()
    printTotal("post t*2")
