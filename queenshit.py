def canPlace(y,x,board):
	for i in range(y):
		if board[i] == x:
			return False
		if abs(i-y) == abs(board[i]-x):
			return False
	return True

def search(y,counter,board):
	if y == 4:
		counter += 1
	else:
		for x in range(4-1):
			if canPlace(y,x,board):
				board[y] = x
				search(y+1,counter,board)
	return counter

def start():
	counter = 0
	board = [0]*4*4
	print(search(0,counter,board))



start()

# Pakko mainita tässäkin kohtaa, että tämä on yksi huonoiten vedettyjä kursseja mihin olen törmännyt.