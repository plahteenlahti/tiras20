from collections import deque

def eval(s):
	spaced = s.replace('(', ' ( ')
	spaced = spaced.replace(')', ' ) ')
	splitted = spaced.split()

	values = deque()
	count = deque()
	for c in splitted: 
		if(c == '('):
			continue
		elif(c == ')'):
			i = len(values)-1
			while i >= 0:
				print(values,count)
				if(values[i] == '*'):
					values.pop()
					res = 1
					for x in count:
						res = res * x
					values.append(res)
					count.clear()
					break
				elif(values[i] == '+'):
					values.pop()
					values.append(sum(count))
					count.clear()
					break
				else: 
					val = values.pop()
					count.append(int(val))
				i -= 1
		else: 
			values.append(c)

	return values[0]

if __name__ == "__main__":
	print('result',eval("(+ 1 2 3 4 5)")) # 15
	print('result',eval("(+ 5 (* 3 2) 7)")) # 18
	print('result',eval("(* (+ (+ 1 2) 3) (+ (* 4 5) 6 2))")) # 168