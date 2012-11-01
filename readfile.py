f = open('file.txt', 'r')
print len(f.readline())
with open('file.txt','r') as f:
    print len(f.readline())
    
