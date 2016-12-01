import math

def nextOption(direction, side):
	if direction=="north":
		if side == "R":
			return "east"
		else:
			return "west"
	elif direction=="east":
		if side == "R":
			return "south"
		else:
			return "north"
	elif direction=="south":
		if side == "R":
			return "west"
		else:
			return "east"
	else:
		if side == "R":
			return "north"
		else:
			return "south"

def checkIfVisited():
	global x,y,visited
	if (x,y) in visited:
		return True
	else:
		visited.append((x,y))
		return False

def calculateCoords(direction, value):
	global x,y,visited
	i = 1
	stop = False
	if direction=="north":
		while i <= value:
			y += 1
			stop = checkIfVisited()
			if stop:
				break
			i += 1
	elif direction=="east":
		while i <= value:
			x += 1
			stop = checkIfVisited()
			if stop:
				break
			i += 1
	elif direction=="south":
		while i <= value:
			y -= 1
			stop = checkIfVisited()
			if stop:
				break
			i += 1
	else:
		while i <= value:
			x -= 1
			stop = checkIfVisited()
			if stop:
				break
			i += 1
	return stop

def manhattanDistance(x, y):
	return abs(x) + abs(y)

visited = []
content = []
with open("input.txt") as f:
	content = f.readlines()

x = 0
y = 0
direction = "north"
stop = False

for el in content[0].split(","):
	side = el.strip()[0]
	value = el.strip()[1:]
	direction = nextOption(direction, side)
	stop = calculateCoords(direction, int(value))
	if stop:
		break

	
print "Distance: ", manhattanDistance(x,y)


