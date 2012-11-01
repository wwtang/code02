
def doitagain():
    print"Do you want to do it again? "
    return raw_input().lower().startswith('y')

while True:
    answer = raw_input("Do you like python? ")
    if answer =="yes":
        print "very good"
 #       answer = raw_input("yes or no:  ")
       # if answer == "yes":
#            print " yes good "
    else:
        print "no nnnono"

    if not doitagain():
        break
            
