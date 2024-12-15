#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	wh = dict()
	instr = list()
	reslv = {'<':(0,-1),'^':(-1,0),'>':(0,1),'v':(1,0)}
	pos = tuple()
	col = len(input_lines[0])*2
	row = 0
	for line in input_lines:
		if len(line) != 0:
			if line[0] == '#':
				i = 0
				for ch in line:
					if ch == '@':
						pos = (row,i)
						wh[(row,i)] = '.'
						wh[(row,i+1)] = '.'
					elif ch == 'O':
						wh[(row,i)] = '['
						wh[(row,i+1)] = ']'
					elif ch == '#':
						wh[(row,i)] = '#'
						wh[(row,i+1)] = '#'
					else:
						wh[(row,i)] = '.'
						wh[(row,i+1)] = '.'
					i += 2
				row += 1
			else:
				instr += list(line)
			
	for i in instr:
		new_pos = (pos[0]+reslv[i][0],pos[1]+reslv[i][1])
		if wh[new_pos] == '.':
			pos = new_pos
		elif wh[new_pos] == ']' or wh[new_pos] == '[':
			if i == '^' or i == 'v':
				to_move = set()
				to_move.add(new_pos)
				if (wh[( new_pos[0],new_pos[1]  )] ) == '[':
					to_move.add((new_pos[0],new_pos[1]+1))
				else:
					to_move.add((new_pos[0],new_pos[1]-1))			
				movement = True
				obstacle = False
				check_move = to_move.copy()
				while movement:
					movement = False
					new_check = set()
					for tm in check_move:
						if (wh[(tm[0]+reslv[i][0],tm[1])]) == ']':
							new_check.add( (tm[0]+reslv[i][0],tm[1]) )
							new_check.add( (tm[0]+reslv[i][0],tm[1]-1) )
							movement = True
						elif (wh[(tm[0]+reslv[i][0],tm[1])]) == '[':
							new_check.add( (tm[0]+reslv[i][0],tm[1]) )
							new_check.add( (tm[0]+reslv[i][0],tm[1]+1) )
							movement = True
						elif (wh[(tm[0]+reslv[i][0],tm[1])]) == '#':
							obstacle = True
							movement = False
							break
					to_move = to_move.union(new_check)
					check_move = new_check.copy()
				if not obstacle:
					crates = dict()
					for ek in to_move:
						crates[(ek[0]+reslv[i][0],ek[1])] = wh[ek]
						wh[ek] = '.'
					for crate in crates:
						wh[crate] = crates[crate]	
					pos = new_pos			
			elif i == '<' or i == '>':
				to_move = [new_pos]
				move_pos = (new_pos[0],new_pos[1]+reslv[i][1])
				while wh[(move_pos)] == ']' or wh[(move_pos)] == '[':
					to_move.append(move_pos)
					move_pos = (move_pos[0],move_pos[1]+reslv[i][1])					
				if wh[move_pos] == '.':
					to_move.reverse()
					for crate_move in to_move:
						wh[(crate_move[0], crate_move[1] + reslv[i][1] )] = wh[crate_move]
					wh[new_pos] = '.'
					pos = new_pos

	result = 0
	for r in range(row):
		for c in range(col):
			if wh[(r,c)] == '[':
				result += r * 100 + c 
	
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 9021
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
