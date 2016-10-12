#Home_Automation_Module.py
#
#Description:
#This file contains shared functions used throughout my home automation system

import fcntl
from time import sleep
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO


ACfile = "/home/mtangy/homeAuto/relayState.txt"

tempPin = "P9_40"
ACpin = "P8_8"
GPIO.setup(ACpin, GPIO.OUT)
ADC.setup()

def fileOverWrite(contents, file):              #Over write file with contents passed to 
    while True:                                                #Continuously attempt to write to file until it is not in use
        try:                                                   #Exception handling for IOError if file is already in use  
            with open(file,'w') as f:                          #Attempt to open file and create file handle
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)  #Lock file to prevent race condition from parallel process trying to access same file 
                f.seek(0)                                      #set file position to start overwrite
                f.write(contents)                              #write contents to file
                fcntl.flock(f, fcntl.LOCK_UN)                  #unlock file
                f.close()                                      #close file 
            break                                              #break loop since file writing is complete 
        except IOError:                                        #error message if file is use and IOError is raised 
            print file," is already in use."		           	

			
def fileCheck(val, file):       #Check contents of file and return True if contents are the same as value passed to function
    while True:                                                 #Continuously attempt to write to file until it is not in use
        try:                                                    #Exception handling for IOError if file is already in use
            with open(file,'r') as f:                           #Attempt to open file and create file handle
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)   #Lock file to prevent race condition from parallel process trying to access same file
                f.seek(0)                                       #set file position to start overwrite
                contents = f.read().strip()                     #assign contents of file to variable to save before closing 
                fcntl.flock(f, fcntl.LOCK_UN)                   #unlock file              
                f.close()                                       #close file
                return contents == val                          #break loop and return result of logical comparision of file contents and passed value. also  
        except IOError:                                         #error message if file is use and IOError is raised 
            print file," is already in use."

def getCurrentTemp():  

    ain_value = ADC.read(tempPin)
    ain_voltage = 1.8 * ain_value
    sensor_output_voltage = ain_voltage * 2
    f = sensor_output_voltage * 100 
    temp = str("%3.1f" % f)
	
    return float(temp[1:])
	
def turnACoff():
    GPIO.output(ACpin, GPIO.HIGH)
    fileOverWrite("off",ACfile)
	
def turnACon():
    GPIO.output(ACpin, GPIO.LOW)
    fileOverWrite("on ",ACfile)	
	
def checkACon():
    return fileCheck("on", ACfile)
	

	