def remove_dup(s,c):
    for i in s:
        
        if c in s:
            new_str = s.translate(None,c)
        else:
            raise CharacterNotFound
    return new_str

remove_dup('asdfaksjdf','d')
