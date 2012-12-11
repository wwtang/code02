import string
CHAR = list(string.ascii_letters) + [" "]
def letter_fre(sent):
	fre = [(c, 0) for c in CHAR]
	for letter in sent:
		index = CHAR.index(letter)
		fre[index] = (letter, fre[index][1] +1)
	return fre


def main():
	sent = 'ashdfkjanmncjkashdfkjhajksdnfkjehransdfnkjasdjfnmaxnioqewuyrpiqutuasjhf'
	print letter_fre(sent)

if __name__=="__main__":
	main()