def canPlace(y,x,board):
	for i in range(0,y):
		if board[i] == x:
			return False
		if abs(i-y) == abs(board[i]-x):
			return False
	return True

def search(y,n,board,counter):
	if y == n:
		counter[0]+=1
		print('vittua?',counter)
	else:
		for x in range(n):
			if canPlace(y,x,board):
				board[y] = x
				search(y+1,n,board,counter)
	

def start():
	n = 11
	counter = [0]
	board = [-1] * n
	print(search(0,n,board,counter))



start()

