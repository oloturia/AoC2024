#!/usr/bin/python3
from dijkstra import Graph, DijkstraSPF

def main(input_file):

	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	maze = dict()
	start_pos = tuple()
	end_pos = tuple()
	graph = Graph()
	dirs = ( (0,1),(1,0),(0,-1),(-1,0) )

	for row,line in enumerate(input_lines):
		for col,ch in enumerate(line):
			if ch == 'S':
				start_pos = (row,col,0)
				maze[(row,col)] = '.'
			elif ch == 'E':
				end_pos = (row,col)
				maze[(row,col)] = 'E'
			else:
				maze[(row,col)] = ch

	for r in range(row):
		for c in range(col):
			if maze[(r,c)] == '.' or maze[(r,c)] == 'E':
				for d1 in range(4):
					for d2 in range(4):
						if abs(d1-d2) == 1 or (d1==0 and d2 ==3) or (d1==3 and d2==0):
							if maze[(r+dirs[d2][0],c+dirs[d2][1])] in ('.','E') :
								graph.add_edge( (r,c,d1), (r,c,d2),1000 )
					if maze[(r+dirs[d1][0],c+dirs[d1][1])] == '.':
						graph.add_edge((r,c,d1),(r+dirs[d1][0],c+dirs[d1][1],d1),1)
					elif maze[(r+dirs[d1][0],c+dirs[d1][1])] == 'E':
						graph.add_edge((r,c,d1),end_pos,1)			
				
	dijkstra = DijkstraSPF(graph,start_pos)

	return dijkstra.get_distance(end_pos)

if __name__ == "__main__":
	test_value = main("TEST0")
	expected_result = 7036
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	test_value = main("TEST1")
	expected_result = 11048
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))

