""" Radix sort for fixed length string"""



def radix_sortFixed(array):
    fixedLength = len(array[0])

    #create buckets
    oa = ord("a")
    oz = ord("z")
    buckets = [[] for x in range(oz-oa+1)]

    
    for position in xrange(fixedLength-1, -1, -1):#begin sort from the last letter
        for string in array:
            buckets[ord(string[position]) - oa].append(string)# put the string into corrent bucket
        del array[:]# empty array
        for bucket in buckets:#reassemble array in new order
            array.extend(bucket)
            del bucket[:]# empty bucket for next loop
    return array



def radix_sortNumber(array):
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

def radix_sortNumber1(array):
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
                


            
def main():
    import random
    array = ["code","base","dame","http","home"]
    print   radix_sortFixed(array)
    numarr = [random.randint(100,999) for i in xrange(10)]
    print radix_sortNumber(numarr)
    print radix_sortNumber1(numarr)

 

if __name__=="__main__":
    main()

    
