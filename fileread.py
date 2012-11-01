import sys
import re
try:
    file = open("file.txt","r")
except IOError:
    print "Could not open the file"
    sys.exit()

text = file.readlines()
file.close()

keyword = re.compile(r'the')

for line in text:
    if keyword.search(line):
        print line,
