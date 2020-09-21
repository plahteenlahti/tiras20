import re


def count(s):
	count = 0
	counter = 1
	prev = ''
	for c in s:
		if(c == prev):
			counter += 1
			count += counter
		else:
			counter = 1
			count += counter
			prev = c

	return count


if(__name__ == "__main__"):
	print(count("bbb")) # 6
	print(count("abbbcaa")) # 11
	print(count("abcde")) # 5
