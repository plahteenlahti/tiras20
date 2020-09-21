



def count(s):
	d = {}
	for c in s:
		if( d.get(c) ):
			prevValue =  d[c]
			d[c] = prevValue + 1
		else:
			d[c] = 1

	return sum(map(lambda n: n * (n + 1) // 2,d.values()))


if __name__ == "__main__":
	print(count("aaa")) # 6
	print(count("abcd")) # 4
	print(count("ababca")) # 10
	print(count("abababa")) # 10