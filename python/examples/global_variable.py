globvar = 0

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1

def print_globvar():
    print("gv",globvar)     # No need for global declaration to read value of globvar

def testglobvar():
    if globvar > 0:
        print(">0", globvar)

if __name__ == "__main__":
    set_globvar_to_one()
    print_globvar()
    globvar = 3
    print_globvar()
