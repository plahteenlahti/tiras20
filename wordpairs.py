def count(t):	
	pairs = {} 
	increments = {}

	for word in t:
		charSet = frozenset(word)
		if charSet not in pairs:
			pairs[charSet] = 0
			increments[charSet] = 0
		elif charSet in pairs and pairs[charSet] > 0:
			pairs[charSet] += 1 + increments[charSet]
			increments[charSet] += 1
		else:
			pairs[charSet] += 1
			increments[charSet] += 1





		

	return sum(pairs.values())

	
if __name__ == "__main__":
	print(count(["A","AA","AAA"])) # 3
	print(count(["A","B","C"])) # 0
	print(count(["KALA","ALA","LAKKA"])) # 1
	print(count(['CCAAB', 'ACACA']))
	print(count(['CBCCC', 'BB', 'BBC', 'CB', 'B', 'ACCC', 'BBC', 'CAB', 'ABAAB', 'BCBAC'])) # 8