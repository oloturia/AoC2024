#!/usr/bin/python3
result = 0

def count_stones(stone,iters):
	global result
	if iters == 0:
		result += 1
		return

	if stone == "0":
		stone = "1"
		count_stones(stone,iters-1)
	elif len(stone)//2 == len(stone)/2:
		left_stone = str(int(stone[len(stone)//2:]))
		right_stone = str(int(stone[:len(stone)//2]))
		count_stones(left_stone,iters-1)
		count_stones(right_stone,iters-1)
	else:
		stone = str(int(stone)*2024)
		count_stones(stone,iters-1)
	return

def main(input_file):
	global result
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()][0].split()
	
	result = 0
	for stone in input_lines:
		count_stones(stone,25)
			

	return result

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 55312
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
