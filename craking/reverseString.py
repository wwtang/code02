"""

little python trick way 
"""


def reverses(s):
	if len(s) <2:
		return s

	lst = list(s)

	i = 0
	j = len(s)-1

	while i<=j:
		lst[i],lst[j] = lst[j],lst[i]
		i +=1
		j -=1

	return "".join(lst)


def reverses1(s):
	return s[::-1]



def main():
	s = "abc"
	s1=  ""
	s2 = "asdflkaksjdf"

	print reverses(s)
	print reverses1(s)
	print 
	print reverses(s1)
	print reverses1(s1)
	print
	print reverses(s2)
	print reverses1(s2)
if __name__=="__main__":
	main()