#!/usr/bin/env python
#-*- coding:utf-8 -*-
#-----------------------------------------------------------------------
# 
# dfixor.py
#
# Description: 
#  
#   Special tool for file XORing and further analysis. 
#
# TODO: fill info
#
# Usage:
#
#   dfixor [options] <filename>
#
# Author: delimitry
#
#-----------------------------------------------------------------------

import sys
import getopt

def print_usage():
	print ''
	print 'dfixor - tool for file XORing and further analysis'
	print ''
	print 'Usage:'
	print '  dfixor [options] <filename>'
	print ''
	print 'Application Options:'
	print '  -h, --help            Print this help message and exit'
	print '  -o, --output          Set output file'	
	print '  -V, --version         Displays the current version'
	print '  -v                    Verbose mode'

def print_version():
	print ''
	print 'DFiXOR v0.1'
	print ''
	
def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "ho:vV", ["help", "version", "output="])
	except getopt.GetoptError, err:
		print str(err)
		print_usage()
		sys.exit()

	output = None
	verbose = False
	for o, a in opts:
		if o == "-v":
			verbose = True
		elif o in ("-h", "--help"):
			print_usage()
			sys.exit()
		elif o in ("-o", "--output"):
			output = a
		elif o in ("-V", "--version"):
			print_version()
			sys.exit()
		else:
			print_usage()
			sys.exit()
			assert False, "unhandled option"

if __name__ == '__main__':
	main()