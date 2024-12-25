#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	state = dict()
	rules = dict()
	rules_line = False
	zvalues = 0
	for line in input_lines:
		if len(line) == 0:
			rules_line = True
			continue
		if rules_line:
			rules[line.split(' -> ')[1]] = tuple(line.split(' -> ')[0].split())
			state[line.split(' -> ')[1]] = None
			if line.split(' -> ')[1][0] == 'z':
				zvalues += 1
		else:
			state[line.split(":")[0]] = int(line.split(":")[1])
	
	znumber = zvalues
	while zvalues > 0:
		for rule in rules.items():
			if state[rule[0]] == None and state[rule[1][0]] != None and state[rule[1][2]] != None:
				if rule[1][1] == 'AND':
					state[rule[0]] = state[rule[1][0]] & state[rule[1][2]]
				elif rule[1][1] == 'OR':
					state[rule[0]] = state[rule[1][0]] | state[rule[1][2]]
				else:
					state[rule[0]] = state[rule[1][0]] ^ state[rule[1][2]]
				if rule[0][0] == 'z':
					zvalues -= 1
	
	result = ""
	for i in range(znumber-1,-1,-1):
		result += str(state["z"+str(i).zfill(2)])
		
	return int(result,2)

if __name__ == "__main__":
	test_value = main("TEST0")
	expected_result = 4
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	test_value = main("TEST1")
	expected_result = 2024
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
