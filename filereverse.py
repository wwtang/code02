import sys
try:
    file = open("file.txt","r")
except IOError:
    print "could not read the file"
    sys.exit()

text = file.readlines()
text.reverse()

for line in text:
    print line
