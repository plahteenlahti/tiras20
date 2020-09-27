def changes(t):

	inversions = 0
	for i in range(1, len(t)):
		requiredChanges = 0
		if(t[i] < t[i-1]):
			requiredChanges =  t[i-1] - t[i] 
			t[i] = t[i] + requiredChanges
			inversions += requiredChanges

	return inversions

if __name__ == "__main__":
	print(changes([3,2,5,1,7])) # 5
	print(changes([1,2,3,4,5])) # 0
	print(changes([3,3,1,4,2])) # 4
	print(changes([7, 1, 2, 5, 3, 6, 3])) #22