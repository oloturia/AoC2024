#!/usr/bin/python3
from functools import lru_cache

reg_list = set()

@lru_cache(maxsize=10000000)
def scanline(stripe):
	global reg_list
	count = 0

	if stripe in reg_list:
		count = 1

	for mlen in range(0,len(stripe)):
		if stripe[-mlen:] in reg_list:
			count += scanline(stripe[:-mlen])
		
	return count
	
def main(input_file):
	global reg_list
	global count
	scanline.cache_clear()
	reg_list = set()
	count = 0
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
		
	reg_list = {x.strip() for x in input_lines[0].split(",")}
	count = 0
	for i in range(2,len(input_lines)):
		count += scanline(input_lines[i])
			
	return count
	
if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 16
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"	
	print(main("INPUT"))
