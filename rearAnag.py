"""set the anagrams next to each other
input: a list of string
outpu: a dict with the anagram as the key and the corresponding string as value, value is a list
"""

def rearAnag(lst):
    storage_dict = {}
    for elem in lst:
        key = "".join(sorted(elem))
        if key not in storage_dict:
            storage_dict[key] = elem
            print storage_dict
        else:
            [storage_dict[key]].append(elem)
            print storage_dict
    return storage_dict

def printAnag(lst):
    output = rearAnag(lst)
    for item in output:
        print item

def test(got, expect):
    if got == expect:
        print "OK"
    else:
        print "No"
        print "got:", got, "expect,", expect

def main():
 #   test(rearAnag(["opts","stop","pots",'tosp',"over","evro","test","etts","vero"]),["opts","stop","pots",'tosp',"over","evro","vero""test","etts"])
    printAnag(["opts","stop","pots",'tosp',"over","evro","test","etts","vero"])
if __name__ =="__main__":
    main()
