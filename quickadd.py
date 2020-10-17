from heapq import heappush, heappop,heapify,merge

class QuickAdd:
	def __init__(self): self.l = []

	def add(self, k, x):
		self.l = list(merge(self.l,[x] * k))

	def remove(self, k):
		sum = 0
		for i in range(k):
			sum += heappop(self.l)
		return sum

if __name__ == "__main__":
	q = QuickAdd()
	q.add(5,3)
	print(q.remove(2)) # 6
	q.add(8,1)
	print(q.remove(4)) # 4
	print(q.remove(7)) # 13
	q.add(10**9,123)
	print(q.remove(10**9)) # 123000000000