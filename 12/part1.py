#!/usr/bin/python3
regions = dict()
perimeter = 0
area = 0
maxrow = 0
maxcol = 0
visited = set()

def fillRegion(y,x,char):
	global regions
	global perimeter
	global area
	global maxrow
	global maxcol
	global visited
	
	visited.add((y,x))
	area += 1

	dirs = ((0,1),(1,0),(0,-1),(-1,0))
	
	for d in dirs:
		if x+d[0] < 0 or x+d[0] > maxcol or y+d[1] < 0 or y+d[1] > maxrow or regions[(y+d[1],x+d[0])] != char:
			perimeter += 1
		else:
			if (y+d[1],x+d[0]) not in visited:
				fillRegion(y+d[1],x+d[0],char)
	return
	
def main(input_file):
	global regions
	global perimeter
	global area
	global maxrow
	global maxcol
	global visited
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	regions = dict()
	for row,line in enumerate(input_lines):
		for col,ch in enumerate(line):
			regions[(row,col)] = ch

	maxrow = row
	maxcol = col
	result = 0
	for y in range(row+1):
		for x in range(col+1):
			if ord("A") <= ord(regions[(y,x)]) <= ord("Z"):
				visited = set()
				perimeter = 0
				area = 0
				fillRegion(y,x,regions[(y,x)])
				for v in visited:
					regions[(v[0],v[1])] = "."
				result += perimeter * area
	return result

if __name__ == "__main__":
	test_value = main("TEST0")
	expected_result = 140
	assert test_value == expected_result,f"Test 0 failed, expected {expected_result}, result {test_value}"
	test_value = main("TEST1")
	expected_result = 1930
	assert test_value == expected_result,f"Test 1 failed, expected {expected_result}, result {test_value}"
	test_value = main("TEST2")
	expected_result = 772
	assert test_value == expected_result,f"Test 2 failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
