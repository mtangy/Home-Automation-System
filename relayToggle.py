#!/usr/bin/env python

#import time
import Adafruit_BBIO.GPIO as GPIO
#import socket # Import socket module


pin = "P8_14"
GPIO.cleanup()
GPIO.setup(pin, GPIO.OUT)

f = open('/usr/local/bin/relayState.txt', 'r+')
relayState = f.read().strip()
f.seek(0)

if relayState == 'off':
    GPIO.output(pin, GPIO.LOW)
    f.write("on ")
    print "AC ON"
	
elif relayState == 'on':
    GPIO.output(pin, GPIO.HIGH)
    f.write("off")
    print "AC OFF"
	
f.close()
