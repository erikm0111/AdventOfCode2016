def moveIfPossible(letter, x, y):
	if letter == "U":
		if y > 0:
			y -= 1
	elif letter == "D":
		if y < 2:
			y += 1
	elif letter == "L":
		if x > 0:
			x -= 1
	else:
		if x < 2:
			x += 1
	return x, y


content = []
with open("input.txt") as f:
	content = f.readlines()

grid = [[1,2,3],
		[4,5,6],
		[7,8,9]]

x, y = 1, 1
for line in content:
	for letter in line.strip():
		x,y = moveIfPossible(letter, x, y)
	print grid[y][x],