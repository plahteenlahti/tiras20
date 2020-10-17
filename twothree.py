from heapq import heappush, heappop,heapify

def smallest(n):
	list = [1]
	heapify(list)
	for i in range(n):
		x = heappop(list)
		heappush(list,x*2)
		heappush(list,x*3)

	return heappop(list)



if __name__ == "__main__":
    print(smallest(1)) # 2
    print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552