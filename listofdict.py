import sys
def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it.
  a list of dict
  """
  # +++your code here+++

  #read the file into text, which read all the lines one time
    try:
        f = open("file.txt","r")
    except IOError:
        print "could not open file"
        sys.exit()
    text = f.readlines()

 
