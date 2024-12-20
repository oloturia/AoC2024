#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	regA = 0
	regB = 0
	regC = 0
	ops = list()

	for line in input_lines:
		if len(line) != 0:
			if line[9] == "A":
				regA = int(line.split(':')[1])
			elif line[9] == "B":
				regB = int(line.split(':')[1])
			elif line[9] == "C":
				regB = int(line.split(':')[1])				
			else:
				for ch in line.split(':')[1].split(','):
					ops.append(int(ch))

	out = list()
	pc = 0
	
	while pc < len(ops):
		op = ops[pc]
		lit = combo = ops[pc+1]
		
		if combo == 4:
			combo = regA
		elif combo == 5:
			combo = regB
		elif combo == 6:
			combo = regC
		
		if op == 0:
			regA = regA//(2**combo)
		elif op == 1:
			regB = regB ^ lit
		elif op == 2:
			regB = combo % 8
		elif op == 3:
			if regA != 0:
				pc = lit
				continue
		elif op == 4:
			regB = regB ^ regC
		elif op == 5:
			out.append(combo % 8 )
		elif op == 6:
			regB = regA//(2**combo)
		elif op == 7:
			regC = regA//(2**combo)
		
		pc += 2
		
	return 	out

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = [4,6,3,5,6,3,5,2,1,0]
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
