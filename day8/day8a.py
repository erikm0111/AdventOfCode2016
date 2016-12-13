def action(screen, line, height, width):
	if line.startswith("rect"):
		w, h = line.split()[1].split("x")[0], line.split()[1].split("x")[1] 
		i = 0
		while i < int(h):
			j = 0
			while j < int(w):
				screen[i][j] = "#"
				j += 1
			i += 1
	elif line.startswith("rotate"):
		byWhitespaces = line.split()
		if byWhitespaces[1] == 'row':
			# to right
			index = int(byWhitespaces[2].split('=')[1])
			offset = int(byWhitespaces[4])
			newRow = []
			i = width - offset
			while i < width:
				newRow.append(screen[index][i])
				i += 1
			i = 0
			while i < width - offset:
				newRow.append(screen[index][i])
				i += 1
			i = 0
			while i < width:
				screen[index][i] = newRow[i]
				i += 1
		elif byWhitespaces[1] == 'column':
			# to down
			index = int(byWhitespaces[2].split('=')[1])
			offset = int(byWhitespaces[4])
			newColumn = []
			i = height - offset
			while i < height:
				newColumn.append(screen[i][index])
				i += 1
			i = 0
			while i < height - offset:
				newColumn.append(screen[i][index])
				i += 1
			i = 0
			while i < height:
				screen[i][index] = newColumn[i]
				i += 1


def initializeScreen():
	screen = []
	i = 0
	while i < height:
		screen.append([])
		j = 0
		while j < width:
			screen[i].append('.')
			j += 1
		i += 1
	return screen


content = []
with open("input.txt") as f:
	content = f.readlines()

height = 6
width = 50

screen = initializeScreen()
for line in content:
	action(screen, line, height, width)

switchedOn = 0
for line in screen:
	for char in line:
		if char == '#':
			switchedOn += 1

print switchedOn
