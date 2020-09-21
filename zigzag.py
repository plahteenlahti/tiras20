def create(n):
	list = []
	order = 1
	for x in range(1, n+1):
		if(order == 1):
			list.insert(0,x)
			order = 0
		else:
			list.append(x)
			order = 1


	return list

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(2)) # [1,2]
    print(create(3)) # [3,1,2]
    print(create(4)) # [3,1,2,4]
    print(create(5)) # [5,3,1,2,4]