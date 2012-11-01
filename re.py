import re

import sys
import string


f = open("file.txt","r")
text = f.read()
print text

list_str = re.findall(r"(\w+)+", text)
for word in list_str:
    print word

