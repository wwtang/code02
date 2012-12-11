import urllib2 
f = urllib2.urlopen("http://www.elacarte.com/challenge/city_grid.txt",'r')
data = f.readlines()

countP = 0
#
for line in data:
	for char in line:
		if char == "P":
			countP +=1

print countP