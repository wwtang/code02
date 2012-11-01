# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # +++your code here+++
    if len(s) >= 3:
        if s[-3:] == "ing": s = s[:-3] + "ly"
           # return s[:-3] + "ly"
        else: s = s+"ing"
 #           return  s + "ing"
    else:
        return s

    
# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  # the use of s.find
  n = s.find("not")
  b = s.find("bad")

  if n and b  and n <b:
      return s[:n] +"good"+ s[b+3:]
  return s
  

def test(got, expected):
    if got == expected:
        print "OK, got: %s : expected: %s" %(got, expected)
    else:
        print "X"

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  # do not make it too much complicated
    a_mid = len(a)/2
    b_mid = len(b)/2

    if len(a)%2 ==1:
        a_mid = len(a)/2+1
        print a_mid
    if len(b)%2 ==1:
        b_mid = len(b)/2+1
        
    return a[:a_mid] + b[:b_mid] +a[a_mid:]+b[b_mid:]
 
  

def main():
    print  "verbing\n"
    test(verbing("flying"), "flyly")
    test(verbing("shot"), "shoting")
    test(verbing("run"), "runing")
    test(verbing("kkk"),"kkking")
    test(verbing("ji"), "ji")
    print"\n"

    print "not_bad\n"
    test(not_bad("I am not bad"), "I am good")
    test(not_bad("This dinner is not bad"), "This dinner is good")
    test(not_bad("bad not ha"), "bad not ha")
    #   test(not_bad("not not bad bad"),)
    test(not_bad("The weather is not so bad"), "The weather is good")

    print "\n"
    print "front_back\n"
    test(front_back("comp!!!","app%%"),"compapp!!!%%")
    test(front_back("howareyou?","**&&"),"howar**eyou?&&")
    test(front_back("##123","**456"),"##1**42356")
if __name__ == "__main__":
    main()
    
    
