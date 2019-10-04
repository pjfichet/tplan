#! /usr/bin/env python

import sys
import locale
from .parser import Parser

def main():
	locale.setlocale(locale.LC_ALL, '')
	parser = Parser()
	if len(sys.argv) == 1:
		parser.parse(sys.stdin)
	else:
		with open(sys.argv[1], 'r') as f:
			parser.parse(f)
