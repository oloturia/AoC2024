#!/usr/bin/python3

rules = dict()
znumber = 0

def swap(a,b):
	global rules
	temp = rules[a]
	rules[a] = rules[b]
	rules[b] = temp
	return rules

def operate(state_orig):
	global znumber
	global rules
	
	zvalues = znumber
	state = state_orig.copy()	
	breakloop = 0
	
	while zvalues > 0:
		breakloop += 1
		for rule in rules.items():
			if state[rule[0]] == None and state[rule[1][0]] != None and state[rule[1][2]] != None:
				if rule[1][1] == 'AND':
					state[rule[0]] = state[rule[1][0]] & state[rule[1][2]]
				elif rule[1][1] == 'OR':
					state[rule[0]] = state[rule[1][0]] | state[rule[1][2]]
				else:
					state[rule[0]] = state[rule[1][0]] ^ state[rule[1][2]]
				if rule[0][0] == 'z':
					zvalues -= 1
		if breakloop >= len(state)*10:
			return "X"*46
	
	result = ""
	for i in range(znumber-1,-1,-1):
		result += str(state["z"+str(i).zfill(2)])
	return result

def check_sum(state,ind):
	global znumber
	index_res = ""
	for x in (1,0):
		for y in (1,0):
			state["x"+str(ind).zfill(2)] = x
			state["y"+str(ind).zfill(2)] = y
			index_res += operate(state)[-(ind+1)]
	return index_res

def main(input_file):
	global rules
	global znumber
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	state = dict()
	rules = dict()
	rules_line = False
	znumber = 0
	xstr = ""
	ystr = ""
	for line in input_lines:
		if len(line) == 0:
			rules_line = True
			continue
		if rules_line:
			rules[line.split(' -> ')[1]] = tuple(line.split(' -> ')[0].split())
			state[line.split(' -> ')[1]] = None
			if line.split(' -> ')[1][0] == 'z':
				znumber += 1
		else:
			state[line.split(":")[0]] = 0

	keys = rules.keys()
	swapped = list()
	
	for i in range(znumber-1):
		idr = check_sum(state,i)
		found = False
		to_ch = ["z"+str(i).zfill(2),]
		while idr != "0110":
			for ch in to_ch:
				for ru in keys:
					if ru[0] == 'z':
						continue
					rules = swap(ch,ru)
					idr = check_sum(state,i)
					if idr == "0110":
						if not (ch[0] == 'z' and (rules[ch][0][0] in ('x','y'))):
							if (ch[0] == 'z' and rules[ch][1] == "XOR") or (ch[0] != 'z'):
								swapped.append(ch)
								swapped.append(ru)
								found = True
								break 
					rules = swap(ch,ru)
				if found:
					break
			if found:
				break
		
			else:
				nlist = list()
				for ch in to_ch:
					nlist.append(rules[ch][0])
					nlist.append(rules[ch][2])
				to_ch = nlist

	return str(sorted(swapped)).replace("[","").replace("]","").replace("'","").replace(" ","")

if __name__ == "__main__":
	print(main("INPUT"))
