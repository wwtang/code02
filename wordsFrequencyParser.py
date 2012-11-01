""""
Words frequency parser

instantiated a WFP with a file
attribute: filename 
method: wordFrequency, totalWords, differentWords, getTopWords, printTopWords

"""

class WFP(object):
	def __init__(self, filename):
		self.filename = filename

	def processFile(self, self.filename):
		hist = dict()
		try:
			f= urllib2.urlopen(filename, "r")
			data = f.readlines()
			for line in data:
				processLine(line, hist)
		return hist
		except IOError,e:
			print e 

		f.close()


	def processLine(line, hist):


		for word in line.split():
		
			word = word.strip(string.punctuation + string.whitespace)
			word = word.lower()

			hist[word] = hist.get(word,0)+ 1

	def totalWords(hist):
		return sum(hist.values())

	def totalDifferentWords(hist):
		return len(hist)

	def mostCommonWords(hist):
		lst = list()
		for k, v in hist.items():
			lst.append((v,k))
		lst.sort(reverse=True)
		return lst

	def printMostCommonWords(hist, num=10):
		"""
		default num is 10, print the top 10 words 
		"""
		lst = mostCommonWords(hist)
		for freq, word in lst[:num]:
			print "%s    :%s " %(word, freq)




			