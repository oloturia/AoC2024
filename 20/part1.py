#!/usr/bin/python3

def main(input_file,limit):
	dirs = ((1,0),(0,1),(-1,0),(0,-1))
	
	cheats = set()
	size_col = 0
	for row in range(2,-1,-1):
		for col in range(-size_col,size_col+1):
			if (row,col) not in dirs:
				cheats.add( (row,col) )
				cheats.add( (-row,col) )
		size_col += 1
	
	maze = dict()
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	start_pos = tuple()
	end_pos = tuple()
	dist_b = 0
	for row,line in enumerate(input_lines):
		for col,ch in enumerate(line):
			if ch == '.':
				maze[(row,col)] = 0
				dist_b += 1
			elif ch == 'S':
				maze[(row,col)] = 0
				start_pos = (row,col)
			elif ch == 'E':
				maze[(row,col)] = 0
				dist_b += 1
				end_pos = (row,col)
	
	cur_pos = start_pos
	maze[cur_pos] = dist_b
	start_to_end = dist_b
	path = [start_pos]
	while cur_pos != end_pos:
		for d in dirs:
			new_room = (cur_pos[0]+d[0],cur_pos[1]+d[1])
			if new_room in maze:
				if maze[new_room] == 0:
					cur_pos = new_room
					dist_b -= 1
					maze[new_room] = dist_b
					path.append(new_room)

		
	count = 0
	for i,room in enumerate(path):
		visited = set()
		for cheat in cheats:
			jump_to = (room[0]+cheat[0],room[1]+cheat[1])
			if jump_to in visited:
				continue
			visited.add(jump_to)
			if jump_to in maze:
				new_dist = i+maze[jump_to]+abs(cheat[0])+abs(cheat[1])
				if ( start_to_end - new_dist ) >= 100:
					count += 1

	return count

if __name__ == "__main__":
	print(main("INPUT",100))
