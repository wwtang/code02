''' Open a file and cout the line, word and character, and then output them as dict'''
def line_dict(filename):
    line_l = list()
    with open(filename) as fin:
        for line in fin:
            line_l.append(line.strip())
       # entire_line_l = line_l.split()#split line in words
        #line_s = ''.join(entire_line_l)#join the words into string
    #line_s = ' '.join(line_l)
    #line_l2 = line_s.split()
    print line_l
    print
    line_s = ' '.join(line_l)
    print 'string of sentence is: '
    print line_s
    print
    print '='*70
    print
    line_l2 = ' '.join(line_l).split()#list of sentence
    print 'list of words:'
    print line_l2
    print
    print '='*70
    print

    line_s2 = ''.join(line_l2)
    print 'string of words:'
    print
    print line_s2
    print
    return line_l2

     
def word_dict(line):
    word_d = dict()
    for  word in line:
        if word in word_d:
            word_d[word] +=1
        else:
            word_d[word] =1
    return word_d
        


def char_dict(word):
    char_d = {}
    for char in word:
        if char in char_d:
            char_d[char]  +=1
        else:
            char_d[char] = 1
    return char_d

    
