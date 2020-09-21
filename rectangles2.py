
def area(rec1, rec2, rec3):
	left = min(rec1[0], rec1[2],rec2[0], rec2[2],rec3[0], rec3[2])
	right= max(rec1[0], rec1[2],rec2[0], rec2[2],rec3[0], rec3[2])
	top = max(rec1[1], rec1[3],rec2[1], rec2[3],rec3[1], rec3[3])
	bottom = min(rec1[1], rec1[3],rec2[1], rec2[3],rec3[1], rec3[3])


	totalArea = abs(left - right) * abs(top - bottom)
	
	aArea = abs(rec1[0] - rec1[2]) * abs(rec1[1] - rec1[3])
	bArea = abs(rec2[0] - rec2[2]) * abs(rec2[1] - rec2[3])
	cArea = abs(rec3[0] - rec3[2]) * abs(rec3[1] - rec3[3])

	abIntersection = (min(rec1[2],rec2[2]) - max(rec1[0], rec2[0])) * (min(rec1[1],rec2[1]) - max(rec1[3], rec2[3]))

	acIntersection = (min(rec1[2],rec3[2]) - max(rec1[0], rec3[0])) * (min(rec1[1],rec3[1]) - max(rec1[3], rec3[3]))

	bcIntersection = (min(rec2[2],rec3[2]) - max(rec2[0], rec3[0])) * (min(rec2[1],rec3[1]) - max(rec2[3], rec3[3]))



	
	return totalArea

if __name__ == "__main__":
		rec1 = (2,-1,3,-3)
		rec2 = (0,2,3,0)
		rec3 = (-3,0,1,-1)
		print(area(rec1,rec2,rec3))


		# rec1 = (-1,1,1,-1)
    # rec2 = (0,3,2,0)
    # rec3 = (0,2,3,-2)
		# rec1 = (-1,2,2,-1)
    # rec2 = (-1,2,2,-1)
    # rec3 = (-1,2,2,-1)



