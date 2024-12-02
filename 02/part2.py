#!/usr/bin/python3

def eval_line(ev_line):
	pnum = None
	inc = (True if ev_line[0] < ev_line[1] else False)
	for num in ev_line:
		if pnum == None:
			pnum = num
			continue
		diff = (num - pnum if inc else pnum - num)
		if not( 1 <= diff <= 3 ):
			return False
		pnum = num
	return True

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	safe = 0
	for line in input_lines:
		ev_line = [int(n) for n in line.split()]
		if eval_line(ev_line):
			safe +=1
		else:
			for i in range(len(ev_line)):
				newline = ev_line.copy()
				newline.pop(i)
				if eval_line(newline):
					safe +=1
					break
	return safe

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 4
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
