""" Given an infinit number of coins(quarters, dime, pennies,nickels), write code to
caculate the number of way of representing n cents.
I think this is the same problem with the stair case problem
f(n) = f(n-25)+f(n-10) +f(n-5) +f(n-1)
"""

def coinRepr(n):
    if n<=0:
        return 0
    if n == 1:
        return 1
    else:
        num_ways = coinRepr(n-25)+coinRepr(n-10)+coinRepr(n-5)+coinRepr(n-1)
    return num_ways

def main():
    print coinRepr(25)
    print coinRepr(1)
    print coinRepr(2)
    print "**"
    print coinRepr(3)
    print coinRepr(4)
    print coinRepr(5)
    print coinRepr(6)
    print coinRepr(10)
    print coinRepr(100)



if __name__=="__main__":
    main()
