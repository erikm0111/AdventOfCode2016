import hashlib
import re
puzzle_input = "reyedfim"
m = hashlib.md5()

pattern = re.compile("^0{5}[^0]")

count = 0
password = ""
while True:
	m = hashlib.md5()
	door_id = puzzle_input + str(count)
	m.update(door_id)
	hashed = str(m.hexdigest())
	#print hashed
	if pattern.match(hashed):
		password += hashed[5]
		print password
	count += 1
	if len(password) == 8:
		break
