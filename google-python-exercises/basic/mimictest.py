
import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  f = open("/Users/qitang/Documents/code02/google-python-exercises/basic/small.txt")
  raw_data = f.read()
  f.close()
  
  m_dict = {}
  data = raw_data.split()
  pre = " "
  for word in data:
      if not pre in m_dict:
        m_dict[pre] = [word]
      else:
        m_dict[pre].append(word)
      pre = word
 

  return m_dict


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
