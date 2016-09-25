#!/usr/bin/env python

#This script is called by relayToggle.php to toggle/flip the logic pin that closes the relay 
#that complete's the circuit that powers the AC


import Adafruit_BBIO.GPIO as GPIO            # import BBB GPIO python library 

pin = "P8_14"                                #assign which pin is used to activate the relay
GPIO.cleanup()                               #reset GPIO pins before changing 
GPIO.setup(pin, GPIO.OUT)                    #set pin as output

f = open('/usr/local/bin/relayState.txt', 'r+')  #open file containg surrent state of relay
relayState = f.read().strip()                    #read and parse and assign string to variable 
f.seek(0)                                        # change file objects position to 0 inorder to completly rewrite file

if relayState == 'off':                           
    GPIO.output(pin, GPIO.LOW)
    f.write("on ")
    print "AC ON"
	
elif relayState == 'on':
    GPIO.output(pin, GPIO.HIGH)
    f.write("off")
    print "AC OFF"
	
f.close()
