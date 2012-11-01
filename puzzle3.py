
f = open('/Users/qitang/Documents/code02/webpage.txt','r')
text = f.readlines()

import re

result = []

for line in text:
    match = re.search(r'[a-zA-Z]', line)
    if match:
        result.append(match.group())
        
