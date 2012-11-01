import random


def tryItAgain():
    print "Do you want to try it agian?"
    return raw_input().lower().startswith('y')

while True:
    
    guesstoken = 0

    print "hello! what's you name?"
    myname = raw_input()

    number = random.randint(1,20)
    print "well, " + myname+ ",  the number in my mind is between 1 to 20, take a guess"


    
    while guesstoken < 6:
        print "take a guess"
        guess_num = input()
        guess = int(guess_num)

        guesstoken += 1

        if guess < number:
            print " your guess is too small."

        if guess > number:
            print "your guess is too large"

        if guess == number:
            break
    if guess == number:
        guesstoken = str(guesstoken)
        print "Good job, "+ myname +", you gueed the number\n"
        print "You are great, you get the right number in "+ guesstoken + " times.\n"
    if guess != number:
        number = str(number)
        print "Nope, the number I was thinking is "+ number
    if not tryItAgain():
        break
    
    
