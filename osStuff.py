#!/usr/bin/env python3
import sys
import os

def printAllEnvironmentVariables():
	for key in os.environ:
		print (key, os.environ[key])

