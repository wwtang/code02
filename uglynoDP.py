


def findNthUglyNo(n):
    uglyno = [0]*150
    uglyno[0] = 1
    i2 = i3 =i5 = 0

    next_multi_of_2 = uglyno[i2]*2# 2
    next_multi_of_3 = uglyno[i3]*3#3
    next_multi_of_5 = uglyno[i5]*5#5

    #print "next_multi_of_2", next_multi_of_2
    #print "next_multi_of_3", next_multi_of_3
    #print "next_multi_of_5", next_multi_of_5

    
    for i in range(1, 150):

        next_ugly = min(next_multi_of_2,next_multi_of_3, next_multi_of_5)


        uglyno[i] = next_ugly


        if next_ugly == next_multi_of_2:

            i2 = i2+1
            next_multi_of_2 = uglyno[i2]*2


        if  next_ugly == next_multi_of_3:
            i3 = i3+1

            next_multi_of_3 = uglyno[i3]*3

        if next_ugly == next_multi_of_5:
            i5 = i5 +1
            next_multi_of_5 = uglyno[i5]*5


    return uglyno[-1]

def main():
    print findNthUglyNo(150)
if __name__=="__main__":
    main()









