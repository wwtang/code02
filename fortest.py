def tryItAgain():
    print"Do you want to try it again? \n"
    return raw_input().lower().startswith('y')

import random
while True:

    guess = raw_input("Guess the number in 1 to 20:\n")
    number = random.randint(1,20)
    print number
    
    for counter in range(5):
        if guess == number:
            print "Good job, you get it, the number in "+ counter +" times"
            break
        if guess < number:
            print "too small! "
            guess = raw_input("New guess: ")
        if guess > number:
            print "too large"
            guess = raw_input("New guess: ")

    print"You failed in 5 times\n"
        
    if not tryItAgain():
        break
