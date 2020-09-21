
def count(s):
	distinct = {}
	count = 0
	left = 0
	
	
	for i in range(0,len(s)):
		distinct[s[i]] = 1 if s[i] not in distinct else distinct[s[i]] + 1
		while (len(distinct) > 2):
				if(s[left] in distinct):
					distinct[s[left]] = distinct[s[left]] - 1
				if (distinct[s[left]] == 0):
						del distinct[s[left]]
				left += 1
		count += i - left + 1

	distinct = {}
	count2 = 0
	left = 0

	for i in range(0,len(s)):
		distinct[s[i]] = 1 if s[i] not in distinct else distinct[s[i]] + 1
		while (len(distinct) > 1):
				if(s[left] in distinct):
					distinct[s[left]] = distinct[s[left]] - 1
				if (distinct[s[left]] == 0):
						del distinct[s[left]]
				left += 1
		count2 += i - left + 1	

	return count - count2



if __name__ == "__main__":
	print(count("aaaa")) # 0
	print(count("abab")) # 6
	print(count("aabacba")) # 8
	print(count("babbbabbba")) # 39
	






