#!/usr/bin/python3
regions = dict()
area = 0
maxrow = 0
maxcol = 0
visited = set()
sides = dict()

def fillRegion(y,x,char):
	global regions
	global area
	global maxrow
	global maxcol
	global visited
	global sides
	
	visited.add((y,x))
	area += 1
	dirs = ((0,1),(1,0),(0,-1),(-1,0))

	for i,d in enumerate(dirs):
		if x+d[0] < 0 or x+d[0] > maxcol or y+d[1] < 0 or y+d[1] > maxrow or regions[(y+d[1],x+d[0])] != char:
			sides.setdefault((x,y),[0,0,0,0])[i] = 1
		else:	
			if (y+d[1],x+d[0]) not in visited:
				fillRegion(y+d[1],x+d[0],char)
	return
	
def findSides(min_y,max_y,min_x,max_x):
	global sides
	perimeters = 0
	
	for y in range(min_y,max_y):
		foundUp = False
		foundDn = False
		for x in range(min_x,max_x):
			if (y,x) in sides:
				if sides[(y,x)][1] == 1 and foundUp == False:
					perimeters += 1
					foundUp = True
				if foundUp and sides[(y,x)][1] == 0:
					foundUp = False
				if sides[(y,x)][3] == 1 and foundDn == False:
					perimeters += 1
					foundDn = True
				if foundDn and sides[(y,x)][3] == 0:
					foundDn = False
			else:
				foundDn = False
				foundUp = False
				
	for x in range(min_x,max_x):
		foundUp = False
		foundDn = False
		for y in range(min_y,max_y):
			if (y,x) in sides:
				if sides[(y,x)][0] == 1 and foundUp == False:
					perimeters += 1
					foundUp = True
				if foundUp and sides[(y,x)][0] == 0:
					foundUp = False
				if sides[(y,x)][2] == 1 and foundDn == False:
					perimeters += 1
					foundDn = True
				if foundDn and sides[(y,x)][2] == 0:
					foundDn = False
			else:
				foundDn = False
				foundUp = False
	return perimeters
	
def main(input_file):
	global regions
	global area
	global maxrow
	global maxcol
	global visited
	global sides
	
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
				sides = dict()
				area = 0
				fillRegion(y,x,regions[(y,x)])
				minregion_y = maxrow
				minregion_x = maxcol
				maxregion_y = 0
				maxregion_x = 0
				for v in visited:
					regions[(v[0],v[1])] = "."
					if v[1] < minregion_y:
						minregion_y = v[1]
					if v[1] > maxregion_y:
						maxregion_y = v[1]
					if v[0] < minregion_x:
						minregion_x = v[0]
					if v[0] > maxregion_x:
						maxregion_x = v[0]	
				perimeters = findSides(minregion_y,maxregion_y+1,minregion_x,maxregion_x+1)	
				result += perimeters * area
	return result

if __name__ == "__main__":
	test_value = main("TEST0")
	expected_result = 80
	assert test_value == expected_result,f"Test 0 failed, expected {expected_result}, result {test_value}"
	test_value = main("TEST1")
	expected_result = 1206
	assert test_value == expected_result,f"Test 1 failed, expected {expected_result}, result {test_value}"
	test_value = main("TEST2")
	expected_result = 436
	assert test_value == expected_result,f"Test 2 failed, expected {expected_result}, result {test_value}"
	test_value = main("TEST3")
	expected_result = 236
	assert test_value == expected_result,f"Test 3 failed, expected {expected_result}, result {test_value}"
	test_value = main("TEST4")
	expected_result = 368
	assert test_value == expected_result,f"Test 4 failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
