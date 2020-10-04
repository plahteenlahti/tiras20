from collections import deque

def count(n):
	steps = n // 2
	twoSteps = (n +1)// 2

	if(n % 2 == 0):
		return steps + twoSteps
	return steps *twoSteps

	# return steps *twoSteps






if __name__ == "__main__":
	print(count(2)) # 2
	print(count(4)) # 4
	print(count(5)) # 6
	print(count(6)) # 6
	print(count(7)) # 12
	print(count(8)) # 8 
	print(count(31)) # 240




	# 1 2 3 4 5 6
	# 3 4 5 6 2 1
	# 5 6 2 1 4 3
	# 2 1 4 3 6 5
	# 4 3 6 5 1 2
	# 6 5 1 2 3 4

	# [3,4,5,2,1]
	# [5,2,1,4,3]
	# [1,4,3,2,5]
	# [3,2,5,4,1]
	# [5,4,1,2,3]
	# [1,2,3,4,5]


	# 1 2 3 4
	# 3 4 2 1
	# 2 1 4 3
	# 4 3 1 2
	# 1 2 3 4

	# 1 2 3 1 2 3 1 2 3
	# 3 2 1
	# 1 2 3

	# 1 2 
	# 2 1
	# 1 2