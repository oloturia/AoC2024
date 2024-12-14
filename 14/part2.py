#!/usr/bin/python3
def main(input_file,wid,hei):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	robots = list()
	for line in input_lines:
		robots.append( ( int( line.split('=')[1].split(',')[0] ), int( line.split('=')[1].split(',')[1].split()[0] ), int( line.split('=')[2].split(',')[0]), int( line.split('=')[2].split(',')[1]) ) ) 
	for secs in range(wid*hei):
		maps = dict()
		for rob in robots:
			p1,p2,v1,v2 = rob  
			xA = ( p1 + v1 * secs ) % wid
			yA = ( p2 + v2 * secs ) % hei
			maps[(xA,yA)] = True

		for i in range(hei-2):
			if (i,wid//2) in maps and (i+1,(wid//2)-1) in maps and (i+1,wid//2) in maps and (i+1,(wid//2)+1) in maps and (i+2,(wid//2)-3) in maps and (i+2,(wid//2)-2) in maps and (i+2,(wid//2)-1) in maps and(i+2,wid//2) in maps and (i+2,(wid//2)+1) in maps and (i+2,(wid//2)+2) in maps and (i+2,(wid//2)+3) in maps:
				return secs
		
	return secs

if __name__ == "__main__":
	print(main("INPUT",101,103))
