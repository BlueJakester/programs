f=open("contacts4.csv", "r")
i=0

for line in f:
    # create list of each line
    list1 = line.split(",")
    # number of elements in list
    elements=len(list1)
    # loop through the file and print non-null elements
    while i < elements:
        if list1[i] != '':
            print list1[i],
        i=i+1
    i=0
