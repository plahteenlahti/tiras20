from collections import Counter

def solve(t):
	arr = list(t)
	count = 0
	
	swaps = {
		'A':0,
		'B':0,
		'C':0
	}

	comp = sorted(list(t))
	dict = Counter(t)
 

	for i in range(0, dict['A']):
		
		if(arr[i] != comp[i]):
			swaps[arr[i]] = swaps[arr[i]] +1
			count += 1

	print('A',swaps)


	for i in range(dict['A'], dict['A'] + dict['B']):	
		
		if(arr[i] != comp[i]):
		
			if(swaps['B'] > 0):
				swaps['B'] = swaps['B'] - 1
		
			else:
				swaps[arr[i]] = swaps[arr[i]] +1
				count += 1


	# print(swaps)
	for i in range(dict['A'] + dict['B'], len(arr)):
		
		if(arr[i] != comp[i]):
			
			if(swaps['C'] > 0):
				swaps['C'] = swaps['C'] - 1
			
			elif(swaps['B'] > 0):
				swaps['B'] = swaps['B'] - 1
			
			elif(swaps['A'] > 0):
				swaps['A'] = swaps['A'] - 1

			else: 
				count += 1


	return count


if __name__ == "__main__":
	print(solve("CCAABB")) # 4 BCAABC BBAACC ABABCC 
	print(solve("CBACBA")) # 3 ABACBC AABCBC ABC
	print(solve("AAAA")) # 0
	print(solve("BCBBCAAAAABB")) # 7
	print(solve("BCCCBBACABCAABCCBCCB")) #7
	print(solve('ACBABACACACBACCBCCCB')) # 6
	print(solve('ABCABCCCACBAA')) # 6
	print(solve('AACBABCACABABCBBCBBBBCABAAACBCBABCAAACBBBCACBABABBCBCBAACCCBABCCBAABCCCACA')) #24

	# for i in range(len(t)):
	# 	#print(arr)
	# 	if(comp[i] == 'C'):
	# 		break 
	# 	if(arr[i] != comp[i]):
	# 		reverseI = len(t) -1
	# 		while(reverseI < len(t)):
	# 			if(arr[reverseI] == comp[i]):
	# 				swaps += 1
	# 				arr[reverseI] = arr[i]
	# 				arr[i] = comp[i]
	# 				break
	# 			reverseI -= 1

	# 		if(arr[i] != comp[i]):
	# 		if(arr[i] == 'B'):
	# 			start = dict['A']
	# 			while(start < len(arr)):
	# 				if(arr[start] == comp[i]):
	# 					swaps += 1
	# 					arr[start] = arr[i]
	# 					arr[i] = comp[i]
	# 					break
	# 				start += 1
			
	# 		else:
	# 			reverse = len(t) -1
	# 			while(reverse > i):
	# 				if(arr[reverse] == comp[i]):
	# 					swaps += 1
	# 					arr[reverse] = arr[i]
	# 					arr[i] = comp[i]
	# 					break
	# 				reverse -= 1
	# print("".join(arr))