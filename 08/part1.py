#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	amap = dict()
	for row,line in enumerate(input_lines):
		for col,ch in enumerate(line):
			if ch != '.':
				amap.setdefault(ch,list()).append((row,col))

	anode = set()
	for ant_freq in amap:
		for ant_ref in amap[ant_freq]:
			for ant_dest in amap[ant_freq]:
				if ant_dest == ant_ref:
					continue
				adiff = (ant_dest[0] + (ant_dest[0]-ant_ref[0]), ant_dest[1] +( ant_dest[1]-ant_ref[1]))
				if adiff[0] in range(row+1) and adiff[1] in range(col+1):
					anode.add((adiff))

	return len(anode)

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 14
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
