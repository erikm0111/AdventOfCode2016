import collections

def decrypt(encrypted, sectorID):
	decrypted = encrypted
	i = 0
	while i < sectorID:
		j = 0
		for c in decrypted:
			if c == ' ' or c == '-':
				decrypted = decrypted[:j] + ' ' + decrypted[j+1:]
			elif chr(ord(c) + 1) > 'z':
				decrypted = decrypted[:j] + 'a' + decrypted[j+1:]
			else:
				decrypted = decrypted[:j] + chr(ord(c)+1) + decrypted[j+1:]
			j += 1
		i += 1
	return decrypted	


content = []
decryptedContent = ""

with open("input.txt") as f:
	content = f.readlines()

for line in content:
	lastDashIndex = line.strip().rfind("-")
	firstBracketInd = line.strip().rfind("[")
	lastBracketInd = line.strip().rfind("]")

	sectorID = int(line.strip()[lastDashIndex+1 : firstBracketInd])
	encrypted = line.strip()[:lastDashIndex]
	decrypted = decrypt(encrypted, sectorID)
	#print decrypted
	decryptedContent += decrypted + str(sectorID) + "\n"

print decryptedContent

with open("output.txt", "w") as f2:
	f2.write(decryptedContent)

"""
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

	firstBracketInd = line.strip().rfind("[")
	lastBracketInd = line.strip().rfind("]")
	realChecksum = line.strip()[firstBracketInd+1 : lastBracketInd]

	if realChecksum == checksum[:5]:
		sectorID = int(line.strip()[lastDashIndex+1 : firstBracketInd])
		sumOfIDs += sectorID
"""