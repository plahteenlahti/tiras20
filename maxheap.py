from heapq import heappush
from math import log, ceil, floor,pow

def getVal(n):
	return floor(log(n, 2))

def count(n):
	counter = 0


	while n > 0 : 
		nearest = floor(pow(2, floor(log(n)/log(2))))
		if(n == nearest):
			counter += getVal(n)
			n = n - 1
		else:	
			counter += (n - nearest) * getVal(n) 
			n = nearest


	return counter


if __name__ == "__main__":
	print(count(4)) # 4
	print(count(7)) # 10
	print(count(123)) # 618
	print(count(999999999)) # 27926258178
