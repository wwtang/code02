"""compare two radix_bucket_sort"""

import time
import random

def sort_time(func):
    def wrapper(*argv):
        t1 = time.clock()
        res = func(*argv)
        t2 = time.clock()
        print "%s took %0.3f  ms" %(func.func_name, (t2 - t1)*1000.0)
        return res
    return wrapper
    
@sort_time
def radix_sortNumber_convert(array):
    numlen = len(str(array[0]))
    buckets = [[] for i in range(10)]#10 buckets

    for digit in xrange(numlen-1, -1,-1):
        for number in array:
            buckets[int(str(number)[digit])].append(number)
        del array[:]#save memory
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
    return array

@sort_time
def radix_sortNumber_mod(array):
    numlen = len(str(array[0]))
    buckets = [[] for i in range(10)]#10 buckets

    for digit in xrange(numlen-1, -1,-1):
        for number in array:
            buckets[number/10**(numlen-1-digit)%10].append(number)
            #buckets[int(str(number)[digit])].append(number)
        del array[:]#save memory
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
    return array

@sort_time
def nomal_sort(array):
    return sorted(array)

def main():
    array = [random.randint(100,999) for i in xrange(1000)]
    radix_sortNumber_convert(array)
    radix_sortNumber_mod(array)
    nomal_sort(array)

if __name__=="__main__":
    main()
    
