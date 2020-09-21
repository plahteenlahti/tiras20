count = 0
n = 100000
a = [0]*(n)

for i in range(2,len(a)):
  if a[i] == 0:
    count += 1
    for j in range(2*i,n,i):
      a[j] = 1

print(count)