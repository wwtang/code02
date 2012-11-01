""" The problem in you code: 1, you read the whole file one time, that will be slow for the large file
2, you have another method to sort the dict by its values
3, you do not have the clear train of thought
Here is the train of thought(algorithm)
first, do the base, derive a dict from the file
secondly, define the two functions, so in you future program, remember how to get the dict from the file
"""
import sys
import operator
# derive the sorted  word_count_dict from the file
def word_count_dict(filename):
    try:
        input_file = open(filename,"r")
    except IOError:
        print "could not open the file"
        sys.exit()
    word_count = {}
    for line in input_file:
        words  = line.split()
        # Special check for the fisrt word in the file
        for word in words:
            word = word.lower()
            if not word in word_count:
                word_count[word]  = 1
            else:
                word_count[word] +=1
    input_file.close()
    return word_count   

# Print the word_count _dict XXXXXReturn the sorted dict
def print_count(filename):
    word_dict = word_count_dict(filename)
    words = sorted(word_dict.keys())
    # create an index of dict, but the dict not sorted, so loop as the index and print corresponding values
    for item in words:
        print item, word_dict[item]
        
# used for sorted by dict values
def get_value(tuples):
    return tuples[1]

def top_count(filename):
    word_dict = word_count_dict(filename)
    #word_dict.item() concert the dict into a list of tuple
 #   sorted_word = sorted(word_dict.item(), key= get_value, reverse=True)
   # for word in sroted_word[:20]:
#        print word, sorted_word[word]
    sorted_word = sorted(word_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_word:
        print item[0], item[1]

def main():
    if len(sys.argv) != 3:
        print "usage: python wordcount.py {--count|--topcount} \"filename\" "
        sys.exit(1)
    option = sys.argv[1]
    filename = sys.argv[2]
   
    if option == "--count":
        print_count(filename)
    elif option == "--topcount":
        top_count(filename)
    else:
        print "unkonwn  " + option 
        sys.exit(1)

if __name__ == "__main__":
    main()
                    


    

    
