def count(s):
	abc = {'A':0,'B':0,'C':0}
	neg = {'A':0,'B':0,'C':0}
	count = 0

	for i in range(len(s)):		
		abc[s[i]] += 1
		neg[s[i]] += 1

		if abc['A'] == abc['B'] == abc['C']:
			count += count + 1

		if neg[s[i]] > 1:
			neg[s[i]] -= 1

		if neg['A'] == neg['B'] == neg['C']:
			print(neg)
			count = count + 1

	


	# print(abc,neg)
	return count

if __name__ == "__main__":
	print(count("CCAABB"),f'{count("CCAABB") == 1}') # 1
	print(count("CBACBA"),f'{count("CBACBA") == 5}') # 5
	print(count("AAABBC"),f'{count("AAABBC") == 0}') # 0
	print(count("CCBCCCABB"),f'{count("CCBCCCABB") == 1}') # 1