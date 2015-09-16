#!/usr/bin/env python3
import sys

""" note: the 0 argument is ./file.py or file.py"""
def withIndex():
	for idx in range(len(sys.argv)):
		print("index:", str(idx), ', value:', sys.argv[idx])

def forEach():
	for element in sys.argv:
		print(element)

withIndex()
#forEach()


