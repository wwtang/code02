with open('poem.txt') as fin:
    for line in fin:
        print len(line.rstrip())
        print len(line)
    #print len(fin.readline().rstrip())
