def count(t):
	last = {}
	pos = -1 

	result = 0
	for i in range(len(t)):
		if t[i] not in last:
			result += i - pos
			last[t[i]] = i
		elif t[i] in last:
			pos = max(pos, last[t[i]])			
			result += i - pos
			last[t[i]] = i
		print(t[i], pos +1, result)
	return result



if __name__ == "__main__":
	print(count([1,2,3,4,5])) # 15
	print(count([1,1,1,1,1])) # 5
	print(count([1,2,1,1,2])) # 8
						#  0 0 1 3 3	
						#  1 3 5 6 8