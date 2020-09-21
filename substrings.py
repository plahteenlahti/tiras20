def count(s):
	substrings = []
	substrings.append(s)

	for i in range(len(s)):
		for j in range(len(s)+1):
				sub = s[i:j]
				if(sub != ''):	
					substrings.append(sub)
	return len(list(set(substrings)))


if __name__ == "__main__":
    print(count("aaa")) # 3
    print(count("abc")) # 6
    print(count("saippuakauppias")) # 110