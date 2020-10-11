##apina
## 97 112 105 110 97


def getHash(s):
	count = 0

	for i in range(len(s)):
		count += (7**(len(s)-i -1))*ord(s[i])

	return count % 10**5

print(getHash('testi'))
print(getHash('apina'))
print(getHash('banaani'))
print(getHash('cembalo'))
