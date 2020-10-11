def count(s):
	pos = {}
	pos[0,0] = 1

	xPosition = 0
	yPosition = 0
	for c in s:
		if c == 'R':
			xPosition += 1
		elif c == 'L':
			xPosition -= 1
		elif c == 'U':
			yPosition += 1
		elif c == 'D':
			yPosition -= 1

		pos[xPosition,yPosition] = 1

	return len(pos)

print(count("LL")) # 3
print(count("UUDLRR")) # 5
print(count("UDUDUDU")) # 2