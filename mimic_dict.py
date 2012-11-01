"""
Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

Set a flag "prev" as the key of the dict, update the prev every time for the new word
Check the if "prev" exits in the keys, if yes, just append the word as value, otherwise
create a new map, that "prev", : word

"""
import sys
import random

def mimic_dict(filename):
    # open file and read the text
    try:
        f = open(filename,"r")
    except IOError:
        print "could not open the file"
        sys.exit()
    text = f.read()
    f.close()
    
    # split the text into a list of words
    words = text.split()
    # set the dict and prev
    mimic_d = {}
    prev =  ''
    
    for word in words:
        if not prev in mimic_d:
            mimic_d[prev] = [word]
        else:
            mimic_d[prev].append(word)
        prev = word
         
    return mimic_d


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  # LAB(begin solution)
  for unused_i in range(20):
    print word,
    nexts = mimic_dict.get(word)          # Returns None if not found
    if not nexts:
      nexts = mimic_dict['']  # Fallback to '' if not found
    word = random.choice(nexts)
