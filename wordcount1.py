""" The problem in you code: 1, you read the whole file one time, that will be slow for the large file
2, you have another method to sort the dict by its values
3, you do not have the clear train of thought
Here is the train of thought(algorithm)
first, do the base, derive a dict from the file
secondly, define the two functions, so in you future program, remember how to get the dict from the file
"""

import sys

def word_count_dict(filename):
    """ Returns a word/count dict for the filename"""
    #utility used by word_pirnt and top_print
    word_count = {}
    input_file = open(filename,"r")
    for line in input_file:
        words = line.split()
        for word in words:
            word = word.lower()
            # special case if we're seeing this word for the first time
            if not word in word_count:
                word_count[word] = 1
            else:
                word_count[word] +=1
    input_file.close()
    return word_count


def print_words(filename):
    """ Prints one per line '<word> <count> stored by word for the given file.'"""
    # call the word_count_dict function to get the desire dict
    word_count = word_count_dict(filename)
    words = sorted(word_count.keys())
    for word in words:
        # pay attention to here
        print word, word_count[word]


def get_count(word_count_tuple):
    """ Return the count from a dict word/coutn tuple, used for custom sort"""
    return word_count_tuple[1]

def print_top(filename):
    """print the top 20 items for the given file"""
    word_count = word_count_dict(filename)
    #Each item is a (word, count) tuple
    #Sort them so the big count are first using key=get_count() to extract cout.
    items = sorted(word_count.items(), key=get_count, reverse=True)

    #Print the first 20
    for item in items[:20]:
        print item[0], item[1]




def main():
    """ the most interesting part of the file ......"""
    if len(sys.argv) !=3:
        print "usage: ./wordcount.py  {--count/--topcount} file"
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]

    if option =="--count":
        print_words(filename)
    elif option =="--topcount":
        print_top(filename)
    else:
        print "unknow option." + option
        sys.exit(1)
if __name__ =="__main__":
    main()
