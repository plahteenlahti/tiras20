def count(n):
    total = (n-1)*(n-2)//2
    two_same = 3*((n-1)//2)
    if n%3 == 0:
        two_same -= 2
    return (total-two_same)//6


if __name__ == "__main__":
	print(count(8)) # 2
	print(count(30)) # 61
	print(count(16)) # 14
	print(count(1337)) # 148296





