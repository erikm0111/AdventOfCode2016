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

def calculateCoords(direction, value):
	global x,y
	if direction=="north":
		y += value
	elif direction=="east":
		x += value
	elif direction=="south":
		y -= value
	else:
		x -= value

def manhattanDistance(x, y):
	return abs(x) + abs(y)

content = []
with open("input.txt") as f:
	content = f.readlines()

x = 0
y = 0
direction = "north"

for el in content[0].split(","):
	side = el.strip()[0]
	value = el.strip()[1:]
	direction = nextOption(direction, side)
	calculateCoords(direction, int(value))
	
print "Distance: ", manhattanDistance(x,y)


