from collections import deque

def listTest(n):

	l = list()

	for i in range(1,n+1):
		l.append(i)

	for i in range(1,n+1):
		l.pop(len(l)-1)

def listTest2(n):
	l = deque()

	for i in range(1,n+1):
		l.append(i)

	for i in range(1,n+1):
		l.pop()


def listTest3(n):
	l = list()

	for i in range(1,n+1):
		l.append(i)

	for i in range(1,n+1):
		l.pop(0)


def listTest4(n):
	l = deque()

	for i in range(1,n+1):
		l.append(i)

	for i in range(1,n+1):
		l.popleft()



if __name__ == "__main__":
	# listTest(10**5)
	listTest2(10**5)
	# listTest3(10**5)
	# listTest4(10**5)