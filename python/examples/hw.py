# define a function
def hw(str_to_print):
    print str_to_print
    return
#
string1 = "Hello World!"
hw(string1)
hw("this is python")

#create a string
names = "john mary tom jean george"

#parse that string into a list
names2 = names.split()

#length of list
names2_len = len(names2)
print "length of list: ",names2_len

#loop through the list
print "contents of list:"
i = 0
while (i < names2_len):
    print str(i) + " " + names2[i]
    i = i + 1
    
#
entered = names2_len+1
while (entered > names2_len - 1):
    promptstring = "enter a number 0 through " + str(names2_len-1) + ": "
    # cast the entered string to integer
    entered = int(input(promptstring))
    
print "showing list item #" + str(entered) + ": " + names2[int(entered)]

