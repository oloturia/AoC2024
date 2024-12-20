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
			if line[9] == "B":
				regB = int(line.split(':')[1])
			elif line[9] == "C":
				regB = int(line.split(':')[1])				
			elif line[9] != "A":
				for ch in line.split(':')[1].split(','):
					ops.append(int(ch))

	
	result = 1
	nfound = 1
	inc = 0
	out = list()
	stroct = ""
	
	while out != ops:
		regA = result
		pc = regB = regC = 0
		out = list()
				
		while pc < len(ops):	
			op = ops[pc]
			lit = combo = ops[pc+1]	
			if combo == 4:
				combo = regA
			elif combo == 5:
				combo = regB
			elif combo == 6:
				combo = regC
			elif combo == 7:
				continue
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
				out.append(combo%8)				
			elif op == 6:
				regB = regA//(2**combo)
			elif op == 7:
				regC = regA//(2**combo)
			pc += 2

		if out == ops:
			return result
		
		if out[-nfound:] == ops[-nfound:]:
			stroct = oct(result)
			nfound += 1
			inc = 0

		if inc == 8:
			result += 1
		else:		
			result = int(stroct+str(inc),8)
			inc += 1
		
if __name__ == "__main__":
	print(main("INPUT"))
