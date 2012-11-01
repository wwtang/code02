"""
Exercise problem: "given a word list and a text file, spell check the contents of the text file and print all (unique) words which aren't found in the word list."
"""

#function to generate a dict according the words from the dict file

def dict_list(filename):
	dict_list = []
	f = open(filename)
	data = f.readlines()
	for line in data:
		for word in line.strip().split(" "):
			dict_list.append(word)

	dict_set = set(dict_list)
	return dict_set
#read the words from the spell_check needed file into words list, which is used for checking
def words_list(words_filename):
	dict_list = []
	f = open(words_filename)
	data = f.readlines()
	for line in data:
		for word in line.strip().split(" "):
			dict_list.append(word)
	return dict_list

#unique words list

def main():
	uniqueWords = []
	filename = "/Users/qitang/Desktop/dict.txt"
	dictionary = dict_list(filename)
	words_filename = "/Users/qitang/Desktop/words.txt"
	words = words_list(words_filename)
	for word in words:
		if word not in dictionary:
			uniqueWords.append(word)
	print uniqueWords



if __name__=="__main__":
	main()