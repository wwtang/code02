"""
ex10.2
Question:
Write a method to sort an array so that all the anagrames are next to each other.
***********************
First, determin the anagrams.(sort every string to check if they are anagrams)
And then, create a dict, use the unique sorted string as key and the strings that are anagrams to be the value,
            which is a list of string
print out the values of the dict.
"""

def output_ana(arr):
    assist_dict = {}

    for item in arr:
        sitem = str(sorted(item))#sorted(item) is a list of characters
        if sitem  not in assist_dict:
            assist_dict[sitem] = [item]# this [item] is cool, so that we can append next stirng to the values
        else:
            assist_dict[sitem].append(item)

    result = [elem for item in assist_dict.values() for elem in item]#nested list comprehension, from left to right order
    return result

def main():
    arr = ["opts","next","jijo","post","xent","iojj","star","arts","stop"]
    print output_ana(arr)

if __name__=="__main__":
    main()

    
