months = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")

for index, month in enumerate(months):
    print("index: {0} month {1}".format(index, month))

print() # for whitespace only

# outputs
# index: 0 month JAN
# index: 1 month FEB
# index: 2 month MAR
# index: 3 month APR
# index: 4 month MAY
# index: 5 month JUN
# index: 6 month JUL
# index: 7 month AUG
# index: 8 month SEP
# index: 9 month OCT
# index: 10 month NOV
# index: 11 month DEC

for index, month in enumerate(months, 1):
    print("index: {0} month {1}".format(index, month))

# outputs
# index: 1 month JAN
# index: 2 month FEB
# index: 3 month MAR
# index: 4 month APR
# index: 5 month MAY
# index: 6 month JUN
# index: 7 month JUL
# index: 8 month AUG
# index: 9 month SEP
# index: 10 month OCT
# index: 11 month NOV
# index: 12 month DEC

print() # for whitespace only

# create dictionary, indexed list
monthd = dict(enumerate(months, 1))
print( monthd ) # print monthd list
print( monthd[2] ) # print only value at list position 2

# outputs
# {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT', 11: 'NOV', 12: 'DEC'}
# FEB
