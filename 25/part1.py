#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	keys = set()
	locks = set()
	lock_index = key_index = 0
	new_obj = list()
	for line in input_lines:
		
		if line == "#####" and (lock_index == key_index == 0):
			new_obj = [0,0,0,0,0]
			lock_index = 6
			continue
		if line == "....." and (lock_index == key_index == 0):
			new_obj = [-1,-1,-1,-1,-1]
			key_index = 6
			continue

		if lock_index > 0:
			for i,ch in enumerate(line):
				if ch == '#':
					new_obj[i] += 1
			lock_index -= 1
			if lock_index == 0:
				locks.add(tuple(new_obj))

		if key_index > 0:
			for i,ch in enumerate(line):
				if ch == '#':
					new_obj[i] +=1
			key_index -= 1
			if key_index == 0:
				keys.add(tuple(new_obj))
			
	count = 0
	for key in keys:
		for lock in locks:
			found = True
			for i in range(5):
				if key[i] + lock[i] > 5:
					found = False
			if found:
				count += 1
	
	return count

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 3
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
