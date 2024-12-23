#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [int(line.rstrip()) for line in f.readlines()]

	prune = lambda a : a % 16777216

	result = 0
	for i in range(0,2000):
		for el,line in enumerate(input_lines):

			number = line
			numberA = line
			numberA *= 64
			number = number ^ numberA
			number = prune(number)
			
			numberB = number
			numberB = numberB//32
			number = number ^ numberB
			number = prune(number)
			
			numberC = number
			numberC *= 2048
			number = number ^ numberC
			number = prune(number)
			
			input_lines[el] = number
	
	for line in input_lines:
		result += line
		
	return result

if __name__ == "__main__":
	test_value = main("TEST0")
	expected_result = 37327623
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
