""" quick sort example"""

def quicksort1(list):
    """quick sort using list comprehension"""
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = quicksort1([x for x in list[1:] if x < pivot])
        greater = quicksort1([x for x in list[1:] if x >=pivot])
        return lesser +[pivot ]+ greater


def test(got, expect):
    if got == expect:
        print "OK"
    else:
        print "NO", "got: ", got, "expect: ",expect

def main():
    test(quicksort1([6,5,3,8,1,6,7]),[1,3,5,6,6,7,8])

if __name__ == "__main__":
    main()
