"""
decorator example
"""
import random 

def decorate(func):
    print "decorate the function %s..."%func.__name__
    def wrapper(*args):
        a, b = args
        print "%s and %s" %(a, b)
        args = a*a, b*b
        print "Invoking the wrapperd function with arguments,", args
        return func(*args)

    print "end...."
    return wrapper

def doubleInput(func):
    print "this is decorator is used to double the input argument for the function %s" %(func.__name__)
    def wrapper(*args,**kwargs):
        a, b = args
        args = 2*a, a*b
        print "doubled args %s and %s"%(args)
        return func(*args)

    return wrapper    

@doubleInput
def testtest(a,b):
    return a+b


from functools import wraps

def my_decorator(view_func):
    def _decorator(request, *args, **kwargs):
        request = "jiba"
        response = view_func(request, *args, **kwargs)
        
        return response
    return wraps(view_func)(_decorator)


import time
def print_time(func):
    def wrapper(fargs,*args,**kwargs):
        startTime = time.clock() 
        fargs = "just a assingment"
        result = func(fargs, *args, **kwargs)
        endTime = time.clock()
        print "run time of this function is %s "  % ((endTime - startTime)*1000.0)
        print startTime, type(startTime)
        print endTime
        return result
    return wrapper



@print_time
def foo(request):
    return request + "   nima"

@print_time
def bubbleSort(arr):
    length = len(arr)
    for i in range(length-1):
        swapTest = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapTest = True

        if swapTest == False:
            break                

def addPostfix(func):
    

def main():
    lst = []
    for i in range(100):
        lst.append(random.randint(0, 100))

    bubbleSort(lst)
    
        #print foo("nima")
    

if __name__=="__main__":
    main()
