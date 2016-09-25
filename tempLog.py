
#!/usr/bin/env python

import MySQLdb
import time
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.ADC as GPIO

pin = "P9_40"

ADC.setup()
GPIO.setup(pin, GPIO.OUT)

def read_temp_value():
    f = read_sensor()
    c = (f - 32) * 5 /9
    F = "%3.1f" % f

    return F

def read_sensor():
    ain_value = ADC.read(pin)
    ain_voltage = 1.8 * ain_value
    sensor_output_voltage = ain_voltage * 2
    f = sensor_output_voltage * 100
	
    return f

def insertTemp(temp,curs,db):
    with db:    
        curs.execute ("INSERT INTO temps values(CURRENT_DATE(),CURTIME(),"+str(temp)+")")
	    db.commit()
        ##print temp,"committed"

def printData():
    curs=db.cursor()
    curs.execute ("SELECT * FROM temps")
    print "\nDate            Time      Temperature"
    print "======================================="
    num = 0 
    for reading in curs.fetchall():
        print str(reading[0])+"    "+str(reading[1])+"    "+str(reading[2])
        num +=1
    print "Number of enteries printed", num                

if __name__ == '__main__':
    db = MySQLdb.connect("localhost", "mtangy", "*password**", "roomTemps")
    curs=db.cursor()
    iter = 0
    while True:
        temp = 0.0;
        temp = read_temp_value()
		##print temp
        insertTemp(temp,curs,db)
		t = open('/usr/local/bin/temp.txt', 'r')
		utemp = int(t.read().strip())
        t.close()
        if utemp > temp:
            GPIO.output(pin, GPIO.HIGH)
            Rs = open('/usr/local/bin/relayState.txt', 'r+')
            Rs.seek(0)
            Rs.write("off")
            Rs.close()           		
        time.sleep(1200)
    
    ##printData()
    ##curs.execute ("SELECT * FROM temps")
    ##print curs.fetchall()	
