

def fibo(n):
	fibo.counter += 1
	if n <= 1:
		return n
	else:
		return fibo(n-1) + fibo(n-2)

fibo.counter = 0

print(fibo(40))
print(fibo.counter)

