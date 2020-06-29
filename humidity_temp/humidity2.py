#!/usr/bin/python3
import os
import sys
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

try:
    f = open('/home/pi/humidity.csv', 'w+')
    if os.stat('/home/pi/humidity.csv').st_size == 0:
            f.write('')
except:
    pass

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    
    convert = temperature * 1.8 + 32

    if humidity is not None and temperature is not None:
        f.write('{0},{1},{2:0.1f}*F,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), convert, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")

    time.sleep(5)
    exit()
