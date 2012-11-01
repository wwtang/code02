"""fibonacci numbers:  cache the intermediate result"""
import time

#Cached method
def fib1(n):
    cache_dict = {0:0,1:1}

    if n == 0: return 0
    if n == 1: return 1
    if n in cache_dict:
        return cache_dict[n]
    cache_dict[n] = fib1(n-1) + fib1(n-2)
    return cache_dict[n]

#Non Cached method
def fib2(n):
    if n == 0:
        return 0
    if n ==1:
        return 1
    else:
        return fib2(n-1) +fib2(n-2)

def main():
    i = 30
    start1 =  time.clock()
    print fib1(i)
    end1 =  time.clock()
    runtime1 = end1 - start1
    print  runtime1, "seconds"

    start2 = time.clock()
    print fib2(i)
    end2 = time.clock()
    runtime2 = end2 - start2
    print runtime2, "seconds"

    print "The no cache method takes ", runtime2 - runtime1, " more seconds than the cached method."

     

if __name__=="__main__":
    main()
   
    
