# inverse a dict
#eg: {'2':[a,d,f],ArithmeticError '3': [s,d,f]}

def invent_dict(d):
    inverse_dict = {}
    for k in d:
        val = d[k]
        if val not in inverse_dict:
            inverse_dict[val] = [k]
        else:
            inverse_dict[val].append(k)
    return inverse_dict
