"""
Write a method to replace all the whilespace with %20 in a string, the string has enough buffer at the
end of the string

algorithm:
1. scane the string to count the whitespace, to caculate the new length of the string
2. scane from the end of the string, if we  get the whitespace replace it with %20 else copy the original
char

"""
def insertChar(string):
    if len(string) <2:
        return None
   
    count = 0
    for char in string:
        if char == " ":
            count +=1
    new_str_len = len(string) + count *3
    new_str = [""]*new_str_len

    for i in range(len(string)-1,-1,-1):
        if string[i] == " ":
            new_str[new_str_len -1] = "0"
            new_str[new_str_len-2] = "2"
            new_str[new_str_len - 3] ="%"
            new_str_len = new_str_len - 3#update the length of new_str_len
        else:
            new_str[new_str_len - 1] = string[i]#copy the original char
            new_str_len = new_str_len -1
    return "".join(new_str)

def main():
    string = "test me"
    print insertChar(string)

if __name__=="__main__":
    main()
            
            

    
