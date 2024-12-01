#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	list_a = list()
	list_b = list()
	for line in input_lines:
		list_a.append(int(line.split()[0]))
		list_b.append(int(line.split()[1]))
	
	similarity = 0
	
	for i in range(0,len(list_a)):
		similarity += list_b.count(list_a[i])*list_a[i]
		
	return similarity

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 31
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
