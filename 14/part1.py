#!/usr/bin/python3

def main(input_file,wid,hei):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]
	
	q1 = q2 = q3 = q4 = 0
	for line in input_lines:
		p1 = int( line.split('=')[1].split(',')[0] )
		p2 = int( line.split('=')[1].split(',')[1].split()[0] )
		v1 = int( line.split('=')[2].split(',')[0])
		v2 = int( line.split('=')[2].split(',')[1])
		
		xA = ( p1 + v1 * 100 ) % wid
		yA = ( p2 + v2 * 100 ) % hei
		
		if xA in range( (wid // 2) ) and yA in range( (hei // 2) ):
			q1 += 1
		elif xA in range( (wid // 2) ) and yA in range( (hei // 2) +2, hei+1):
			q2 += 1
		elif xA in range( (wid // 2) +1, wid+1) and yA in range( (hei // 2) ):
			q3 += 1
		elif xA in range( (wid // 2) +1, wid+1) and yA in range( (hei // 2) +1, hei + 1):
			q4 += 1
		
	return 	q1*q2*q3*q4

if __name__ == "__main__":
	test_value = main("TEST",11,7)
	expected_result = 12
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT",101,103))
