from heapq import heappush, heappop,heapify,merge

class QuickAdd:
	def __init__(self):
		self.l = []

	def add(self, k, x):
		heappush(self.l, (x,k))

	def remove(self, removeK):
		sum = 0
		while removeK > 0:
			x, k = heappop(self.l)

			if k - removeK == 0:
				print('if',x,removeK,sum)
				sum += x * removeK
				break

			elif k - removeK > 0:
				print('elif',x,removeK,sum)
				sum += x * removeK
				heappush(self.l, (x, k - removeK))
				break

			else:
				print('else',x,removeK,sum)
				sum += x * k
				removeK -= k
		
		return sum
		

if __name__ == "__main__":
	q = QuickAdd()
	q.add(5,3)
	print(q.remove(2)) # 6
	print('check',q.l)
	q.add(8,1)
	print('check',q.l)
	print(q.remove(4)) # 4
	print('check',q.l)
	# print(q.l)
	print(q.remove(7)) # 13
	q.add(10**9,123)
	print(q.remove(10**9)) # 123000000000