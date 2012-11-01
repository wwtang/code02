import re
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher andytang@gmail.com'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
        print tuple[0]  ## username
        print tuple[1]  ## host
print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
