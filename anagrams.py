def anagram(word,place, anagrams,included,characters):
	if len(word) == place:
		anagrams.add("".join(characters))	 
	else:
		for i in range(0,len(word)):
			if not included[i]:
				included[i] = True
				characters[place] = word[i]
				anagram(word,place+1,anagrams,included,characters)
				included[i] = False
	return list(anagrams)

		


def create(s):
	anagrams = set()
	included = [False] * len(s)
	characters = [0] * len(s)
	place = 0
	anagram(s, place, anagrams,included,characters)
	return anagrams

if __name__ == "__main__":
	print(create("ab")) # [ab,ba]
	print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
	print(len(create("aybabtu"))) # 1260
