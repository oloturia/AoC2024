#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	visited = set()
	loc = dict()
	position = tuple()
	dirs = ((-1,0),(0,1),(1,0),(0,-1))
	curdir = 0
	for row,line in enumerate(input_lines):
		for col,ch in enumerate(line):
			loc[(row,col)] = ch
			
			if ch == '^':
				loc[(row,col)] = '.'
				position = (row,col)
				visited.add((row,col))
	
	while True:
		newpos = (position[0] + dirs[curdir][0], position[1] + dirs[curdir][1])
		if newpos not in loc:
			break
		if loc[newpos] == '#':
			curdir = (curdir+1)%4
			continue
		position = newpos
		visited.add(position)
	return len(visited)

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 41
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
