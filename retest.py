import re

line = "cate are smater than dog cate are smater than"

matchObj = re.search(r'are (.*) than', line, re.M|re.I)

if matchObj:
    print "search"
    print matchObj.group()
    print matchObj.group(1)
else:
    print "No match Object"

matchObj = re.match(r'are (.*) than', line, re.M|re.I)

if matchObj:
    print "match"
    print matchObj.group()
    print matchObj.group(1)
else:
    print "No match"

subObj = re.sub(r'cate', "Cate", line)

if subObj:
    print "subObj------->"
    print subObj
else:
    print "No subObj"



print line.replace("cate","CCate")

string = "Python&Pails"

matchObj1 = re.match(r'([Pp])ython&\1ails', string)

if matchObj1:
    print string
else:
    print "No match"

alternatives = "ruby ruble"

matchObja = re.findall(r'rub(y|le)', alternatives)
if matchObja:
    for elem in matchObja:
        print elem
else:
    print "Alternative not match"


