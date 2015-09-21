#!/usr/bin/python
import pifacedigitalio as pfd
from time import sleep

INVALID_INDEX_MESSAGE = "Invalid index. LED must be between 0 and 7"


def led_on(num, pifacedigital):
	led_change(num, pifacedigital, True)

def led_off(num, pifacedigital):
	led_change(num, pifacedigital, False)

#true for on, false for off
def led_change(num, pifacedigital, on):
	if not checkRange(num):
		return
	pifacedigital.leds[num].turn_on() if on else pifacedigital.leds[num].turn_off()

def checkRange(num):
	if (num < 0 or num > 7):
		print INVALID_INDEX_METHOD
		return False
	else:
		return True

#returns 1 if switch pressed, 0 if not pressed
def getSwitch(num, pifacedigital):
	if (num < 0 or num > 3):
		print INVALID_INDEX_MESSAGE
		return FALSE
	return pifacedigital.switches[num].value
	
#---------------------Example functions-----------------------------------------

#goes through the leds and turns them on sequentially while turning the previous one off
def cycleLEDs(pifacedigital):
	for i in range (8):
		led_on(i, pifacedigital)
		sleep(1.0)
		led_off(i, pifacedigital)		

#returns when the specified button is pressed
def pollSwitch(switchNum, pifacedigital):
	while not getSwitch(switchNum, pifacedigital):
		pass
	return

#-----------------------------------------------------------------------------------

if __name__ == "__main__":
	print "PiFace experiments"
	pifacedigital = pfd.PiFaceDigital()
	pollSwitch(0, pifacedigital)
	print "button pressed"
	
