"""
build a binary tree from inOrder and PreOrder list

"""
def build(preorder, inorder):
    if len(preorder) == 0:
        return None

    root = preorder[0]
    left_count = inorder.index(root) # number of items in left sub-tree

    left_inorder = inorder[0:left_count]
    left_preorder = preorder[1:1+left_count]

    right_inorder = inorder[1+left_count:]
    right_preorder = preorder[1+left_count:]

    return [root, build(left_preorder, left_inorder), build(right_preorder, right_inorder)]


def buildPostAndInorder(postorder, inorder):
	if len(postorder) ==0:
		return None

	root = postorder[-1]

	count = inorder.index(root)

	leftInorder = inorder[:count]
	leftPostorder = postorder[:count]

	rightInorder = inorder[count+1:]
	rightPostorder = postorder[count:-1]

	return [root, buildPostAndInorder(leftPostorder, leftInorder), buildPostAndInorder(rightPostorder,rightInorder)]

def main():
	preorder = ['A', 'B', 'D', 'E', 'C', 'F']
	inorder  = ['D', 'B', 'E', 'A', 'C', 'F']
	postorder = ['D','E','B','F','C','A']

	print build(preorder, inorder)
	print buildPostAndInorder(postorder, inorder)

if __name__=="__main__":
	main()