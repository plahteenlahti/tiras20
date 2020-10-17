from collections import namedtuple

def same(node1, node2):
	if node1 == node2 == None:
		return True
	if node1 != None and node2 != None: 
		return same(node1.left, node2.left) and same(node1.right, node2.right)
      
	return False

if __name__ == "__main__":
	Node = namedtuple("Node", ["left", "right"])
	tree1 = Node(None,Node(Node(None,None),Node(None,None)))
	tree2 = Node(Node(Node(None,None),Node(None,None)),None)
	tree3 = Node(None,Node(Node(None,None),Node(None,None)))
	print(same(tree1,tree2)) # False
	print(same(tree1,tree3)) # True
	print(same(tree2,tree3)) # False