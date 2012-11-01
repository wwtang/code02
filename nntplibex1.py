import nntplib
import string

SERVER = "news.gmane.org"
GROUP= "gmane.comp.python.committers"
AUTHOR = "fredrick@pythonware.com"


#connecte to server
server = nntplib.NNTP(SERVER)

#choose a newsgroup
resp, count, first, last, name = server.group(GROUP)
print "count", "=>", count
print "range", "=>", first, last

#list all items on the server
resp, items = server.xover(first, last)

#extract some statistics
authors = {}
subjects = {}
for id, subject, author, date, message_id, reference, size, lines in items:
    authors[author] = None
    if subject[:4] == "Re: ":
        subject = subject[4: ]
    subjects[subject] = None
    if string.find(author, AUTHOR) >= 0:
        print id, subject
print "authors", "=>", len(authors)
print "subjects", "=>", len(subjects)



