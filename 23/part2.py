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
	
	sets_of_multi = dict()
	for hub,spokes in t_links.items():
		for sp in spokes:
			network = tuple( sorted( {hub,sp}.union(t_links[sp].intersection(spokes) ) ) ) 
			sets_of_multi.setdefault(network,0)
			sets_of_multi[network] += 1
	
	maxnet = str(max(sets_of_multi,key=sets_of_multi.get)).replace(" ","").replace("'","").replace("(","").replace(")","")	
	return maxnet

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = "co,de,ka,ta"
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
