#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	wh = dict()
	instr = list()
	reslv = {'<':(0,-1),'^':(-1,0),'>':(0,1),'v':(1,0)}
	pos = tuple()
	col = len(input_lines[0])
	row = 0
	for line in input_lines:
		if len(line) != 0:
			if line[0] == '#':
				for i,ch in enumerate(line):
					if ch == '@':
						pos = (row,i)
						wh[(row,i)] = '.'
					else:
						wh[(row,i)] = ch
				row += 1
			else:
				instr += list(line)
			

	for i in instr:
		new_pos = (pos[0]+reslv[i][0],pos[1]+reslv[i][1])
		if wh[new_pos] == '.':
			pos = new_pos
		elif wh[new_pos] == 'O':
			move_pos = (new_pos[0]+reslv[i][0],new_pos[1]+reslv[i][1])
			while wh[(move_pos)] == 'O':
				move_pos = (move_pos[0]+reslv[i][0],move_pos[1]+reslv[i][1])
			if wh[move_pos] == '.':
				wh[new_pos] = '.'
				wh[move_pos] = 'O'
				pos = new_pos
	
	result = 0
	for r in range(row):
		for c in range(col):
			if wh[(r,c)] == 'O':
				result += r * 100 + c 
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 10092
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
