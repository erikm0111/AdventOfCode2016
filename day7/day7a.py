def findPatternOutsideBrackets(line):
	i = 0
	foundPattern = False
	inBrackets = False
	while i < len(line) - 4:
		if line[i] == "[":
			inBrackets = True
		if line[i] == "]":
			inBrackets = False
		if not inBrackets:
			if line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
				foundPattern = True
				break
		i += 1
	return foundPattern


def findPatternInsideBrackets(line):
	i = 0
	foundPattern = False
	inBrackets = False
	while i < len(line) - 4:
		if line[i] == "[":
			inBrackets = True
		if line[i] == "]":
			inBrackets = False
		if inBrackets:
			if line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
				foundPattern = True
				break
		i += 1
	return foundPattern


content = []

with open("input.txt") as f:
	content = f.readlines()

count = 0
for line in content:
	if findPatternOutsideBrackets(line) and not findPatternInsideBrackets(line):
		count += 1

print count