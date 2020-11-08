def fibo(n,f):
	if n <= 1:
		return n
	elif f[n] != 0:
		return f[n]
	else: 
		f[n] = fibo(n-1,f) + fibo(n-2,f)
		return f[n]



n = 100
print(fibo(n,[0]*(n+1)))