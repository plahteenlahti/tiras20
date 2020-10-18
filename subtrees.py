from collections import namedtuple


def count(node):
	if not node:
		return (0,0)


	left = count(node.left) 
	right = count(node.right)
	
	counter = left[0] + right[0] +1
	difference = abs(left[0]-right[0])
	
	print('diff:',difference)
	print('counter:',counter)
	
	
	
	
	return counter, max(difference, left[1], right[1])



def diff(node):	
	return count(node)[1]


if __name__ == "__main__":
	Node = namedtuple("Node", ["left", "right"])
	tree1 = Node(None,Node(Node(None,None),Node(None,None)))
	tree2 = Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=None))
	tree3 = Node(left=Node(left=Node(left=None, right=None), right=Node(left=None, right=None)), right=Node(left=Node(left=None, right=None), right=None))


	print(diff(tree1)) # 3 
	# print(diff(tree2)) # 4 
	# print(diff(tree3)) # 1 

