num_strings = [1,21,53,84,50,66,7,38,9]
odd_strings = []
even_strings = []
for i in num_strings:
	if i%2==0:
		even_strings.append(i)
	else:
		odd_strings.append(i)

print odd_strings
print even_strings
print '%'*20
