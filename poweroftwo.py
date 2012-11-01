def powOfTwo(x):
    if x<1:
        return False
    elif x ==1:
        return True
    else:
        x = divNum(x)
  

def divNum(x):
    while x >1:
        x = x/2
        return x
