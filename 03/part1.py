#!/usr/bin/python3
import re

def main(input_file):
	with open(input_file) as f:
		lines = [line.rstrip() for line in f.readlines()]
	
	found = list()
	
	for line in lines:
		found += re.findall("mul\(\d+\,\d+\)",line) 
	result = 0
	for muls in found:
		result += int(muls.split("(")[1].split(",")[0]) * int(muls.split("(")[1].split(",")[1][:-1])
	return result

if __name__ == "__main__":
	test_value = main("TEST1")
	expected_result = 161
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
