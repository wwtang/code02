"""
Write a program that reads a file, breaks each line into words, 
strips whitespace and punctuation from the words, and converts them to lowercase.
"""
import string
from string import *
import pprint as pp
import urllib2


def wordParser(fileName):
	result = []
	try:	
		f = open(fileName, "r")
		data = f.readlines()
		
		for line in data:
			
			result.append(removePunc(line).strip())

		return result
	except IOError,e:
		print e


def removePunc(str):
	# lst = list(str)
	# for c in lst:
	# 	if c in string.punctuation:
	# 		lst.remove(c)
	# 		print c
	inTab = string.punctuation
	outTab = " "*len(inTab)

	transTab = maketrans(inTab, outTab)

	modifiedStr = str.translate(transTab)

	return modifiedStr



def processFile(filename):
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

def markovAnalysis(filename):
	"""
	markvo analysis should check the whole text at one time, because if we check
	the text line by line, the new line will not be append to the previous word, 
	which will decrease the accuracy.
	"""
	hist = dict()
	if filename[:4] == "http":
		data = openUrlFile(filename)
	else:
		data = openLocalFile(filename)

	#data = urllib2.urlopen(filename).read()
	# for word in data.split():
	# 	word = word.strip(string.punctuation + string.whitespace)
	# 	word.lower()
	# 	hist[word] = []
	wordList = data.split()
	#print wordList

	for i in range(len(wordList)-1):
		
		wordList[i] = modifyWord(wordList[i])

		if wordList[i] not in hist:

			hist[wordList[i]] = [wordList[i+1]]
		else:
			hist[wordList[i]].append(wordList[i+1])

	return hist

def modifyWord(word):
	return word.strip(string.punctuation + string.whitespace).lower()

def openLocalFile(filename):
	try:
		f = open(filename)
		data = f.read()
	except IOError,e:
		print e 
	f.close()
	return data

def openUrlFile(filename):
	try:
		f = urllib2.urlopen(filename)
		data = f.read()
	except IOError,e:
		print e 
	f.close()
	return data


def printTopHist(hist, num=10):
	for item in hist.items()[:num]:
		print item
def printAllHist(hist):
	for item in hist.items():
		print item[0], item[1]

def main():

	fileName = "/Users/qitang/Desktop/test.txt"

	url = "http://www.awesomefilm.com/script/emma.txt"
	# hist = processFile(url)
	# print "The number of total words in emma is:"

	# print totalWords(hist)
	# print 
	# print "the number of total different words is: "
	# print totalDifferentWords(hist)
	# print "the top ten words in emma:"
	# print printMostCommonWords(hist)

	hist1 = markovAnalysis(fileName)
	printTopHist(hist1)
	printAllHist(hist1)

	# pp.pprint(wordParser(fileName))
	# str = "string.capwords(s[, sep])"
	# print removePunc(str)
	# print processFile(url)

if __name__=="__main__":
	main()