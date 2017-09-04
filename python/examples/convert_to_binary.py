import sys

if len(sys.argv) == 1:
    print( "usage: {0} N (N = number to convert)".format(sys.argv[0]) )
    sys.exit(0)

# six_pad8spaces = "{0:08b}".format(int(sys.argv[1],16))
# print(six_pad8spaces)

pad4spaces = "{0:04b}".format(int(sys.argv[1],16))
print(pad4spaces)


