#!/usr/bin/python3

result = 0
cache = dict()

def count_stones(stone,iters):
	global result
	global cache
	
	if (stone,iters) in cache:
		result += cache[(stone,iters)]
		return cache[(stone,iters)]
	
	if iters == 1:
		if len(stone)//2 == len(stone)/2:
			cache[(stone,1)] = 2
			result += 2
			return 2
		else:
			cache[(stone,1)] = 1
			result += 1
			return 1
			
	temp = 0
	if stone == "0":
		temp = count_stones("1",iters-1)
		cache[("0",iters)] = temp
	elif len(stone)//2 == len(stone)/2:
		left_stone = str(int(stone[len(stone)//2:]))
		temp = count_stones(left_stone,iters-1)	
		right_stone = str(int(stone[:len(stone)//2]))
		temp += count_stones(right_stone,iters-1)		
		cache[(stone,iters)] = temp
	else:	
		nstone = str(int(stone)*2024)
		temp = count_stones(nstone,iters-1)
		cache[(stone,iters)] = temp
		
	return temp

def main(input_file,iters):
	global result
	global cache
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()][0].split()
	
	cache = dict()
	result = 0
	for stone in input_lines:
		count_stones(stone,iters)
	return result

if __name__ == "__main__":
	test_value = main("TEST",25)
	expected_result = 55312
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT",75))
