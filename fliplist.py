from collections import deque
class FlipList:
	def __init__(self):
		self.l = deque()
		self.order = 1

	def push_last(self,x):
		if(self.order == 1):
			self.l.append(x)
		else: 
			self.l.appendleft(x)

	def push_first(self,x):
		if(self.order == 1):
			self.l.appendleft(x)
		else: 
			self.l.append(x)

	def pop_last(self):
		if(self.order == 1):
			return self.l.pop()
		else: 
			return self.l.popleft()

	def pop_first(self):
		if(self.order == 1):
			return self.l.popleft()
		else: 
			return self.l.pop()

	def flip(self):
		self.order = 1 if self.order == 0 else 0



if __name__ == "__main__":
	f = FlipList()
	f.push_last(1)
	f.push_last(2)
	f.push_last(3)
	print(f.pop_first()) # 1
	f.flip()
	print(f.pop_first()) # 3