def canSplit(splitHelper,array):
	sumLeft = 0
	sumRight = 0
	for i in range(len(splitHelper)):
			if(splitHelper[i] == 0):
				sumLeft += array[i]
			else: 
				sumRight += array[i]
	if (sumRight == sumLeft) : 
		return True

	else:
		return False

def search(k,splitHelper,array):
	
	if k == len(array):
		return canSplit(splitHelper,array)
	else:
		for i in range(0,2):
			splitHelper[k] = i
			if search(k+1, splitHelper, array):
				return True
			else:
				continue

	return False

def check(t):
	array = sorted(t)
	splitHelper = [0]*len(t)
	return search(0,splitHelper,array)

if __name__ == "__main__":
	print(check([3,4,5])) # False
	print(check([16,8,4,4])) # True
	print(check([9,4,8,7,6])) # True
	print(check([1,2,3,4,5,6])) # False
	print(check([1,2,3,4,5,6,7])) # True
	print(check([9, 6, 10, 10, 3])) # True
	print(check([4,4,4,6,6])) # True