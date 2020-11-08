def search(k,n,a,b):
	if a == n or b == n:
		return 1
	else: 
		f[n] = search(n-1,f) + search(n-2,f)
		return f[n]

def count(n,a,b):
	counter = [0]*
	search(k,n,a,b,counter)

if __name__ == "__main__":
	print(count(4,1,2)) # 5
	print(count(10,2,5)) # 2
	print(count(10,6,7)) # 0
	print(count(30,3,5)) # 58
	print(count(50,2,3)) # 525456