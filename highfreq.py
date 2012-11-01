"""
Return maximum orruring character in the input string
"""

def highfreq(string):
    if len(string) < 2:
        return [string]

    table = dict()

    
    for char in string:
        if char not in table:
            table[char] = 1
        else:
            table[char] +=1
    
    #for k, v in table.items():
    print table
    return max(table)


def main():
    string = "test"
    print highfreq(string)

    string = "xyzsasdf ksjdlkfie asnksdf skdjfe nxkjks e "
    print highfreq(string)

if __name__=="__main__":
    main()
