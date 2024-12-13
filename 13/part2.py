#!/usr/bin/python3
import numpy as np

def main(input_file):

	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	inc = 10000000000000
	result = 0
	for line in input_lines:
		if len(line) > 0:
			if line[7] == "A":
				xa=int(line.split("+")[1].split(",")[0])
				ya=int(line.split("+")[2])
			elif line[7] == "B":
				xb=int(line.split("+")[1].split(",")[0])
				yb=int(line.split("+")[2])
			elif line[0] == "P":
				rx=int(line.split("=")[1].split(",")[0]) + inc
				ry=int(line.split("=")[2]) + inc
				a = np.array([[xa,xb],[ya,yb]])
				b = np.array([rx,ry])
				solution = np.linalg.solve(a,b)
				if ( abs(round(solution[0]) - solution[0]) < 0.001 and abs(round(solution[1]) - solution[1]) < 0.001 ):
					result += solution[0]*3 + solution[1]
				
	return round(result)

if __name__ == "__main__":
	print(main("INPUT"))

