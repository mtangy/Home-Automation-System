#!/usr/bin/python          
#^Indicates which interpreter to use 

from time import sleep
from gpiozero import LED, Button, DistanceSensor
import socket                # Import socket module

s = socket.socket()          # Create a socket object for communication

#host = socket.gethostname() # Get local machine name

port = 4                     # Reserve a port for your service.
serverIP = '192.168.1.108'   #static local IP I assigned for my Beaglebone that is acting as a server
s.connect((serverIP, port))  #establish connection to socket on server side 


led = LED(12)                 # LED to indicate when script is complete 
stopButton = Button(15, pull_up=False) #button to stop script 
hcSr = DistanceSensor(echo=13, trigger=7, threshold_distance=0.1)  # threshold distance of 0.1m tells the wait_for()'s 
                                                                   # what distance range (.328in) to pause the script at

while !(stopButton.when_pressed):

    hcSr.wait_for_out_of_range()      #pause script until the change in distance exceeds .328in indicating door is open 
	c.send('door open')               #send packet indicating door is open
    hcSr.wait_for_in_range()          #pause script until distance is back in range indicating door is closed
    c.send('door closed')	           #send packet indicating door is closed
    
s.close                  # Close socket when finished 

led.on()                 #temporarily turn LED off to indicate socket communication is done and script is finished
sleep(5)
led.off()

