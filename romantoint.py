import re
def romanToInt(romanNum):
    romanDict = {
        '' : 0, 'I' : 1, 'II' :2, 'III':3, 'IV':4, 'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX' :9,
        'X':10, 'CD':400, 'XX':20, 'CM': 900, 
        'XXX':30, 'DCCC':800, 'XL':40, 'CCC':300, 
        'L':50, 'LX':60, 'LXX':70, 'CC':200, 'LXXX':80, 
        'DC':600, 'XC':90, 'XCC':100, 'DCC':700, 
        'D':500, "M":1000,"MM":2000,"MMM":3000}

    romanPattern = re.compile(r'^(M{0,3})(CM|CD|C{1,3}|D?C{0,3})(XL|XC|X{1,3}|L?X{0,3})(IV|IX|I{1,3}|V?I{0,3})')
    romanNumGroup = romanPattern.search(romanNum).groups()
    print romanNumGroup
    Count = sum([romanDict[elem] for elem in romanNumGroup if elem in romanDict.keys()])
    print Count
    
