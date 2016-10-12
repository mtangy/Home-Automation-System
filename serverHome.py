import Home_Automation
import socket # Import socket module
import time

s = socket.socket() # Create a socket object
port = 4            # Reserve a port for your service.
s.bind(('', port))  # Bind to the port
s.listen(5)   # Now wait for client connection.

f = open('serverLog.txt', 'w')

c, addr = s.accept()       # Establish connection with client.
addr = str(addr[0])
f.write(str(addr)+" - "+time.strftime("%H:%M:%S")+"\n")

if(addr[0:7] == '192.168'):  #checks that client IP is local

    while True:                               #constantly run process  
        packetContents = str(c.recv(1024))    #wait for Rpi client to send packet indicating door changes state
        print packet contents                 #print packet contents for debugging purposes 
		
        if packetContents == "door open" and Home_Automation.checkACon():  #Check if door is open and AC is on
            Home_Automation.turnACoff()                               #rewrite state of file now that AC is off
        else:
            continue

        if packetContents == "door closed" and not Home_Automation.checkACon(): 
            Home_Automation.turnACon()
        else:
            continue

else:

    print "address not local"

    f.write("client from outside subnet\n")
    c.close() # Close the connection
