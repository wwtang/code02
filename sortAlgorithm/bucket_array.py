"""bucket sort"""


def bucket_sort(lst):
    #initialize the buckets
    buckets = [[] for i in range(10)]

    # distribute value to different bucket 
    for value in lst:
        buckets[value/10].append(value)
    #sort each bucket
    arr = []
    for bucket in buckets:
        sorted(bucket)
        #concatecate the sorted bucket
        arr += bucket
 
        
 
    return arr
if __name__=="__main__":
    from random import randint
    array = [randint(0,99) for x in range(20)]
    print "before sorting: ", array
    bucket_sort(array)
    print "after sorting: ", bucket_sort(array)
        
