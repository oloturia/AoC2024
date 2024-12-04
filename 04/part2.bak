#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	found = 0 
	directions = ( (0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1) )

	for row,line in enumerate(input_lines):
		for col,ch in enumerate(line):
			if ch == 'X':
				for d in directions:
					if row+d[0] >= 0 and col+d[1] >= 0 and row+d[0] < len(line) and col+d[1] < len(input_lines) and row+d[0]*2 >= 0 and col+d[1]*2 >= 0 and row+d[0]*2 < len(line) and col+d[1]*2 < len(input_lines) and row+d[0]*3 >= 0 and col+d[1]*3 >= 0 and row+d[0]*3 < len(line) and col+d[1]*3 < len(input_lines) and( input_lines[row+d[0]][col+d[1]] == 'M' and input_lines[row+d[0]*2][col+d[1]*2] == 'A' and input_lines[row+d[0]*3][col+d[1]*3] == 'S'):
						found +=1
	return found

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 18
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
