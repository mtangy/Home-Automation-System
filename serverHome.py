import Adafruit_BBIO.ADC as GPIO
import socket # Import socket module
import time

s = socket.socket() # Create a socket object
port = 4            # Reserve a port for your service.
s.bind(('', port))  # Bind to the port
s.listen(5)   # Now wait for client connection.

f = open('serverLog.txt', 'w')

pin = "P9_40"
GPIO.setup(pin, GPIO.OUT)

c, addr = s.accept()       # Establish connection with client.
f.write(str(addr)+" - "time.strftime("%H:%M:%S")+"\n")

if(addr[:7] == '192.168'):  #checks that client IP is local
    while True:
        packetContents = str(c.recv(1024))
		
		if packetContents == "door open":
		     relayState = Rs.read().strip()
			 if relayState == "on":
                 GPIO.output(pin, GPIO.HIGH)
				 Rs = open('/usr/local/bin/relayState.txt', 'r+')
				 Rs.seek(0)
				 Rs.write("off")
				 Rs.close()
		     else:
			     continue
		if packetContents == "door closed":
		     relayState = Rs.read().strip()
			 if relayState == "off":
                 GPIO.output(pin, GPIO.LOW)
				 Rs = open('/usr/local/bin/relayState.txt', 'r+')
				 Rs.seek(0)				 
				 Rs.write("on")
				 Rs.close()
		     else:
			     continue		
                 	
else:
    f.write("client from outside subnet\n")
    c.close() # Close the connection
