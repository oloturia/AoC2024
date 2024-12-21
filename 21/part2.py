#!/usr/bin/python3
from functools import lru_cache

@lru_cache
def new_move(string,level):
	if level == 25:
		return len(string)
	
	curpos = 'A'
	moves = ""
	for ch in string:
		moves += keypad_2(curpos,ch)
		curpos = ch
	total = 0
	for move in moves.split('A')[:-1]:
		total += new_move(move+'A',level+1)

	return total

def keypad_1(source,dest):
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
			return '>>vvA'
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
		curpos =  'A'
		moves =  ""
		for ch in line:
			moves += keypad_1(curpos,ch)
			curpos = ch
		for move in moves.split('A')[:-1]:
			result += new_move(move+'A',0) * int(line[:3])
	return result

if __name__ == "__main__":
	print(main("INPUT"))
