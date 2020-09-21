import random

n = 10**5
list = []
for i in range(n):
	list.append(random.randrange(1,20,1))

for i in range(1,len(list)):
	j = i-1
	while j >= 0 and list[j] > list[j+1]:
		list[j], list[j+1] = list[j+1], list[j]
		j -= 1


