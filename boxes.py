def count(t,x):
	t.sort()
	boxCount = 0

	j = 0 
	for i in range(len(t) - 1, -1, -1):

		if(j < i and t[i] + t[j] <= x):
			# print(f'if {t[i]}-{t[j]}')
			# boxCount += 1
			j += 1
		else:
			# print(f'else {t[i]}-{t[j]}')
			boxCount += 1

	return boxCount
	


if __name__ == "__main__":
	print(count([1,2,3,4],10)) # 2
	print(count([4,4,4,4],5)) # 4
	print(count([7,2,3,9],10)) # 3
	print(count([4,2,1,5,3],6)) #5 3
	print(count([5, 3, 1, 4, 2], 10)) # 3
	print(count([5, 4, 3, 2, 1], 5)) # 3


#CASES
# if item == boxSize
# if item < boxSize then add it,



	# 	boxCount = 0 
	# itemCount = 1
	# remaingSpace = [0]*len(t) 
	# for i in range(len(t)): 
			
	# 	j = 0 
	# 	minSpace = x + 1 
	# 	boxIndex = 0 

	# 	for j in range(boxCount): 
	# 		if (remaingSpace[j] >= t[i] and remaingSpace[j] - t[i] < minSpace) and itemCount < 2: 
	# 				boxIndex = j 
	# 				itemCount += 1
	# 				minSpace = remaingSpace[j] - t[i] 

	# 	if (minSpace == x + 1): 
	# 		remaingSpace[boxCount] = x - t[i] 
	# 		boxCount += 1 
	# 		itemCount = 1
	# 	else:
	# 		itemCount += 1
	# 		remaingSpace[boxIndex] -= t[i] 

	# return boxCount 