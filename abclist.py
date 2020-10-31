
def KRecur(options, selected, k):
	arr = []
	if k==0:
		return selected
	else:
		for i in range(3):
			newSelected = selected + options[i]
			value = KRecur(options, newSelected, k-1)
			if(isinstance(value,list) ):
				arr += value
			else:
				arr.append(value)
	return arr 


def create(n):
	options = ['A','B','C']

	a = KRecur(options,'',n)
	return a

if __name__ == "__main__":
	print(create(1)) # [A,B,C]
	print(create(2)) # [AA,AB,AC,BA,BB,BC,CA,CB,CC]
	print(len(create(5))) # 243
	print(len(create(10))) # 243

	# A -> A -> A