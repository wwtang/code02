

f = open('/Users/qitang/Documents/code02/equality.txt', 'r')

text = f.readlines()

import re
result = []
for line in text:
    match = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',line)

    if match:
        print match
       
        result.append(match)

