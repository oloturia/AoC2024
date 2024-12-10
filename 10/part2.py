#!/usr/bin/python3

trailmap = dict()
currval = 0
dirs = ((1,0),(0,1),(-1,0),(0,-1))

def findroute(start,inc):
	global currval
	global trailmap
	global dirs
	
	for d in dirs:
		try:
			if ( trailmap[(start[0]+d[0],start[1]+d[1])] - inc == 1 ):
				if trailmap[(start[0]+d[0],start[1]+d[1])] == 9:
					currval += 1
				findroute( (start[0]+d[0],start[1]+d[1]), inc+1)
		except KeyError:
			continue
	return

def main(input_file):
	global trailmap
	global currval
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	trailmap = dict()
	startpoints = list()
	for row,line in enumerate(input_lines):
		for col,ch in enumerate(line):
			if ch == '.':
				continue
			trailmap[(row,col)] = int(ch)
			if int(ch) == 0:
				startpoints.append((row,col))
	currval = 0
	for sp in startpoints:
		value = 0
		findroute(sp,0)

	return currval

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 81
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
