from heapq import heappush, heappop,heapify

def find(t, k):
	l = sorted(t)

	diffs = [(l[i + 1] - l[i], i, i + 1) for i in range(len(l) - 1)]
	heapify(diffs)

	for x in range(k):
		diff, i, j = heappop(diffs)
		if j + 1 < len(l):
			heappush(diffs, (l[j + 1] - l[i], i, j + 1))
		
	return diff

if __name__ == "__main__":
	# t = [4,1,5,2]
	# print(find(t,1),1) # 1
	# print(find(t,2),2) # 1
	# print(find(t,3),2) # 2
	# print(find(t,4),3) # 3
	# print(find(t,5),3) # 3
	# print(find(t,6),4) # 4

	# t = [10, 7, 3, 5, 4]
	# print(find(t,7),4) # 4

	# t = [6, 2, 7]
	# print(find(t,3),5)

	# t = [2, 15, 9, 16, 14, 11, 10, 8]
	# print(find(t,24),8)

	# t = [5, 4, 10, 3, 9, 1]
	# print(find(t,12), 6)

	t = [14, 4, 17, 3, 20, 7, 16, 13, 15]
	print(find(t,21), 8)

	# t =[62301, 823823, 60040, 662081, 635289, 937220, 338758, 922045, 649562, 586284, 569102, 16143, 870444, 576280, 758621, 331153, 462747, 158038, 407204, 971518, 858423, 244411, 880707, 954144, 602096, 689650, 516913, 196523, 569578, 326058, 472246, 851663, 92285, 897805, 376417, 267110, 877196, 479510, 112381, 134906]
	# print(find(t,78),54166)