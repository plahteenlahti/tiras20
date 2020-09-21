
def area(rec1, rec2, rec3):
	x1 = min(rec1[0],rec2[0],rec3[0])
	y1 = max(rec1[1],rec2[1],rec3[1])
	x2 = max(rec1[2],rec2[2],rec3[2])
	y2 = min(rec1[3],rec2[3],rec3[3])

	rows = {}
	for x in list(range(x1,x2)):
		columns = {}
		for y in list(range(y1,y2,-1)):
			columns[y] = 0
		rows[x] = columns

	for x in range(rec1[0],rec1[2]):
		for y in range(rec1[1],rec1[3],-1):
			rows[x][y] = 1

	for x in range(rec2[0],rec2[2]):
		for y in range(rec2[1],rec2[3],-1):
			rows[x][y] = 1

	for x in range(rec3[0],rec3[2]):
		for y in range(rec3[1],rec3[3],-1):
			rows[x][y] = 1			
	

	return sum([sum(rows[i].values()) for i in rows])

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16
		#x1 , y1, x2 ja y2