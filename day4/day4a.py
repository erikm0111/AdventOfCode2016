import collections

content = []

with open("input.txt") as f:
	content = f.readlines()

sumOfIDs = 0
for line in content:
	lastDashIndex = line.strip().rfind("-")
	d = collections.defaultdict(int)
	for c in line[:lastDashIndex]:
		if c != "-":
			d[c] += 1
	sortedByFreq = sorted(d.items(), key=lambda x: x[1], reverse=True)
	mostCommon = sortedByFreq
	d2 = {}
	for value,key in mostCommon:
		if key not in d2:
			d2[key] = [value]
		else:
			d2[key].append(value)
	groupedByFreq = sorted(d2.items(), key=lambda x: x[0], reverse=True)
	checksum = ""
	for freq, letters in groupedByFreq[:5]:
		for l in sorted(letters):
			checksum += l

	#print groupedByFreq
	#print checksum
	firstBracketInd = line.strip().rfind("[")
	lastBracketInd = line.strip().rfind("]")
	realChecksum = line.strip()[firstBracketInd+1 : lastBracketInd]

	if realChecksum == checksum[:5]:
		sectorID = int(line.strip()[lastDashIndex+1 : firstBracketInd])
		sumOfIDs += sectorID

print sumOfIDs

		