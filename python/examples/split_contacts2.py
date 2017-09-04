f=open("contacts4.csv", "r")
i=0
p=0

for line in f:
    # create list of each line
    list1 = line.split(",")
    # number of elements in list
    elements=len(list1)
    # loop through the file and print non-null elements
    while i < 13:
        if list1[i] != '':
            #print "el:",str(i),list1[i]
            print list1[i],
            p=p+1
            # I only want fname, lname and a number
            # so after getting one number, break
            if p == 3:
                p=0
                break
        i=i+1
    print
    i=0
