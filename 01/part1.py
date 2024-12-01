#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	list_a = list()
	list_b = list()
	for line in input_lines:
		list_a.append(int(line.split()[0]))
		list_b.append(int(line.split()[1]))
	
	list_a.sort()
	list_b.sort()
	difference = 0
	
	for i in range(0,len(list_a)):
		difference += abs(list_a[i] - list_b[i])
		
	return difference

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 11
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
