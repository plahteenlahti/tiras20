def add(word, length, result):
	chars = ['A','B','C']
	if len(word) == length:
		result.append(word)
	else:
		if(len(word) > 0):
			lastChar = word[-1]
			chars.remove(lastChar)
			for char in chars:
				add(word + char, length, result)	
		else:
			add(word+"A", length, result)
			add(word+"B", length, result)
			add(word+"C", length, result)

def create(n):
	result = []
	add("", n, result)
	return result

if __name__ == "__main__":
	print(create(1)) # [A,B,C]
	print(create(2)) # [AB,AC,BA,BC,CA,CB]
	print(len(create(5))) # 48