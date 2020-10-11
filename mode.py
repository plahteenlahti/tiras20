class Mode:
	def __init__(self):
		self.d = {}
		self.mode = 0
		self.modeRef = 0
	
	def add(self, x): 
		self.d[x] = self.d[x] +1 if x in self.d else  1



		if(self.d[x] > self.mode): 
			self.modeRef = x
			self.mode = self.d[x]
		elif(self.d[x] == self.mode and self.modeRef > x):
			self.modeRef = x
			self.mode = self.d[x]
		return self.modeRef
			

if __name__ == "__main__":
	m = Mode()
	print(m.add(1)) # 1
	print(m.add(2)) # 1
	print(m.add(2)) # 2
	print(m.add(1)) # 1
	print(m.add(3)) # 1
	print(m.add(3)) # 1
	print(m.add(3)) # 3