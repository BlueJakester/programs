#!/usr/bin/python3

# print decimal equiv of 33-126
i = 33
x = 0

while i <= 126:
    # zero fill left to 3 digits i.e. "033 !" with no newline
    print(format(i, '03d'), chr(i), " ", end="")
    i += 1
    # after output og 10, print newline
    if x == 9:
        print()
        x = 0
    else:
        x += 1

# print a newline before exit
print()
