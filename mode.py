class Mode:
	def __init__(self):
		self.d = {}
		self.smallest = 0
	
	def add(self, x): 
		self.d[x] = self.d[x] +1 if x in self.d else  1

		return max(self.d, key=self.d.get)
			

if __name__ == "__main__":
	m = Mode()
	print(m.add(1)) # 1
	print(m.add(2)) # 1
	print(m.add(2)) # 2
	print(m.add(1)) # 1
	print(m.add(3)) # 1
	print(m.add(3)) # 1
	print(m.add(3)) # 3