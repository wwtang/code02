# output the file

import sys
try:
    file1 = open("file.txt","r")
except IOError:
    print "could not read the file"
    sys.exit()


text = file1.readlines()

file1.close()

try:
    file2 = open("output.txt","w")
except IOError:
    print "could not open the file"
    sys.exit()
    
file2.writelines(text)
file2.close()

file2 = open ("append.txt", "a")
file2.writelines(text)
file2.close
