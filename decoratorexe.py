#def  shout(words = "yes"):
#    return words.capitalize() +'!'



def talk():

    def whisper(word="yes"):
        return word.lower()+ "....."
    print whisper()




try:
    print whisper()
except NameError, e:
    print e


def getTalk(typ="shout"):

    def shout(word="yes"):
        return word.capitalize()+'!'

    def whisper(word="yes"):
        return word.lower()+"......."

    if typ == "shout":
        return shout
    else:
        return whisper

def doSomethingBefore(func):
    print "I do something before then I call the funciton"
    print func()

doSomethingBefore(getTalk)
