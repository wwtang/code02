""" print all the duplicate of input string

"""


def printDup(string):
    if len(string) <2:
        return string

    help_dict  = dict()

    for char in string:
        if char not in help_dict:
            help_dict[char] = 1
        else:
            help_dict[char] +=1

    return help_dict

def main():
    string = "geeksforgeeks"
    print printDup(string)

if __name__=='__main__':
    main()
