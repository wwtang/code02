for i in range(1, 101):
    (a,b) = divmod(i,3)
    (c,d) = divmod(i,5)
    if b ==0 and d ==0:
        print "fizzbuzz"
    elif b == 0:
        print "fizz"
    elif d == 0:
        print "buzz"
    else:
        print i
    
