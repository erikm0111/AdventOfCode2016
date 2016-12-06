from collections import defaultdict

content = []

with open("input.txt") as f:
	content = f.readlines()

messageLength = len(content[0])
dicts = []
i = 0
while i < messageLength:
	letterDict = defaultdict(lambda: 0)
	dicts.append(letterDict)
	i += 1

for line in content:
	j = 0
	while j < messageLength:
		char = line[j]
		dict1 = dicts[j]
		dict1[char] += 1
		dicts[j] = dict1
		j += 1

i = 0
while i < messageLength:
	print sorted(dicts[i].items(), key=lambda x: x[1], reverse=True)[0][0] ,
	i += 1

