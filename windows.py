


def count(t,k):
	map = {} 
	count = 0
	distincts = []

	for i in range(k): 
		if t[i] not in map: 
			count += 1
			map[t[i]] = 1
		else:
			map[t[i]] += 1

	distincts.append(count)

	for i in range(k, len(t)): 
		if map[t[i - k]] == 1:
			count -= 1
		map[t[i - k]] = map[t[i - k]] - 1
	
		if t[i] not in map or map[t[i]] == 0: 
				count += 1
		map[t[i]] = 1 if t[i] not in map else map[t[i]] + 1


		distincts.append(count)


	return distincts

	

if __name__ == "__main__":
	print(count([1,1,2,2],2)) # [1,2,1]
	print(count([1,1,1,1],4)) # [1]
	print(count([1,2,3,2,2,2],3)) # [3,2,2,1]
	print(count([3,3,2,3,3,3,1,2,2,3],6))
						#  1 1 2 2 2 2 