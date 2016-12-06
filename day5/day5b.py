import hashlib
import re
puzzle_input = "reyedfim"
m = hashlib.md5()

pattern = re.compile("^0{5}")
pattern2 = re.compile("[0-7]")

count = 0
password = "________"
while True:
	m = hashlib.md5()
	door_id = puzzle_input + str(count)
	m.update(door_id)
	hashed = str(m.hexdigest())
	#print hashed
	if pattern.match(hashed):
		position = hashed[5]
		if pattern2.match(position):
			position = int(hashed[5])
			char = hashed[6]
			password = password[:position] + char + password[position+1:]
			print password
	count += 1
	if "_" not in password:
		break
