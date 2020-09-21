count = 0
n = 100000
for x in range(2, n +1 ):
    prime = True
    for y in range(2, x - 1):
        if x % y == 0:
            prime = False
            break
    if prime:
        count += 1

print('primes: ',count)
