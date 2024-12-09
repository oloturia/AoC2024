#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		defrag = f.readlines()[0].strip()

	index_left = 0
	last_char = len(defrag)-1
	id_right = len(defrag)//2
	id_left = 0
	mov_right = 0
	checksum = 0
	end = False
	
	for place,str_fl in enumerate(defrag):
		fl = int(str_fl)
		if place // 2 == place / 2:
			for i in range(fl):
				if last_char == place:
					end = True
					break
				checksum += index_left * id_left
				index_left += 1
			if end:
				break
			id_left += 1
		else:
			for i in range(fl):
				if last_char == place:
					end = True
					break
				checksum += index_left * id_right
				index_left += 1
				mov_right += 1
				if mov_right == int(defrag[last_char]):
					mov_right = 0
					last_char -= 2
					id_right -= 1
			if end:
				break
	for i in range( int(defrag[last_char]) - mov_right):
		checksum += index_left * id_right
		index_left += 1
		
	return checksum

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 1928
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
