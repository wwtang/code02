def intToRoman(inputValue):
    if inputValue < 1 or inputValue > 3999:
        print "The input value is out of range"
        return None
    intRomanDict = {
	    0 : ["I",'IV','V','IX'],
	    1 : ['X','XL','L','XC'],
	    2 : ['C','CD','D','CM'],
	    3 : ['M','','','']	
		}
    n =  len(str(inputValue))
    result = []
    for d in range(n-1,-1,-1):#(3,2,1,0)
        d_value = inputValue/10**(d)%10
        if 1 <= d_value and d_value <= 3:
            result.append(intRomanDict[d][0]*d_value)
        elif d_value == 4:
            result.append(intRomanDict[d][1])
        elif 5 <= d_value and d_value <= 8:
            result.append(intRomanDict[d][2]+intRomanDict[d][0]*(d_value-5))
        elif d_value == 9:
            result.append(intRomanDict[d][3])
    return "".join(result)


    
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



def checkValid(inputValue):
    #check if the character in the string is not the roman numerals
    romanDict =['I','V','L','X','C','D','M']
    for elem in inputValue:
        if elem not in romanDict:
            return False
    #check if the character repeats over three times
    import re
    if re.findall(r'(\w)\1{4,}',inputValue):
        return False
    return True
	
def Roman_Int(inputValue):
	
    if isinstance(inputValue, int):#determine if input is integer
        return intToRoman(inputValue)
        
	
    if isinstance(inputValue, str):#determin if input is string
        if checkValid(inputValue):
            return romanToInt(inputValue)	
        else:
            raise Exception,"BadRomanNumeral"

def  test(got, expected):
    if got == expected:
        print "OK"
    else:
        print "No", "got", got, " but expected: ", expected
        
def main():
    print "test int to roman"
    test(Roman_Int(1),"I")
    test(Roman_Int(5),"V")
    test(Roman_Int(99),"XCIX")
    test(Roman_Int(3999),"MMMCMXCIX")
	
    print "test roman to int"
    test(Roman_Int("MMMCMXCIX"),3999)
    test(Roman_Int("XCIX"),99)
    test(Roman_Int("V"),5)
    test(Roman_Int("I"),1)
	
    print "test for bad romans"
    Roman_Int(0)
    Roman_Int(4000)
    Roman_Int("niasdf2")
    Roman_Int("IIIIII")

   
		
if __name__=="__main__":
    main()
	
			
