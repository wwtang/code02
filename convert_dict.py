def convert_dict(filename):
    new_dict = {}
    with open(filename) as f:
        for word in f:
            new_dict[word] = ''
    print  new_dict 

        
