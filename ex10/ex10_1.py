"""10.1
Question: You are given tow sorted arrays, A and B, where A has a large engough buffer at the end to hold B.
Wirte a method to merge B into A.

****************
It look like merge sort, but there is no need for the extra space to allocate the sorted element, due the the
buffer at the end of A.
At firt, I was think about the merge process of the external sort. But it is inefficent here
The better way is begin from the last. choose and compare the largest element of each aaray and place it
at the end of A, so that the largest element in both A and B is located at the correct place

example:

A = [1,4,6,8,9]
B = [2,5,10]

return A = [1,2,4,5,6,8,9,10]

"""

def mergeAB(A, B):
    indexA=  len(A)-1
    indexB = len(B)-1
    mergeIndex = len(A)+len(B) -1# the size of A is a problem
    A = A +[""]*len(B)#create the buffer of size B and append to A
    print len(A)

    while indexA >= 0 and indexB >= 0:# watch out "0" is the first in the Index, do not foget it
        if A[indexA] >= B[indexB]:
            A[mergeIndex] = A[indexA]
            mergeIndex -=1
            indexA -=1
        else:
            A[mergeIndex] = B[indexB]
            mergeIndex -=1
            indexB-=1
            
    while indexB >= 0:# A is already in A, so just think about B
        A[mergeIndex] = B[indexB]
        mergeIndex -= 1
        indexB -=1
    return A

def main():
    A = [2,4,6,8,9,10,15,36]
    B = [1,5,10]
    print mergeAB(A,B)

if __name__=="__main__":
    main()






