#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	safe = 0
	for line in input_lines:
		safe +=1
		pnum = None
		inc = (True if int(line.split()[0]) < int(line.split()[1]) else False)
		for num in [int(n) for n in line.split()]:
			if pnum == None:
				pnum = num
				continue
			diff = (num - pnum if inc else pnum - num)
			if not( 1 <= diff <= 3 ):
				safe -=1
				break
			pnum = num
	return 	safe

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 2
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
