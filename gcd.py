"""
gcd greatest common divisor/ greatest common fractor
"""


def gcd(a , b):
    if a == 0:
        return b
    while b!=0:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a

def gcd2(a,b):
    if b == 0:
        return a
    else:
        return gcd2(b,  a%b)


def lcm(c,d):
    return c*d/gcd2(c,d)

def main():
    a = 4
    b = 6
    c = 4
    d =6

    print gcd(a,b)
    print gcd2(a,b)
    print lcm(c,d)

if __name__=="__main__":
    main()
