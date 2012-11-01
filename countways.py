"""
This is a recursion question
"""
map_dict = {}
def countway(n):
    if n < 0:
        return 0
    elif n == 0:
        map_dict[0] = 1
    else:
        map_dict[n] = countway(n-1)+countway(n-2) +countway(n-3)
        if n not in map_dict:
            map_dict[n]  = way

    return map_dict[n]


def test(got, expect):
    if got == expect:
        print "OK"
    else:
        print "NO,  got ", got, " expect ", expect

def main():
    test(countway(3), 4)
    test(countway(1), 1)
    test(countway(2), 2)

if __name__ == "__main__":
    main()
