import re
import sys

try:
    file1 = open("About.html","r")
except IOError:
    print "Could not open the file"
    sys.exit()
    
text = file1.readlines()
file1.close()



keyword = re.compile(r"<.+?>")

for line in text:

    result = keyword.search(line)

    if result:
        print result.group(0), 
