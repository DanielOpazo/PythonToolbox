#!/usr/bin/env python3
import sys

"""r: only read
	w: only write (will overwrite file of same name)	
	a: for appending
	r+: read and write

open() will create a new file if it doesn't already exist
"""	
"""writes-------------------------------------------+"""

#doesn't put a "\n"
def writeToFile(fileName, content):
	with open(fileName, 'w') as textFile:
		textFile.write(content)
#writeLines doesn't put a '\n'. wtf		
def writeLinesToFile(fileName, lines):
	with open(fileName, 'w') as textFile:
		textFile.writelines(lines)
def appendTextToFile(content):
	with open(fileName, 'a') as textFile:
		textFile.write(content)
def appendLinesToFile(lines):
	with open(fileName, 'a') as textFile:
		textFile.writelines(lines)

"""-------------------------------------------------------+"""

"""reads -------------------------------------------------+"""
#returns string containing all characters from the file
#read has a int parameter for how many characters to return
def readEntireFile(fileName):
	with open(fileName, 'r') as textFile:
		return textFile.read()

#the "\n" char stays attached to each line
#readline() will return a single line
def readLinesFromFile(fileName):
	with open(fileName, 'r') as textFile:
		lines = textFile.readlines()
	return lines

#another way to read the lines from a file
def readLinesFromFile2(fileName):
	with open(fileName, 'r') as textFile:
		lines = []
		for line in textFile:
			lines.append(line)
	return lines
"""-----------------------------------------------+"""

if sys.argv[1] is None:
	fileName = input("enter the file name: ")
else:
	fileName = sys.argv[1]
print ("".join(readLinesFromFile(fileName)))
#print ("".join(readLinesFromFile2(fileName)))
#appendTextToFile("text appended")
#appendLinesToFile(["line appended\n", "another line appended\n"])
#writeToFile(fileName, "file write")
#writeLinesToFile(fileName, ["write line\n", "write another line\n"])

