
from collections import namedtuple


def count(node, level):
	if not node:
		return 0
	elif(level - 1 != 0):
		return count(node.left, level - 1) + count(node.right, level - 1)
	elif node:
		return 1
	elif node.left and node.right:
		count(node.left, 1) + count(node.right, 1) 
	else:
		return 0

		
if __name__ == "__main__":
	Node = namedtuple("Node", ["left", "right"])
	tree = Node(None,Node(Node(None,None),Node(None,None)))
	print(count(tree,1)) # 1
	print(count(tree,2)) # 1
	print(count(tree,3)) # 2
	print(count(tree,4)) # 0