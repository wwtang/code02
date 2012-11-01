import sys
import operator
def print_word(textname):
    # read the text
    try:
        f = open(textname,"r")
    except IOError:
        print "could not open the file"
        sys.exit()
    # read the entir file at one time, there should be another method
    text = f.read()
    f.close()

     # list of words
    words = text.lower().split()
    # count the word
    
    word_dict = {}
    for word in words:
        # not in the dict, create the item
        if not word in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] +=1
    

    # store the word as dict

    #for k in sorted(word_dict):
    #      print k, word_dict[k]
    return word_dict


def top_word(filename):
    created_dict = print_word(filename)
    sorted_dict = sorted(created_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    count = 0
    for item in sorted_dict:
        print item
        count +=1
        while count ==20:
            print "*"*10
            count = 0
        
    
def main():
    print"22"
    print_word("file.txt")

if __name__== '__main__':
    print "nima"
    main
