def romanToInt(inputValue):
    import re
    roamnToIntDict = {
		"I": 1, "II":2, "III":3, 'IV':4, 'V':5, "VI":6, "VII":'7', "VIII":8, 'IX':9,
		"X": 10, "XX":20, "XXX":30, 'XL':40, 'L':50, "LX":60, "LXX":'70', "LXXX":80, 'XC':90,
		"C": 100, "CC":200, "CCC":300, 'CD':400, 'D':500, "DC":600, "DCC":'700', "DCCC":800, 'CM':900,
		"M":1000,'MM':2000,'MMM':3000,'':0
		}

    romanpattern = re.compile('^(M{0,4})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
    result = romanpattern.findall(inputValue)
    return sum(roamnToIntDict[elem] for tuples in result for elem in tuples )
