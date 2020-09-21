import random

n = 10**3
list = []
for i in range(n):
	list.append(random.randrange(1,20,1))


middleIndex = len(list)//2

aList = list[:middleIndex]
bList = list[middleIndex:]

help = [None] * len(list)


def sort(a,b):
	if a == b:
		return
	k = (a+b)//2
	index = (len(a) + len(b))//2
	sort(a,k)
	sort(k+1,b)
	merge(a,k,k+1,b)


def merge(a1, b1, a2, b2):
	a = a1, b = b2
	for i in range(a,b):
		if a2 > b2 or (a1 <= b1 and list[a1] <= list[a2]):
			help[i] = list[a1]
			a1 += 1
		else:
			help[i] = list[a2]
			a2 += 1
	for i in range(a,b):
		list[i] = help[i]



sort(aList,bList)
