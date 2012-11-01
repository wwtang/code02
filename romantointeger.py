"""Roman to integer
1. create the dict in detail
2. create the re.pattern
3. find all the matched subroman string (p.findall)
4. concatecate the result
{I:1, V:5, X:10, L:50 , C:100, D:500, M:1000 }
"""
import re

def RomanToInt(input_string):
    RomanDict = {
    "I":1,"II":2,"III":3,"IV":4, "V":5, "VI":6, "VII":7,"VIII":8,"IX":9,
    "X":10,"XX":20,"XXX":30,"XL":40, "L":50, "LX":60, "LXX":70,"LXXX":80,"XC":90,
    "C":100,"CC":200,"CCC":300,"CD":400, "D":500, "DC":600, "DCC":700,"DCCC":800,"MC":900,
    "M":1000,"MM":2000, "MMM":3000
    }

    pattern = re.compile(r'(M{1,3})|(C{1,3}|CD|DC{0,3}|MC)|(X{1,3}|XL|LX{0,3}|XC)|(I{1,3}|IV|VI{0,3}|IX)')
    result = []
    sublist = pattern.findall(input_string)
    for tuples in sublist:
        for elem in tuples:
            result.append(elem)

    final_result = sum([RomanDict[item] for item in result if item])
    return final_result

def input_control():
    input_string = raw_input("please input Roman Numbers: ")
    print RomanToInt(input_string)


def main():
    input_control()

    Try = True
    while Try:
        yorn = raw_input("Do you want to try it again? (yes or no):\t")
        if yorn.lower().startswith("y"):
            input_control()
        else:
            Try = False
     
if __name__=="__main__":
    main()
    

