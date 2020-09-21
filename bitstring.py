def calculate(s):
	count = 0
	alteredCount = 1

	value = '0' if s[0] == '1' else '1'
	alteredString = value + s[1:]

	prev = s[0]
	for i in range(1,len(s)):
		if(prev != s[i]):
			prev = s[i]
		elif(prev == s[i]):
			value = '0' if s[i] == '1' else '1' 
			prev = value 
			count += 1

	prev = alteredString[0]
	for i in range(1,len(alteredString)):
		if(prev != alteredString[i]):
			prev = alteredString[i]
		elif(prev == alteredString[i]):
			value = '0' if s[i] == '1' else '1' 
			prev = value 
			alteredCount += 1

	return min(count, alteredCount)

if __name__ == "__main__":
	print(calculate("1010")) # 0
	print(calculate("1111")) # 2
	print(calculate("10010001")) # 3
	print(calculate("00100")) # 2




	# mutationCountFromLeft = 0
	# mutationCountFromRight = 0
	# prevLeft = s[0]
	# prevRight = s[-1]
	# string1 = s
	# string2 = s
	
	# for i in range(1, len(string1)):
	# 	if(prevLeft != string1[i]):
	# 		prevLeft = string1[i]
	
	# 	elif(prevLeft == string1[i]):
	# 		value = '0' if string1[i] == '1' else '1' 
	# 		string1 = s[:i] + value + string1[i+1:]
	# 		prevLeft = string1[i] 
	# 		mutationCountFromLeft += 1

	# for i in range(len(string2)-2,-1, -1):
	# 	if(prevRight != string2[i]):
	# 		prevRight = string2[i]
	
	# 	elif(prevRight == string2[i]):

	# 		value = '0' if string2[i] == '1' else '1' 
	# 		string2 = string2[:i] + value + string2[i+1:]
	# 		prevRight = string2[i] 
	# 		mutationCountFromRight += 1