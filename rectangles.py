def area(rec1, rec2, rec3):
	
	abc = 0

	print(intersects(rec1,rec2))
	print(intersects(rec1,rec3))
	print(intersects(rec2,rec3))

	if(intersects(rec1,rec2) and intersects(rec1,rec3) and intersects(rec2,rec3)):
		dx = min(rec1[2], rec2[2], rec3[2]) - max(rec1[0], rec2[0], rec3[0])
		dy = min(rec1[1], rec2[1], rec3[1]) - max(rec1[3], rec2[3], rec3[3])
		abc = abs(dx*dy)

	print('intersection(rec1, rec2)',intersection(rec1, rec2))
	print('intersection(rec1, rec3)',intersection(rec1, rec3))
	print('intersection(rec2, rec3)',intersection(rec2, rec3))
	print('abc',abc)

	totalArea = (calculateArea(rec1)+calculateArea(rec2)+calculateArea(rec3)) -intersection(rec1, rec2) - intersection(rec1, rec3) - intersection(rec2, rec3) + abc


	return totalArea

def intersection(rec1,rec2):
	if(intersects(rec1,rec2)):
		intersectionY = min(rec1[1], rec2[1]) - max(rec1[3], rec2[3])
		intersectionX = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
		return abs(intersectionX*intersectionY)
	return 0


def intersects(rec1,rec2):
	if (rec1[0] < rec2[2] and rec1[2] > rec2[0] and
    rec1[1] > rec2[3] and rec1[3] < rec2[1]):
		return True
	return False

# def contains(r1, r2):
#   if(r1[0] < r2[0] < r2[2] < r1[2] and r1[1] < r2[1] < r2[3] < r1[3]):
# 		return True
# 	return False

def calculateArea(rec):
    return abs((rec[2]-rec[0]) * (rec[3]-rec[1]))

if __name__ == "__main__":
    # rec1 = (-1,1,1,-1)
    # rec2 = (0,3,2,0)
    # rec3 = (0,2,3,-2)
    # print(area(rec1,rec2,rec3)) # 16
    # rec1 = (1,2,3,0)
    # rec2 = (-3,2,1,-3)
    # rec3 = (-2,-2,2,-3)
    # print(area(rec1,rec2,rec3)) # 25
    # rec1 = (2,-1,3,-3)
    # rec2 = (0,2,3,0)
    # rec3 = (-3,0,1,-1)
    # print(area(rec1,rec2,rec3)) # 12
    rec1 = (0,3,3,2)
    rec2 = (-1,3,2,-3)
    rec3 = (-1,0,2,-3)
    print(area(rec1,rec2,rec3)) # 19
