def count(t):
	count = 0

	left = [0]*len(t)
	right = [0]*len(t)

	left[0] = t[0]
	right[-1] = t[-1]

	for i in range(1, len(t)):
		if(left[i-1] > t[i]):
			left[i] = left[i-1] 
		else:
			left[i] =  t[i]


	for i in range(len(t)-2, -1, -1):
		if(right[i+1] < t[i]):
			right[i] = right[i+1] 
		else:
			right[i] = t[i]

	# print('--')
	# print(left)
	# print(t)
	# print(right)
	# print('--')

	for i in range(len(t)-1): 
		#print('i+1',t[i+1], left[i+1], right[i+1])
		#print('i',t[i], left[i], right[i])
		if(left[i] < right[i+1] and left[i] < left[i+1] and right[i] < right[i +1]):
			#print(t[i], t[i+1])
			count += 1

	
	return count


if __name__ == "__main__":
		print(count([1,2,3,4,5]),'- 4') # 4
		print(count([5,4,3,2,1]),'- 0') # 0
		print(count([2,1,2,5,7,6,9]),'- 3') # 3
		print(count([2, 2, 2, 2, 2]),'- 0') # 0
		print(count([3, 1, 4, 2]), '- 0')