#!/usr/bin/python3

def main(input_file):
	with open(input_file) as f:
		defrag = f.readlines()[0].strip()

	files = dict()
	spaces = list()
	index_space = 0
	for i,ch in enumerate(defrag):
		if i // 2 == i / 2:
			files.setdefault(i//2,(index_space,int(ch)))
			index_space += int(ch)
		else:
			spaces.append((index_space,int(ch)))
			index_space += int(ch)

	checksum = 0
	for f in range(len(files)-1,-1,-1):
		found = False
		for i,s in enumerate(spaces):
			if s[1] >= files[f][1]:
				found = True
				index = s[0]
				for fsize in range(files[f][1]):
					checksum += index * f
					index += 1
				spaces[i] = (spaces[i][0]+files[f][1], spaces[i][1]-files[f][1])
				break
			if s[0] >= files[f][0]:
				break
		if not found:
			index = files[f][0]
			for fsize in range(files[f][1]):
				checksum += index * f
				index += 1
	return checksum

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 2858
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
