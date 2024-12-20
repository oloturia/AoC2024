#!/usr/bin/python3
reg_list = set()

def scanline(stripe):
	global reg_list
	if stripe in reg_list:
		return True
	for mlen in range(0,len(stripe)):
		if stripe[-mlen:] in reg_list:
			if scanline(stripe[:-mlen]):
				return True
	return False
	
def main(input_file):
	global reg_list
	reg_list = set()
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
		
	reg_list = {x.strip() for x in input_lines[0].split(",")}
	count = 0
	for i in range(2,len(input_lines)):
		if scanline(input_lines[i]):
			count += 1
			
	return count
	
if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 6
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"	
	print(main("INPUT"))
