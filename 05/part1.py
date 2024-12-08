#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	rules = dict()
	result = 0
	for line in input_lines:
		if '|' in line:
			rules.setdefault(line.split('|')[0],list()).append(line.split('|')[1])
		
		elif ',' in line:
			found = True
			i = 0
			while found and i < len(line.split(',')):
				num = line.split(',')[i]
				for nump in line.split(',')[:i]:
					if num not in rules:
						break
					if nump in rules[num]:
						found = False
						break
				i += 1
			if found:
				result += int( line.split(',')[len(line.split(','))//2] )
		

	return result

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 143
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
