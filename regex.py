#!/usr/bin/env python3
import sys
import re

#set verbose flag if regex is really long
#putting r in front of a regex, ie re.compile(r'\W+') is raw string
#it doesn't handle \ specially at all
#regexes can get real complicated
#match only finds it at the beginning of the string. search() actually scans

#returns a list of all matches
#one that returns an iterator also exists
def findAllMatches(regex, text):
	pattern = re.compile(regex)
	return pattern.findall(text)

#this is better for 1 time searches, but compiling
#is better if you do it more frequently
def findAllMatches2(regex, text):
	return re.findall(regex, text)

#.group(0) is the whole expression
def matchGroups():
	match = re.match('([a-zA-Z]+)(\\d+)', 'abcd1234')
	print('letters:',match.group(1), 'numbers:', match.group(2))

#python exclusive, can give matched groups names. this is so cool.
def matchNamedGroups():
	match = re.match('(?P<letters>[a-zA-Z]+)(?P<numbers>\\d+)','abcd1234')
	print ('letters:',match.group('letters'), 'numbers:', match.group('numbers'))

#can pass a maxsplit parameter
#strings have their own split too
def split():
	p = re.compile(r'\s')
	result = p.split('A test of split function')
	print(result)

#can pass a maxsub parameter
#subn also returns a new string, also num of replacements
#strings have replace() too
def searchAndReplace(regex, text, replace):
	p = re.compile(regex)
	print(p.sub(replace, text))

#print(findAllMatches('\w+', 'I went to the store'))
#matchGroups()
#matchNamedGroups()
#split()
searchAndReplace('color', 'american says color', 'colour')
