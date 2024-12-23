#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [int(line.rstrip()) for line in f.readlines()]

	prune = lambda a : a % 16777216

	result = 0

	sequences = list()
	
	for el in input_lines:
		sequences.append(list())
		sequences[-1] = [el%10]
	
	
	for i in range(0,2000):
		for el,line in enumerate(input_lines):
			number = line
	
			numberA = line
			numberA *= 64
			number = number ^ numberA
			number = prune(number)
			
			numberB = number
			numberB = numberB//32
			number = number ^ numberB
			number = prune(number)
			
			numberC = number
			numberC *= 2048
			number = number ^ numberC
			number = prune(number)

			input_lines[el] = number
			sequences[el].append( number%10 )

	buyer = list()

	for sequence in sequences:
		buyer.append(sequence.copy())
	
	for i0 in range(len(sequences)):
		for i1 in range(1999,-1,-1):	
			if i1 == 0:
				continue
			sequences[i0][i1] -= sequences[i0][i1-1]
		sequences[i0].pop(0)
		buyer[i0].pop(0)
	

	bananas = dict()
	for s,sequence in enumerate(sequences):
		visited = set()
		for i in range(3,2000):
			seq = (sequence[i-3],sequence[i-2],sequence[i-1],sequence[i])
			if seq not in visited:
				visited.add(seq)
				bananas.setdefault(seq,0)
				bananas[seq] += buyer[s][i]

	return bananas[max(bananas, key=bananas.get)]

if __name__ == "__main__":
	test_value = main("TEST1")
	expected_result = 23
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
