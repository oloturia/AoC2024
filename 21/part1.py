#!/usr/bin/python3

def keypad_1(source,dest):#,keypad_type):
	if source == '7':
		if dest == '7':
			return 'A'
		if dest == '8':
			return '>A'
		if dest == '9':
			return '>>A'
		if dest == '4':
			return 'vA'
		if dest == '5':
			return 'v>A'
		if dest == '6':
			return 'v>>A'
		if dest == '1':
			return 'vvA'
		if dest == '2':
			return 'vv>A'
		if dest == '3':
			return 'vv>>A'
		if dest == '0':
			return '>vvvA'
		if dest == 'A':
			return '>>vvvA'
	if source == '8':
		if dest == '7':
			return '<A'
		if dest == '8':
			return 'A'
		if dest == '9':
			return '>A'
		if dest == '4':
			return '<vA'
		if dest == '5':
			return 'vA'
		if dest == '6':
			return 'v>A'
		if dest == '1':
			return '<vvA'
		if dest == '2':
			return 'vvA'
		if dest == '3':
			return 'vv>A'
		if dest == '0':
			return 'vvvA'
		if dest == 'A':
			return 'vvv>A'
	if source == '9':
		if dest == '7':
			return '<<A'
		if dest == '8':
			return '<A'
		if dest == '9':
			return 'A'
		if dest == '4':
			return '<<vA'
		if dest == '5':
			return '<vA'
		if dest == '6':
			return 'vA'
		if dest == '1':
			return '<<vvA'
		if dest == '2':
			return '<vvA'
		if dest == '3':
			return 'vvA'
		if dest == '0':
			return '<vvvA'
		if dest == 'A':
			return 'vvvA'
	if source == '4':
		if dest == '7':
			return '^A'
		if dest == '8':
			return '>^A'
		if dest == '9':
			return '>>^A'
		if dest == '4':
			return 'A'
		if dest == '5':
			return '>A'
		if dest == '6':
			return '>>A'
		if dest == '1':
			return 'vA'
		if dest == '2':
			return 'v>A'
		if dest == '3':
			return 'v>>A'
		if dest == '0':
			return '>vvA'
		if dest == 'A':
			return '>>vvA'
	if source == '5':
		if dest == '7':
			return '<^A'
		if dest == '8':
			return '^A'
		if dest == '9':
			return '>^A'
		if dest == '4':
			return '<A'
		if dest == '5':
			return 'A'
		if dest == '6':
			return '>A'
		if dest == '1':
			return '<vA'
		if dest == '2':
			return 'vA'
		if dest == '3':
			return 'v>A'
		if dest == '0':
			return 'vvA'
		if dest == 'A':
			return 'vv>A'
	if source == '6':
		if dest == '7':
			return '<<^A'
		if dest == '8':
			return '<^A'
		if dest == '9':
			return '^A'
		if dest == '4':
			return '<<A'
		if dest == '5':
			return '<A'
		if dest == '6':
			return 'A'
		if dest == '1':
			return '<<vA'
		if dest == '2':
			return '<vA'
		if dest == '3':
			return 'vA'
		if dest == '0':
			return '<vvA'
		if dest == 'A':
			return 'vvA'
	if source == '1':
		if dest == '7':
			return '^^A'
		if dest == '8':
			return '>^^A'
		if dest == '9':
			return '>>^^A'
		if dest == '4':
			return '^A'
		if dest == '5':
			return '>^A'
		if dest == '6':
			return '>>^A'
		if dest == '1':
			return 'A'
		if dest == '2':
			return '>A'
		if dest == '3':
			return '>>A'
		if dest == '0':
			return '>vA'
		if dest == 'A':
			return '>>vA'
	if source == '2':
		if dest == '7':
			return '<^^A'
		if dest == '8':
			return '^^A'
		if dest == '9':
			return '>^^A'
		if dest == '4':
			return '<^A'
		if dest == '5':
			return '^A'
		if dest == '6':
			return '>^A'
		if dest == '1':
			return '<A'
		if dest == '2':
			return 'A'
		if dest == '3':
			return '>A'
		if dest == '0':
			return 'vA'
		if dest == 'A':
			return 'v>A'
	if source == '3':
		if dest == '7':
			return '<<^^A'
		if dest == '8':
			return '<^^A'
		if dest == '9':
			return '^^A'
		if dest == '4':
			return '<<^A'
		if dest == '5':
			return '<^A'
		if dest == '6':
			return '^A'
		if dest == '1':
			return '<<A'
		if dest == '2':
			return '<A'
		if dest == '3':
			return 'A'
		if dest == '0':
			return '<vA'
		if dest == 'A':
			return 'vA'
	if source == '0':
		if dest == '7':
			return '^^^<A'
		if dest == '8':
			return '^^^A'
		if dest == '9':
			return '>^^^A'
		if dest == '4':
			return '^^<A'
		if dest == '5':
			return '^^A'
		if dest == '6':
			return '>^^A'
		if dest == '1':
			return '^<A'
		if dest == '2':
			return '^A'
		if dest == '3':
			return '^>A'
		if dest == '0':
			return 'A'
		if dest == 'A':
			return '>A'
	if source == 'A':
		if dest == '7':
			return '^^^<<A'
		if dest == '8':
			return '<^^^A'
		if dest == '9':
			return '^^^A'
		if dest == '4':
			return '^^<<A'
		if dest == '5':
			return '<^^A'
		if dest == '6':
			return '^^A'
		if dest == '1':
			return '^<<A'
		if dest == '2':
			return '<^A'
		if dest == '3':
			return '^A'
		if dest == '0':
			return '<A'
		if dest == 'A':
			return 'A'
			
	return 


def keypad_2(source,dest):
	keypad = dict()
	
	if source == 'A':
		if  dest == '^':
			return '<A'
		if dest == '>':
			return 'vA'
		if dest == 'v':
			return '<vA'
		if dest == '<':
			return 'v<<A'
		if dest == 'A':
			return 'A'
	
	if source == '<':
		if  dest == '^':
			return '>^A'
		if dest == '>':
			return '>>A'
		if dest == 'v':
			return '>A'
		if dest == '<':
			return 'A'
		if dest == 'A':
			return '>>^A'
			
	if source == '^':
		if  dest == '^':
			return 'A'
		if dest == '>':
			return 'v>A'
		if dest == 'v':
			return 'vA'
		if dest == '<':
			return 'v<A'
		if dest == 'A':
			return '>A'
			
	if source == 'v':
		if  dest == '^':
			return '^A'
		if dest == '>':
			return '>A'
		if dest == 'v':
			return 'A'
		if dest == '<':
			return '<A'
		if dest == 'A':
			return '^>A'
			
	if source == '>':
		if  dest == '^':
			return '<^A'
		if dest == '>':
			return 'A'
		if dest == 'v':
			return '<A'
		if dest == '<':
			return '<<A'
		if dest == 'A':
			return '^A'	
	return 

def main(input_file):
	with open(input_file) as f:
		input_lines = [line.rstrip() for line in f.readlines()]

	result = 0
	for line in input_lines:
		curpos0 = curpos1 = curpos2 = 'A'
		r0 = r1 = r2 = ""
		for ch in line:
			r0 += keypad_1(curpos0,ch)
			curpos0 = ch
		for ch in r0:
			r1 += keypad_2(curpos1,ch)
			curpos1 = ch
		for ch in r1:
			r2 += keypad_2(curpos2,ch)
			curpos2 = ch
		result += len(r2)*int(line[:3])
		
	return result

if __name__ == "__main__":
	test_value = main("TEST")
	expected_result = 126384
	assert test_value == expected_result,f"Test failed, expected {expected_result}, result {test_value}"
	print(main("INPUT"))
