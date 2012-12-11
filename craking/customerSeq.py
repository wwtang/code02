class CustomSeq():
	def __len__(self):
		return 5

	def __getitem__(self,index):
		return "x{0}.format(index)"


class FunkyBackwards(CustomSeq):
	def __reversed__(self):
		return "BACKWARDS"


normal_list=[1,2,3,4,5]


for seq in normal_list, CustomSeq(), FunkyBackwards():
	print("\n{}:".format(seq.__class__.__name__), end="")
	for item in reversed(seq):
		print(item, end= ", ")