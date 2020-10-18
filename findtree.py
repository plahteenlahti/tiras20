from collections import namedtuple

def same(node1, node2):
	if node1 == node2 == None:
		return True
	if node1 != None and node2 != None: 
		return same(node1.left, node2.left) and same(node1.right, node2.right)
	return False


def count(node1, node2):
	if node2==None:
		return 0		
	return same(node1, node2) + count(node1, node2.left) + count(node1, node2.right)

if __name__ == "__main__":
	Node = namedtuple("Node", ["left", "right"])
	tree1 = Node(Node(None,None),Node(None,None))
	tree2 = Node(None,Node(Node(None,None),Node(None,None)))
	print(count(tree1,tree2)) # 1