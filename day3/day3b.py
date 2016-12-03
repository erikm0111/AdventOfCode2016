content = []

with open("input.txt") as f:
	content = f.readlines()

count = 0
matrix = []
for lineStr in content:
	line = lineStr.strip()
	possible = True
	x, y, z = int(line.split()[0].strip()), int(line.split()[1].strip()), int(line.split()[2].strip())
	matrix.append([x, y, z])
	if x + y <= z:
		possible = False
	if x + z <= y:
		possible = False
	if y + z <= x:
		possible = False

col = 0
while col < 3:
	row = 0
	while row < len(content):
		possible = True
		x,y,z = matrix[row][col], matrix[row+1][col], matrix[row+2][col]
		if x + y <= z:
			possible = False
		if x + z <= y:
			possible = False
		if y + z <= x:
			possible = False
		if possible:
			count += 1
		row += 3
	col += 1

print count