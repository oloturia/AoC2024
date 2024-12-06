#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	visited = set()
	loc = dict()
	start_position = tuple()
	dirs = ((-1,0),(0,1),(1,0),(0,-1))
	curdir = 0
	for row,line in enumerate(input_lines):
		for col,ch in enumerate(line):
			loc[(row,col)] = ch
			
			if ch == '^':
				loc[(row,col)] = '.'
				start_position = (row,col)
				visited.add((row,col))
	
	found = 0
	for x in range(row+1):
		for y in range(col+1):
			if loc[(row,col)] == '#' or (row,col) == start_position:
				continue
			position = start_position
			curdir = 0
			obs_loc = loc.copy()
			obs_loc[(x,y)] = '#'
			visited = set()			
			while True:
				newpos = (position[0] + dirs[curdir][0], position[1] + dirs[curdir][1])
				if newpos not in obs_loc:
					break
				if obs_loc[newpos] == '#':
					curdir = (curdir+1)%4
					continue
				position = newpos
				if (position+(curdir,)) in visited:
					found += 1
					break
				visited.add( position+(curdir,) )
	return found

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 6
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
