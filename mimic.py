def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  # LAB(begin solution)
  mimic_dict = {}
  f = open(filename, 'r')
  text = f.read()
  f.close()
  words = text.split()
  # what's hell of this prev?
  #prev is the first str in the dict if word in the dict just append the word to the end
  # else create a new key
  prev = ''
  for word in words:
    # if prev is not the key, set it as key, and append the word as the the first value
    if not prev in mimic_dict:
      mimic_dict[prev] = [word]
    else:
    # if the key "prev" exit, append the word as the next value in the value list
      mimic_dict[prev].append(word)
    # Could write as: mimic_dict[prev] = mimic_dict.get(prev, []) + [word]
    # It's one line, but not totally satisfying.

    
    # update the key of the dict
    prev = word
  return mimic_dict
  # LAB(replace solution)
  # return
  # LAB(end solution)
