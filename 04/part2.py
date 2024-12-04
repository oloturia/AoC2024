#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	found = 0 
	directions = ( (1,1),(1,-1),(-1,-1),(-1,1) )

	for row,line in enumerate(input_lines):
		for col,ch in enumerate(line):
			if row == 0 or col == 0 or row == len(input_lines)-1 or col == len(line)-1:
				continue
			if ch == 'A':
				letters = ""
				for d in directions:
					letters += input_lines[row+d[0]][col+d[1]]
				if letters.count('M') == 2 and letters.count('S') == 2 and (letters.count('MM') == 1 or letters.count('SS') ==1):
					found +=1
	return found

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 9
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
