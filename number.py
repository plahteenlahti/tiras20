
def search(n, k):
	# print(n,k)
	if n == k:
		return 1

	elif(k != 0 and n > k):
		return search(n - 1, k - 1) + search(n - k, k)
	else: 
		return 0



def count(number):
	counter = 0

	k = 0
	while k < number +1: 
		counter  += search(number,k)
		k += 1
	return counter

if __name__ == "__main__":
	print(count(4)) # 5
	print(count(5)) # 7
	print(count(8)) # 22
	print(count(42)) # 53174py


	#  check -> https://en.wikipedia.org/wiki/Partition_(number_theory)
