#!/usr/bin/python3

def valid(start_num,factors):
	if len(factors) == 1:
		if factors[0] - start_num == 0:
			return True
		else:
			return False

	if str(start_num) == ''.join([str(x) for x in factors]):
		return True

	conc_str = str(factors[-1])			
	addnum = 0
	mulnum = 0
	concnum = 0
	last_fact = factors.pop()
	addnum = start_num - last_fact
	if start_num // last_fact == start_num / last_fact:
		mulnum = start_num // last_fact
	if(conc_str == str(start_num)[-len(conc_str):]) and str(start_num) != conc_str:
		concnum = int( str(start_num)[:-len( str(conc_str) )])
		
	result_mul = False
	result_add = False
	result_conc = False
	if addnum > 0:
		result_add = valid(addnum,factors.copy())
	if mulnum != 0:
		result_mul = valid(mulnum,factors.copy())
	if concnum != 0:
		result_conc = valid(concnum,factors.copy())
	
	return result_add or result_mul or result_conc

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
	expected_result = 11387
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
