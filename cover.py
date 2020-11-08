def cover(n,m,k):
	if(k == 1):
		return 1
	else:
		return cover(n - k, m, k-1) + cover(n, m-k, k-1)

# def search(n,m,i, k):
# 	if(i == 1):
# 		return 1
# 	if n == k:
# 		return 1

# 	elif(k != 0 and n > k):
# 		return search(n - 1, m - 1) + search(n - k, k)
# 	else: 
# 		return 0


def count(n, m, k):

	return cover(n,m,k)

if __name__ == "__main__":
	print(count(2,2,4)) # 8
	print(count(2,3,3)) # 13
	# print(count(4,4,1)) # 1
	# print(count(4,3,10)) # 3146
	# print(count(4,4,16)) # 70878