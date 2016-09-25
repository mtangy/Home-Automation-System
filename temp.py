#!/usr/bin/env python

import time
import Adafruit_BBIO.ADC as ADC
#import socket # Import socket module

ADC.setup()

def read_temp_values_cont():
        
        f = read_sensor()

        c = (f - 32) * 5 /9      
        #f2 = s.recv(1024)

        print "%3.1fF" % f
        #print "\nTemperature 2:"+str(f2)

def read_sensor():
        ain_value = ADC.read("P9_40")

        ain_voltage = 1.8 * ain_value

        sensor_output_voltage = ain_voltage * 2

        f = sensor_output_voltage * 100

        return f

if __name__ == '__main__':
        read_temp_values_cont()
        #s.close # Close the socket when done

