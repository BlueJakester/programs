from time import localtime, strftime

f = open('file_write.txt', 'w')

i = 0

while i < 10:
    string0 = str(i).zfill(3)
    string1 = strftime(" %a %d %b %Y %H:%M:%S\n", localtime())
    f.write(string0+string1)
    i=i+1

f.close()
