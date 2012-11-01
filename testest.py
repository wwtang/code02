def fun(n):
    if n >0:
         fun( n-1)
         print n
         fun(n-1)


def fun2(arr, n):
    if n==1:
        return arr[0]
    else:
        x = fun2(arr, n-1)
    if x >arr[n-1]:
        return x
    else:
        return arr[n-1]
        
def main():
    arr = [12, 10,30,50,100]
    print fun2(arr, 5)
    fun(4)
    return 0

if __name__=="__main__":
    main()
    
