'''This function returns a dict with the element of the string 's' as key and the 
corresponding frequencies as value. histogram is used frequently please remember it'''
def histogram(s):
    new_d = {}
    for cha in s:
        if cha not in new_d:
            new_d[cha] = 1
        else:
            new_d[cha] +=1
    return new_d
