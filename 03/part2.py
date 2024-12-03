#!/usr/bin/python3
import re

def main(input_file):
	with open(input_file) as f:
		lines = [line.rstrip() for line in f.readlines()]
	
	found = list()
	for line in lines:
		found += re.findall("mul\(\d+\,\d+\)|don\'t\(\)|do\(\)",line)
	
	result = 0
	donot = True
	for instr in found:
		if instr == "do()":
			donot = True
		elif instr == "don't()":
			donot = False
		else:
			if donot:
				result += int(instr.split("(")[1].split(",")[0]) * int(instr.split("(")[1].split(",")[1][:-1])

	
	
	return result

if __name__ == "__main__":
	test_value = main("TEST2")
	expected_result = 48
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
