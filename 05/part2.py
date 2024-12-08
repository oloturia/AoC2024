#!/usr/bin/python3


def tester(rules,linesp):
	found = True
	i = 0
	while found and i < len(linesp):
		num = linesp[i]
		for nump in linesp[:i]:
			if num not in rules:
				break
			if nump in rules[num]:
				found = False
				break
		i += 1
	if not found:
		return (nump,num)
	else:
		return False

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	rules = dict()
	result = 0
	for line in input_lines:
		if '|' in line:
			rules.setdefault(line.split('|')[0],list()).append(line.split('|')[1])
		elif ',' in line:
			newline = line.split(',').copy()
			found = tester(rules,newline)
			if not found:
				continue
			while found:
				temp = newline.pop(newline.index(found[0]))
				newline.insert(newline.index(found[1])+1,temp)
				found = tester(rules,newline)
			
			result += int( newline[len(newline)//2] )

	return result

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 123
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
