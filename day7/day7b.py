def isSSL(line):
	i = 0
	foundSSL = False
	inBrackets = False
	outsidePatterns = []
	while i < len(line) - 2:
		if line[i] == "[":
			inBrackets = True
		if line[i] == "]":
			inBrackets = False
		if not inBrackets:
			if line[i] == line[i+2] and line[i] != line[i+1] and line[i+1] != '[' and line[i+1] != ']':
				outsidePatterns.append(line[i] + line[i+1] + line[i+2])
		i += 1

	i = 0
	inBrackets = False
	while i < len(line) - 2:
		if line[i] == "[":
			inBrackets = True
		if line[i] == "]":
			inBrackets = False
		if inBrackets:
			if line[i] == line[i+2] and line[i] != line[i+1] and line[i+1] != '[' and line[i+1] != ']':
				for pattern in outsidePatterns:
					if pattern[0] == line[i+1] and pattern[1] == line[i]:
						foundSSL = True
						break
				if foundSSL:
					break
		i += 1

	return foundSSL


content = []

with open("input.txt") as f:
	content = f.readlines()

count = 0
for line in content:
	if isSSL(line):
		count += 1

print count