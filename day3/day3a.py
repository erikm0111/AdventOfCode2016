content = []

with open("input.txt") as f:
	content = f.readlines()

count = 0
for lineStr in content:
	line = lineStr.strip()
	possible = True
	x, y, z = int(line.split()[0].strip()), int(line.split()[1].strip()), int(line.split()[2].strip())
	if x + y <= z:
		possible = False
	if x + z <= y:
		possible = False
	if y + z <= x:
		possible = False
	if possible:
		count += 1

print count