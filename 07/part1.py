#!/usr/bin/python3

def valid(start_num,factors):
	if len(factors) == 1:
		if factors[0] - start_num == 0:
			return True
		else:
			return False
	
	addnum = 0
	mulnum = 0
	
	last_fact = factors.pop()
	addnum = start_num - last_fact
	if start_num // last_fact == start_num / last_fact:
		mulnum = start_num // last_fact
		
	result_mul = False
	result_add = False
	if addnum > 0:
		result_add = valid(addnum,factors.copy())
	if mulnum != 0:
		result_mul = valid(mulnum,factors.copy())
	
	return result_add or result_mul
		
		

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	result = 0
	for line in input_lines:
		start_num = int(line.split(':')[0])
		hist = str(start_num)+"="
		if valid(start_num,[int(x) for x in line.split(":")[1].strip().split(" ")]):
			result += start_num
			
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 3749
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
