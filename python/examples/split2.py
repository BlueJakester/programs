#!/usr/local/bin/python3

#string = "Now is the time for all good men"
string = "Now,is,the,time,for,all,good,men"

print (string)

# delimiter space by default, otherwise provide
string = string.split(",")
print (string)

i=0
while i < len(string) :
	print (i, string[i])
	i += 1
