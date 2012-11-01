import sys
try: 
    f= open("est.txt", "rU")
    text = f.read()
    print text
    f.close()
except IOError:
    sys.stderr.write("problem reading: "+ "ext.txt")
