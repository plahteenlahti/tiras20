

class Item: 
	def __init__(self, data): 
		self.data = data
		self.next = None

class LinkedList: 
	def __init__(self):  
		self.head = None
		
	def printList(self): 
		temp = self.head 
		while (temp): 
			print (temp.data) 
			temp = temp.next


def testList():
	linkedList = LinkedList()
	head = Item(1)

	linkedList.head = head

	lastItem = head

	for i in range(2, 10**5 +1):
		newItem = Item(i)
		lastItem.next = newItem

		lastItem = newItem

def testList2():
	linkedList = LinkedList()
	head = Item(1)

	linkedList.head = head

	lastItem = head

	for i in range(2,  10**5 +1):
		newItem = Item(i)
		lastItem.next = newItem

		lastItem = newItem

	# linkedList.printList()

	current = linkedList.head
	linkedList.head = None

	for i in range(1, 10**5 +1):
		next = current.next
		current.next = None
		current = next

	

	linkedList.printList()

if __name__ == "__main__":
		# testList()
		testList2()