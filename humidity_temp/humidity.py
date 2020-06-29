#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    convert = temperature * 1.8 + 32

    print ('Temp: {0:0.1f} F  Humidity: {1:0.1f} %'.format(convert, humidity))