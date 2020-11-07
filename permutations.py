def search(k,n,included,values):
	if k == n:
		print( values)
	else:
		for i in range(1, n+1):
			if not included[i-1]:
				included[i-1] = True
				values[k] = i
				search(k+1,n,included,values)
				included[i-1] = False

	


def getPermutations():
	n = 9
	included = [False]* (n)
	row = 1
	values = [0] * n
	search(0,n,included,values)

getPermutations()

## Run with python3 permutations.py > output.txt