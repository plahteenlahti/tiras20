from heapq import heappush, heappop, _heappop_max,_heapify_max

def testHeap():
	q = []
	for i in range(1,11):
		heappush(q,i)


	heappop(q)
	heappop(q)
	heappop(q)
	return q

class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)

class MinHeap(object):
	def __init__(self): self.h = []
	def heappush(self, x): heappush(self.h, x)
	def heappop(self): return heappop(self.h)
	def __getitem__(self, i): return self.h[i]
	def __len__(self): return len(self.h)


class MaxHeap(MinHeap):
	def heappush(self, x): heappush(self.h, MaxHeapObj(x))
	def heappop(self): return heappop(self.h).val
	def __getitem__(self, i): return self.h[i].val
	def __str__(self): return self.h.__str__()

def testMaxHeap():
	maxh = MaxHeap()
	for i in range(1,11):
		maxh.heappush(i)


	maxh.heappop()
	maxh.heappop()
	maxh.heappop()

	for i in range(len(maxh)):
		print(maxh.__getitem__(i))


      


if __name__ == "__main__":
	# print(testHeap())
	testMaxHeap()


