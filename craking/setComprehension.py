from collections import namedtuple
Book = namedtuple("Book", "author title genre")



books = [
           Book("Pratchett", "Nightwatch", "fantasy"),
           Book("Pratchett", "Thief Of Time", "fantasy"),
           Book("Le Guin", "The Dispossessed", "scifi"),
           Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
           Book("Turner", "The Thief", "fantasy"),
           Book("Phillips", "Preston Diamond", "western"),
           Book("Phillips", "Twice Upon A Time", "scifi"),
]


fantasy_author = { b.author for b in books if b.genre == 'fantasy'}

fantasy_author1 = (b.author for b in books if b.genre == 'fantasy')
print fantasy_author
print 
for i in fantasy_author1:
	print i 
print fantasy_author1

fantasy_titles = {b.title:b for b in books if b.genre == 'fantasy'}
print fantasy_titles