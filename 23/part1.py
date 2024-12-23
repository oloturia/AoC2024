#!/usr/bin/python3
def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	t_links = dict()
	for line in input_lines:
		t_links.setdefault(line.split('-')[0],set())
		t_links[line.split('-')[0]].add(line.split('-')[1])
		
		t_links.setdefault(line.split('-')[1],set())
		t_links[line.split('-')[1]].add(line.split('-')[0])
	
	sets_of_three = set()
	for hub,spokes in t_links.items():
		if hub[0] == 't':
			for sp in spokes:
				for intrs in t_links[sp].intersection(spokes):
					sets_of_three.add( tuple(sorted([hub,sp,intrs])) )
	
	return len(sets_of_three)

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 7
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
