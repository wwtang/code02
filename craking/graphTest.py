"""
Graph test

"""

wdg = {
	'0':{'1':5,'3':10},
	'1':{'2':3},
	'2':{'3':1},
	'3':{}
}

for vertex in wdg:
	print vertex, wdg[vertex]

inf = float('inf')

dist ={}
for vstart in wdg:
	item = {}
	for vend in wdg:
		if wdg[vstart] == vend:

			dist[vstart] = 


