def partition(l):
	if len(l)<=1:
		return l
	#set the last element as pivot
	pivot = l[-1];

	i = -1;
	for j in range(len(l)-2):
		if l[j] <= pivot:
			i +=1
			l[j], l[i] = l[i], l[j]
	print pivot, l[i+1], i+1
	l[-1], l[i+1] = l[i+1], l[-1]


	return l



def main():
	l = [2,8,7,1,3,5,6,4]
	print "we are here"
	print partition(l)

if __name__=="__main__":
	main()
