"""
Input: an array of number
Output: True, if all numbers are prime
             or False, (if not all the numbers are prime) and prime numbers
"""

import math
def isPrime(num):
  if num < 2:
     return False

  root = int(math.sqrt(num)+1)
  for i in range(2, root):
      if num % i== 0:
          return False
  return True


def allPrime(arr):

  if len(arr)<1:

    return False
  #set the default flag as True, if any non-prime number appears, set it as False
  allPrimeNumbers = True

  result = []

  for num in arr:
    if isPrime(num):
      result.append(True)
    else:
      result.append(False)
      allPrimeNumbers = False

  if allPrimeNumbers:

    return True #all number are prime numbers
  else:
    #not all the numbers are prime number, return an list of result of each number
    return result
        
def test(got, expect):
  if got == expect:
    print "OK"
  else:
    print "Got %s, but expect %s"%(got, expect)

def main():
  test(allPrime([2,3,5,7]),True)
  test(allPrime([2,3,4,5]),[True,True,False,True])
  test(allPrime([0,2,3,4]),[False,True,True,False])
  test(allPrime([11,13,17,19]),True)

if __name__=="__main__":
  main()





