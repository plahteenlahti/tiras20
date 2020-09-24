def getIntervals(t):
	sortedList = sorted(t)
	start = sortedList[0]
	prev = sortedList[0]

	for i in sortedList[1:]:
		if(i == prev +1):
			prev = i
		else:
			yield [start, prev] 
			start = prev = i 

	yield [start, prev] 

def count(t):
	intervals = getIntervals(t)

	return len(list(intervals))



if __name__ == "__main__":
    print(count([4,1,5,3])) # 2
    print(count([4,2,1,3])) # 1
    print(count([5,2,7,6,3,9])) # 3

