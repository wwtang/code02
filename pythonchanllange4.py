import urllib

f= urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')

while True:
    nextf = f.read()[-5:]
    f = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nextf)
    print nextf
    if not f:
        break



