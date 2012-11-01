"""integer to roman numbers

1. create the dict
2. analysys from the larget digit and append to resut(if begin from the small digit, we need to reverse the result)
3. concatecate the result
"""

RomanDict = {
    1: ["I", "IV", "V", "IX"],
    2: ["X", "XL", "L", "XC"],
    3: ["C", "CD","D", "CM"],
    4: ["M","", "", ""]
    }


def intToRoman(input_int):
    len_int  = len(str(input_int))
    result = []
    for digit in range(1,len_int+1):#begin from thousands digit
        remainder = input_int/10**(len_int - digit)%10#check each digit
        if remainder ==0:
            roman_value =""
        elif remainder >0 and remainder<4:
            roman_value = RomanDict[len_int-digit+1][0]*(remainder)
        elif remainder == 4:
            roman_value = RomanDict[len_int-digit+1][1]
        elif remainder >4 and remainder < 9:
            roman_value = RomanDict[len_int-digit+1][2] + RomanDict[len_int-digit+1][0]*(remainder -5)
        elif remainder == 9:
            roman_value = RomanDict[len_int-digit+1][3]
        result.append(roman_value)
    finalresult = "".join(result)
    return finalresult
        
def Input_control():
    input_int = input("Please input the integer(0-3999): ")
    if input_int <0 or input_int > 3999:
        print "The input integer out of range"
    else:
        print "The Roman Number is: ",   intToRoman(input_int)
    
    
def main():
    Input_control()

    Try = True
    while Try:
        yorn = raw_input("try it again? (yes or no): " )
        if yorn.lower().startswith("y"):
            Input_control()
        else:
            Try = False
        

if __name__=="__main__":
    main()



