def anagram(word, length, result):
	if len(word) == length:
		result.append(word)
	else:
		for perm in anagram(word[1:]):
			for i in range(len(word)):
					result.append(perm[:i] + word[0:1] + perm[i:])


def create(s):
	result = []
	anagram("", s, result)
	return result

if __name__ == "__main__":
	print(create("ab")) # [ab,ba]
	print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
	print(len(create("aybabtu"))) # 1260