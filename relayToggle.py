#!/usr/bin/env python

#This script is called by relayToggle.php to toggle/flip the logic pin that closes the relay 
#that complete's the circuit that powers the AC


import Home_Automation
import Adafruit_BBIO.GPIO as GPIO

#GPIO.cleanup()

if not Home_Automation.checkACon():
    Home_Automation.turnACon()
    print "AC ON"
    while True:
        pass
        	    
else:
    Home_Automation.turnACoff()
    print "AC OFF"
    while True:
        pass
        
