from collections import deque  

def count(s):
	d = deque()
	d.append(s[0])

	for i in range(1,len(s)):
		if(len(d) != 0 and d[-1] == '(' and s[i] == ')'):
			d.pop()
		else:
			d.append(s[i])

	return len(d)

if __name__ == "__main__":
	print(count("(()())")) # 0
	print(count("))))))")) # 6
	print(count("((())(")) # 2
	print(count("()()()()()"))