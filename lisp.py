from collections import deque

def operate(operation, value, current):
	endResult = 0
	if operation == "*":
		endResult = current * value
	else:	
		endResult = current + value

	return endResult


def eval(s):
	result = 0
	operation = ''
	operations = deque()
	print(s)
	for i in range(len(s)-1, 0, -1):
		c = s[i]
		if(c == '('):
			print(operation)
			result = operate(operation, eval(s[i:]), result)
			print('recursion result',result)
		elif(c =='+'):	
			operation = '+'
		elif(c =='*'):
			operation = '*'
		elif(c == ')'):
			print('break',s)
			break
		elif(c == ' '):
			continue
		else: 
			value = int(c)
			result = operate(operation, value, result)
		

	return result

if __name__ == "__main__":
	print('result',eval("(+ 1 2 3 4 5)")) # 15
	print('result',eval("(+ 5 (* 3 2) 7)")) # 18
	print('result',eval("(* (+ (+ 1 2) 3) (+ (* 4 5) 6 2))")) # 168