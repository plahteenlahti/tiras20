
from collections import namedtuple

def height(node):	
	if not node:
		return -1
	return 1 + max(height(node.left), height(node.right))

if __name__ == "__main__":
	Node = namedtuple("Node", ["left", "right"])
	tree = Node(None,Node(Node(None,None),Node(Node(None,Node(Node(None,None),Node(None,Node(None,Node(Node(None,None),Node(None,None)))))),None)))
	print(height(tree)) 

