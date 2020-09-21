def getValue(value):
	count = 1
	prev = ''
	incomplete = ''
	for i in range(len(value), 0 , -1):
		curr = value[i-1]
		# print(curr, prev, count)
		if(curr == prev): 
			# print('curr == prev)')
			count += 1
		elif(prev != '' and prev != curr):
			# print('prev != '' and prev != curr')
			incomplete = str(count) + prev + incomplete 
			count = 1
		elif(i == 0): 
			# print('i == 0')
			incomplete = str(count) + curr + incomplete
		# else: 
			# print('else')
			# count += 1
		prev = curr	
	incomplete = str(count) + prev + incomplete
	return incomplete



def generate(n):
	seed = '1'	
	if(n == 1):
		return '1'

	for i in range(1,n):
		seed = getValue(seed)

	return seed


if __name__ == "__main__":
    # print(generate(1)) # 1
    print(generate(2)) # 11
    print(generate(3)) # 21
    print(generate(4)) # 1211
    print(generate(5)) # 111221


		# print(getValue('1'))
		# print(getValue('111'))
		# print(getValue('2221111'))