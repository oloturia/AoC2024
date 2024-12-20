#!/usr/bin/python3
import dijkstra
import sys

def main(input_file,mrow,mcol,size):
	
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	walls = set()
	new_walls = list()
	for line in input_lines:
		if size != 0:
			walls.add((int(line.split(',')[0]), int(line.split(',')[1]) ))
			size -= 1
		else:
			new_walls.append(( int(line.split(',')[0]), int(line.split(',')[1]) ))
	
	for n in new_walls:
		walls.add(n)
		graph = dijkstra.Graph()
		dirs = ((0,1),(-1,0),(0,-1),(1,0))	
		for y in range(mrow+1):
			for x in range(mcol+1):
				for d in dirs:
					ny = y + d[1]
					nx = x + d[0]
					if (ny >= 0 and ny <= mrow) and (nx >= 0 and nx <= mcol) and ((ny,nx) not in walls):
						graph.add_edge((y,x),(ny,nx),1)
		
		best_path = dijkstra.DijkstraSPF(graph, (0,0))
		if str(best_path.get_distance((mrow,mcol))) == "inf":
			return n
	return 
	
if __name__ == "__main__":
	test_value = main("TEST",6,6,12)
	expected_result = (6,1)
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT",70,70,1024))
